package modelx

import (
	"context"
	"time"

	"github.com/oklog/ulid"
	"github.com/shopspring/decimal"
)

// SolarRadiationInterface is common interface for radiation data sources.
//
//go:generate moq -out solar_radiation_moq.go . SolarRadiationInterface:SolarRadiationMock
type SolarRadiationInterface interface {
	RadiationHistory(ctx context.Context, timeFrom, timeTo time.Time, coord *Coord) (*SolarRadiation, error)
	RadiationPrediction(ctx context.Context, timeFrom, timeTo time.Time, coord *Coord) (*SolarRadiation, error)
}

type Coord struct {
	Lat decimal.Decimal
	Lon decimal.Decimal
}

type SolarRadiation struct {
	ID        ulid.ULID
	CreatedAt time.Time
	Coord     Coord

	// Duration between measurements.
	Bucket time.Duration
	Data   []Radiation
}

// All values are expressed in W/m2
// Note about Clear Sky and Cloudy Sky algorithms:
// https://openweathermap.org/api/solar-radiation/behind-solar-radiation-api#introduction
type Radiation struct {
	// Date and time of measurements, Unix, UTC.
	Timestamp time.Time

	CloudySkyGlobalHorizontalIrradiance  decimal.Decimal
	CloudySkyDirectNormalIrradiance      decimal.Decimal
	CloudySkyDiffuseHorizontalIrradiance decimal.Decimal
	ClearSkyGlobalHorizontalIrradiance   decimal.Decimal
	ClearSkyDirectNormalIrradiance       decimal.Decimal
	ClearSkyDiffuseHorizontalIrradiance  decimal.Decimal
}
