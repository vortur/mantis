package controller

import (
	"context"
	"fmt"
	"time"

	"modelx"

	"github.com/araddon/dateparse"
)

type PredictGenerationRequest struct {
	PolyID   uint64        `json:"poly_id"`
	FromTime string        `json:"from_time"`
	ToTime   string        `json:"to_time"`
	Bucket   time.Duration `json:"bucket"`
	SiteType string        `json:"site_type"`
}

type GenerationPrediction struct {
	Bucket   time.Duration
	FromTime time.Time
	ToTime   time.Time
	Data     []float64
}

type Service struct {
	repo      modelx.RepositoryInterface
	radiation modelx.SolarRadiationInterface
	gis       modelx.GISServerInterface
}

func (s *Service) Predict(ctx context.Context, req *PredictGenerationRequest) (*GenerationPrediction, error) {
	fromTime, err := dateparse.ParseAny(req.FromTime)
	if err != nil {
		return nil, fmt.Errorf("failed to parse time from: %w", err)
	}

	toTime, err := dateparse.ParseAny(req.ToTime)
	if err != nil {
		return nil, fmt.Errorf("failed to parse to time: %w", err)
	}

	sitesPoly := s.gis.GetSitesPoly(req.PolyID)

	sites := s.repo.Sites(ctx, sitesPoly)

	generations, err := s.repo.EnergyGeneration(ctx, fromTime, toTime, sitesPoly, req.SiteType)
	if err != nil {
		return nil, fmt.Errorf("failed to fetch generation: %w", err)
	}

	groupedGens := groupGeneration(generations)

	radiation, err := s.radiation.RadiationHistory(ctx, fromTime, toTime, &modelx.Coord{Lat: req.Lat, Lon: req.Lon})
	if err != nil {
		return nil, fmt.Errorf("failed to get radiation history: %w", err)
	}

	radiationPrediction, err := s.radiation.RadiationPrediction(ctx, fromTime, toTime, &modelx.Coord{Lat: req.Lat, Lon: req.Lon})
	if err != nil {
		return nil, fmt.Errorf("failed to get radiation history: %w", err)
	}

	// Predict for each site...
	for _, gen := range groupedGens {
		predictor := modelx.NaivePrediction{}

		// predictor.Predict(ctx, normalizeGeneration(generation), , radiationPrediction []float64)
	}

	return &GenerationPrediction{}, nil
}

func groupGeneration(gens []*modelx.Generation) [][]*modelx.Generation {
	m := make(map[string][]*modelx.Generation)

	for _, g := range gens {
		m[g.SiteID] = append(m[g.SiteID], g)
	}

	out := make([][]*modelx.Generation, 0, len(m))
	for _, v := range m {
		out = append(out, v)
	}

	return out
}

func radiationNormalization(radiation []*modelx.SolarRadiaiton) []float64 {
}

func normalizeGeneration(generation []*modelx.Generation) []float64 {
	out := make([]float64, 0, len(generation))

	for _, g := range generation {
		out = append(out, g.Energy.Float64())
	}

	return out
}
