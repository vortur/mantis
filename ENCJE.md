# Encje

## Status

```json
{
    "id": "01GCMEPA3Y0PAP9NVN87V6FKHP",
    "created_at": "2022-01-01T00:00:00Z",
    "updated_at": "2022-01-01T00:00:00Z",
    "e_tag": "01GCMER7N5R05JGBY7MDAK34QZ",
    "device_id": "01GCMEV26HE7VWQDWVFNGXGE4H",
    "status": "OK|BUSY|SOFTWARE_ERR|HARDWARE_ERR|NO_CONNECTION",
    "status_description": "It works!",
}
```

## Site

```json
{
    "id": "01GCMEPA3Y0PAP9NVN87V6FKHP",
    "created_at": "2022-01-01T00:00:00Z",
    "updated_at": "2022-01-01T00:00:00Z",
    "e_tag": "01GCMER7N5R05JGBY7MDAK34QZ",
    "type": "SOLAR|WIND|HYDRO",
    "name":"My installation.",
    "user_id": "01GCMF1QWCMAKDJY198KEW2MZC",
    "lat": 54.134510,
    "lon": 15.546856,
    "poly_id": 123452345234523,
    "address_id": "01GCMF1QWCMAKDJY198KEW2MZC",
    "site_details_id": "01GCMJKP02RWQ837A781KBFZ2Q",
}
```

## Site details

```json
{
    "id": "01GCMEPA3Y0PAP9NVN87V6FKHP",
    "created_at": "2022-01-01T00:00:00Z",
    "updated_at": "2022-01-01T00:00:00Z",
    "e_tag": "01GCMER7N5R05JGBY7MDAK34QZ",
    "peak_power": 2000,
    "nominal_power": 1000,
    "efficiency": 0.1234,
}
```

## User

```json
{
    "id": "01GCMEPA3Y0PAP9NVN87V6FKHP",
    "created_at": "2022-01-01T00:00:00Z",
    "updated_at": "2022-01-01T00:00:00Z",
    "e_tag": "01GCMER7N5R05JGBY7MDAK34QZ",
    "name": "Witold K",
    "nick": "jozuenoon",
    "email": "xxx@op.pl",
    "address_id": "01GCMF1QWCMAKDJY198KEW2MZC",
}
```

## Address

```json
{
    "id": "01GCMEPA3Y0PAP9NVN87V6FKHP",
    "created_at": "2022-01-01T00:00:00Z",
    "updated_at": "2022-01-01T00:00:00Z",
    "e_tag": "01GCMER7N5R05JGBY7MDAK34QZ",
    "street": "",
    "city":"",
    "postal_code": "",
    "country": "",
    "region": "",
}
```
## Current generation

Instantaneous power in watts.

```json
{
    "id": "01GCMEPA3Y0PAP9NVN87V6FKHP",
    "created_at": "2022-01-01T00:00:00Z",
    "updated_at": "2022-01-01T00:00:00Z",
    "e_tag": "01GCMER7N5R05JGBY7MDAK34QZ",
    "site_id": "01GCMKEF417CPPM53C35V5M7K8",
    "power": 1000,
}
```

## Energy generation

Energy generated in watt-hour.

```json
{
    "id": "01GCMEPA3Y0PAP9NVN87V6FKHP",
    "created_at": "2022-01-01T00:00:00Z",
    "updated_at": "2022-01-01T00:00:00Z",
    "e_tag": "01GCMER7N5R05JGBY7MDAK34QZ",
    "from_time": "2022-01-01T00:00:00Z",
    "to_time": "2022-01-01T00:00:00Z",
    "site_id": "01GCMKEZVRDB0ZT8QDGHH265AE",
    "energy": 1000,
}
```

## Energy usage

Energy usage in watt-hour.

```json
{
    "id": "01GCMEPA3Y0PAP9NVN87V6FKHP",
    "created_at": "2022-01-01T00:00:00Z",
    "updated_at": "2022-01-01T00:00:00Z",
    "e_tag": "01GCMER7N5R05JGBY7MDAK34QZ",
    "from_time": "2022-01-01T00:00:00Z",
    "to_time": "2022-01-01T00:00:00Z",
    "site_id": "01GCN29KXP0DSHVATZG1QB0V49",
    "energy": 1000,
}
```

## Energy generation forecast

```json
{
    "id": "01GCMEPA3Y0PAP9NVN87V6FKHP",
    "created_at": "2022-01-01T00:00:00Z",
    "updated_at": "2022-01-01T00:00:00Z",
    "e_tag": "01GCMER7N5R05JGBY7MDAK34QZ",
    "poly_id": 123456,
    "from_time": "2022-01-01T00:00:00Z",
    "to_time": "2022-01-01T00:00:00Z",
    "energy": 1000,
    "model": "modelx",
}
```
