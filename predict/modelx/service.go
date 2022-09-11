package modelx

import (
	"context"
)

type NaivePrediction struct{}

func (NaivePrediction) Predict(ctx context.Context, generation [][]float64, radiation []float64, radiationPrediction []float64) ([]float64, error) {
	return naivePredict(ctx, generation, radiation, radiationPrediction)
}

type PredictInterface interface {
	Predict(ctx context.Context, generation [][]float64, radiation []float64, radiationPrediction []float64) []float64
}

func naivePredict(ctx context.Context, generation [][]float64, radiation []float64, radiationPrediction []float64) ([]float64, error) {
	coef := make([][]float64, 0, len(generation))

	// For each generation calculate coefficients.
	for _, g := range generation {
		lcorrs := make([]float64, len(g))

		for i := range g {
			lcorrs[i] = g[i] / radiation[i]
		}

		coef = append(coef, lcorrs)
	}

	// Reduce to average coefficient.
	m := make([]float64, 0, len(coef))
	for _, c := range coef {
		m = append(m, mean(c))
	}

	out := make([]float64, len(radiationPrediction))

	for i, rp := range radiationPrediction {
		for _, c := range m {
			out[i] += c * rp
		}
	}

	return out, nil
}

func mean(data []float64) float64 {
	if len(data) == 0 {
		return 0
	}

	var sum float64
	for _, d := range data {
		sum += d
	}

	return sum / float64(len(data))
}
