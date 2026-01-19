
# Data Lineage Documentation

Generated: 2026-01-20T19:25:15.625026

## Source
- File: climate_change_indicators.csv
- Description: FAO Climate Change Indicators - Surface Temperature Change
- Rows: 225

## Raw Layer
- File: data/raw/climate_indicators_raw_20260120_192515.csv
- Contains exact copy of source with metadata columns added

## Cleaned Layer
- File: data/cleaned/climate_indicators_cleaned_20260120_192515.csv
- Columns: ['country', 'iso3', 'temp_2000', 'temp_2010', 'temp_2020', 'temp_2022', '_cleaned_at']

## Transformations Applied
1. Added metadata columns (_source_file, _extracted_at, _row_num) to track data lineage
2. Selected only relevant columns: Country, ISO3, F2000, F2010, F2020, F2022
3. Renamed columns to database-friendly format (lowercase with underscores)
4. Added _cleaned_at timestamp to track when transformation occurred
5. Saved raw layer to data/raw/ directory for data preservation
6. Saved cleaned layer to data/cleaned/ directory for downstream use
