package modelx

//go:generate moq -out gis_moq.go . GISServerInterface:GISServerMock
type GISServerInterface interface {
	// GetSitesPoly gets list of sites contained inside area.
	GetSitesPoly(area uint64) []uint64
}
