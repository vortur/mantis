CREATE TABLE IF NOT EXISTS mx_solar_radiation_history (
    id CHAR(26),
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    coord_lat DECIMAL(8, 6),
    coord_lon DECIMAL(9, 6),
    cloudy_sky_global_horizontal_irradiance DECIMAL(10, 2),
    cloudy_sky_direct_normal_irradiance DECIMAL(10, 2),
    cloudy_sky_diffuse_horizontal_irradiance DECIMAL(10, 2),
    clear_sky_global_horizontal_irradiance DECIMAL(10, 2),
    clear_sky_direct_normal_irradiance DECIMAL(10, 2),
    clear_sky_diffuse_horizontal_irradiance DECIMAL(10, 2),
    timestamp DATETIME NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS mx_prediction (
    id CHAR(26),
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    request_id CHAR(26) NOT NULL,
    poly_id BIGINT UNSIGNED NOT NULL
);

CREATE TABLE IF NOT EXISTS mx_solar_radiation_prediction (
    id CHAR(26),
    prediction_id CHAR(26),
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    cloudy_sky_global_horizontal_irradiance DECIMAL(10, 2),
    cloudy_sky_direct_normal_irradiance DECIMAL(10, 2),
    cloudy_sky_diffuse_horizontal_irradiance DECIMAL(10, 2),
    clear_sky_global_horizontal_irradiance DECIMAL(10, 2),
    clear_sky_direct_normal_irradiance DECIMAL(10, 2),
    clear_sky_diffuse_horizontal_irradiance DECIMAL(10, 2),
    timestamp DATETIME NOT NULL,
    PRIMARY KEY (id)
);