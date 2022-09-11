package adapter

import (
	"context"
	"testing"
	"time"

	"github.com/stretchr/testify/suite"
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

type RepositoryTestSuite struct {
	suite.Suite

	db   *gorm.DB
	repo *RepositorySQL

	dbTable string
}

func TestRepositoryTestSuite(t *testing.T) {
	suite.Run(t, new(RepositoryTestSuite))
}

func (rx *RepositoryTestSuite) SetupSuite() {
	db, err := gorm.Open(sqlite.Open("file::memory:?cache=shared&parseTime=true"), &gorm.Config{})
	rx.NoError(err)

	rx.db = db
	repo, ok := NewRepositorySQL(db).(*RepositorySQL)

	if !ok {
		rx.FailNow("failed")
	}

	rx.repo = repo

	err = rx.db.Exec(`
CREATE TABLE energy_generations (
  id int NOT NULL,
  e_tag varchar(255) DEFAULT NULL,
  from_time datetime(6) DEFAULT NULL,
  to_time datetime(6) DEFAULT NULL,
  site_id bigint(20) DEFAULT NULL,
  energy int(10) DEFAULT NULL,
  created_at datetime(6) DEFAULT NULL,
  updated_at datetime(6) DEFAULT NULL,
  published_at datetime(6) DEFAULT NULL,
  PRIMARY KEY (id)
);`).Error
	rx.Require().NoError(err)

	err = rx.db.Exec(`CREATE TABLE sites (
	  id int NOT NULL,
	  e_tag varchar(255) DEFAULT NULL,
	  ` + "`type`" + ` varchar(255) DEFAULT NULL,
	  name varchar(255) DEFAULT NULL,
	  user_id bigint(20) DEFAULT NULL,
	  lat double DEFAULT NULL,
	  lon double DEFAULT NULL,
	  poly_id bigint(20) DEFAULT NULL,
	  address_id bigint(20) DEFAULT NULL,
	  site_details_id bigint(20) DEFAULT NULL,
	  created_at datetime(6) DEFAULT NULL,
	  updated_at datetime(6) DEFAULT NULL,
	  published_at datetime(6) DEFAULT NULL,
	  PRIMARY KEY (id)
	);`).Error
	rx.Require().NoError(err)
}

func (rx *RepositoryTestSuite) TearDownSuite() {
	db, err := rx.db.DB()
	rx.NoError(err)
	rx.NoError(db.Close())
}

func (rx *RepositoryTestSuite) SetupTest() {
	err := rx.db.Exec(`INSERT INTO sites
	` + "(id, e_tag, `type`, name, user_id, lat, lon, poly_id, address_id, site_details_id)" + `
	VALUES(1, 'xxx', 'SOLAR', 'name', 'user_id', 4.4, 5.5, 1, 2, 3);
	`).Error
	rx.Require().NoError(err)

	err = rx.db.Exec(`INSERT INTO energy_generations
	(id, e_tag, from_time, to_time, site_id, energy)
	VALUES(1, 'xxx', ?, ?, 1, 1000);
	`, time.Now().Add(-time.Hour*12), time.Now().Add(-time.Hour)).Error
	rx.Require().NoError(err)
}

func (rx *RepositoryTestSuite) TearDownTest() {
	rx.db.Exec(`DROP TABLE sites`)
	rx.db.Exec(`DROP TABLE energy_generations`)
}

func (rx *RepositoryTestSuite) TestRepository_EnergyGenerationSimple() {
	data, err := rx.repo.EnergyGeneration(context.Background(), time.Now().Add(-time.Hour*24), time.Now(), []uint64{1, 2, 3, 4}, "SOLAR")
	rx.Require().NoError(err)

	rx.Require().Len(data, 1)
	rx.Require().Equal(data[0].Energy.IntPart(), 1000)
}
