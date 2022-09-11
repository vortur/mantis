// Code generated by moq; DO NOT EDIT.
// github.com/matryer/moq

package modelx

import (
	"context"
	"sync"
	"time"
)

// Ensure, that RepositoryMock does implement RepositoryInterface.
// If this is not the case, regenerate this file with moq.
var _ RepositoryInterface = &RepositoryMock{}

// RepositoryMock is a mock implementation of RepositoryInterface.
//
// 	func TestSomethingThatUsesRepositoryInterface(t *testing.T) {
//
// 		// make and configure a mocked RepositoryInterface
// 		mockedRepositoryInterface := &RepositoryMock{
// 			EnergyGenerationFunc: func(ctx context.Context, fromTime time.Time, toTime time.Time, sites []uint64, siteType string) ([]*Generation, error) {
// 				panic("mock out the EnergyGeneration method")
// 			},
// 			SitesFunc: func(ctx context.Context, sites []uint64) ([]*Sites, error) {
// 				panic("mock out the Sites method")
// 			},
// 		}
//
// 		// use mockedRepositoryInterface in code that requires RepositoryInterface
// 		// and then make assertions.
//
// 	}
type RepositoryMock struct {
	// EnergyGenerationFunc mocks the EnergyGeneration method.
	EnergyGenerationFunc func(ctx context.Context, fromTime time.Time, toTime time.Time, sites []uint64, siteType string) ([]*Generation, error)

	// SitesFunc mocks the Sites method.
	SitesFunc func(ctx context.Context, sites []uint64) ([]*Sites, error)

	// calls tracks calls to the methods.
	calls struct {
		// EnergyGeneration holds details about calls to the EnergyGeneration method.
		EnergyGeneration []struct {
			// Ctx is the ctx argument value.
			Ctx context.Context
			// FromTime is the fromTime argument value.
			FromTime time.Time
			// ToTime is the toTime argument value.
			ToTime time.Time
			// Sites is the sites argument value.
			Sites []uint64
			// SiteType is the siteType argument value.
			SiteType string
		}
		// Sites holds details about calls to the Sites method.
		Sites []struct {
			// Ctx is the ctx argument value.
			Ctx context.Context
			// Sites is the sites argument value.
			Sites []uint64
		}
	}
	lockEnergyGeneration sync.RWMutex
	lockSites            sync.RWMutex
}

// EnergyGeneration calls EnergyGenerationFunc.
func (mock *RepositoryMock) EnergyGeneration(ctx context.Context, fromTime time.Time, toTime time.Time, sites []uint64, siteType string) ([]*Generation, error) {
	if mock.EnergyGenerationFunc == nil {
		panic("RepositoryMock.EnergyGenerationFunc: method is nil but RepositoryInterface.EnergyGeneration was just called")
	}
	callInfo := struct {
		Ctx      context.Context
		FromTime time.Time
		ToTime   time.Time
		Sites    []uint64
		SiteType string
	}{
		Ctx:      ctx,
		FromTime: fromTime,
		ToTime:   toTime,
		Sites:    sites,
		SiteType: siteType,
	}
	mock.lockEnergyGeneration.Lock()
	mock.calls.EnergyGeneration = append(mock.calls.EnergyGeneration, callInfo)
	mock.lockEnergyGeneration.Unlock()
	return mock.EnergyGenerationFunc(ctx, fromTime, toTime, sites, siteType)
}

// EnergyGenerationCalls gets all the calls that were made to EnergyGeneration.
// Check the length with:
//     len(mockedRepositoryInterface.EnergyGenerationCalls())
func (mock *RepositoryMock) EnergyGenerationCalls() []struct {
	Ctx      context.Context
	FromTime time.Time
	ToTime   time.Time
	Sites    []uint64
	SiteType string
} {
	var calls []struct {
		Ctx      context.Context
		FromTime time.Time
		ToTime   time.Time
		Sites    []uint64
		SiteType string
	}
	mock.lockEnergyGeneration.RLock()
	calls = mock.calls.EnergyGeneration
	mock.lockEnergyGeneration.RUnlock()
	return calls
}

// Sites calls SitesFunc.
func (mock *RepositoryMock) Sites(ctx context.Context, sites []uint64) ([]*Sites, error) {
	if mock.SitesFunc == nil {
		panic("RepositoryMock.SitesFunc: method is nil but RepositoryInterface.Sites was just called")
	}
	callInfo := struct {
		Ctx   context.Context
		Sites []uint64
	}{
		Ctx:   ctx,
		Sites: sites,
	}
	mock.lockSites.Lock()
	mock.calls.Sites = append(mock.calls.Sites, callInfo)
	mock.lockSites.Unlock()
	return mock.SitesFunc(ctx, sites)
}

// SitesCalls gets all the calls that were made to Sites.
// Check the length with:
//     len(mockedRepositoryInterface.SitesCalls())
func (mock *RepositoryMock) SitesCalls() []struct {
	Ctx   context.Context
	Sites []uint64
} {
	var calls []struct {
		Ctx   context.Context
		Sites []uint64
	}
	mock.lockSites.RLock()
	calls = mock.calls.Sites
	mock.lockSites.RUnlock()
	return calls
}