package modelx

import (
	"context"
	"time"

	"github.com/shopspring/decimal"
)

type Generation struct {
	ID        uint64
	CreatedAt time.Time
	UpdatedAt time.Time
	ETag      string
	FromTime  time.Time
	ToTime    time.Time
	SiteID    string
	Energy    decimal.Decimal
}

type Sites struct {
	ID            uint64
	CreatedAt     time.Time
	UpdatedAt     time.Time
	ETag          string
	Type          string
	Name          string
	Lat           decimal.Decimal
	Lon           decimal.Decimal
	PolyID        uint64
	AddressID     uint64
	SiteDetailsID uint64
}

//go:generate moq -out repository_moq.go . RepositoryInterface:RepositoryMock
type RepositoryInterface interface {
	EnergyGeneration(ctx context.Context, fromTime, toTime time.Time, sites []uint64, siteType string) ([]*Generation, error)
	Sites(ctx context.Context, sitesPoly []uint64) ([]*Sites, error)
}
