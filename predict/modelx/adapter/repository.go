package adapter

import (
	"context"
	"fmt"
	"time"

	"modelx"

	"github.com/araddon/dateparse"
	"github.com/shopspring/decimal"
	"gorm.io/gorm"
)

func NewRepositorySQL(db *gorm.DB) modelx.RepositoryInterface {
	return &RepositorySQL{
		db: db,
	}
}

type RepositorySQL struct {
	db *gorm.DB
}

type Generation struct {
	ID        uint64
	CreatedAt string
	UpdatedAt string
	ETag      string
	FromTime  string
	ToTime    string
	SiteID    string
	Energy    decimal.Decimal
}

func (r *RepositorySQL) EnergyGeneration(ctx context.Context, fromTime, toTime time.Time, sites []uint64, siteType string) ([]*modelx.Generation, error) {
	var generation []*Generation

	if err := r.db.Raw(`
SELECT
	eg.id,
	eg.created_at,
	eg.updated_at,
	eg.e_tag,
	eg.from_time,
	eg.to_time,
	eg.site_id,
	eg.energy
FROM
	sites as s
LEFT JOIN energy_generations as eg on
	s.id = eg.site_id
WHERE
	poly_id in ?
	AND `+"`type` = ?;", sites, siteType).Scan(&generation).Error; err != nil {
		return nil, fmt.Errorf("failed to make query: %w", err)
	}

	out := make([]*modelx.Generation, 0, len(generation))

	for _, g := range generation {
		out = append(out, &modelx.Generation{
			ID:        g.ID,
			CreatedAt: dateparse.MustParse(g.CreatedAt),
			UpdatedAt: dateparse.MustParse(g.UpdatedAt),
			ETag:      g.ETag,
			FromTime:  dateparse.MustParse(g.FromTime),
			ToTime:    dateparse.MustParse(g.ToTime),
			SiteID:    g.SiteID,
			Energy:    g.Energy,
		})
	}

	return out, nil
}

func (r *RepositorySQL) Sites(ctx context.Context, sites []uint64) ([]*modelx.Sites, error) {
	panic("not implemented") // TODO: Implement
}

func gracefullParse(s string) time.Time {
	out, err := dateparse.ParseAny(s)
	if err != nil {
		return time.Time{}
	}

	return out
}
