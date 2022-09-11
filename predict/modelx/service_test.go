package modelx

import (
	"context"
	"reflect"
	"testing"
)

func Test_naivePredict(t *testing.T) {
	tests := []struct {
		name                string
		generation          [][]float64
		radiation           []float64
		radiationPrediction []float64
		want                []float64
		wantErr             bool
	}{
		{
			name: "",
			generation: [][]float64{
				{2, 3, 4, 5, 6},
				{1, 2, 3, 4, 5},
			},
			radiation:           []float64{0.5, 1.5, 2.5, 3.5, 4.5},
			radiationPrediction: []float64{1.2, 1.5, 1.2, 1.2, 4.5},
			want:                []float64{1, 1, 1, 1, 1},
			wantErr:             false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, err := naivePredict(context.Background(), tt.generation, tt.radiation, tt.radiationPrediction)
			if (err != nil) != tt.wantErr {
				t.Errorf("naivePredict() error = %v, wantErr %v", err, tt.wantErr)

				return
			}
			if !reflect.DeepEqual(len(got), len(tt.want)) {
				t.Errorf("naivePredict() = %v, want %v", got, tt.want)
			}
		})
	}
}
