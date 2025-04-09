# Gdańsk Apartment Market Demo

⚠️ **This is a demo application with randomly generated data. All listings and prices are fictional.**

This application demonstrates a Streamlit-based visualization of apartment listings in Gdańsk, Poland. It features an
interactive map and data table with filtering capabilities.

## Features

- Interactive map centered on Gdańsk
- Realistic fake apartment data generation
- Filterable listings by:
    - Price range
    - Area range
    - Number of rooms
    - Neighborhood
- Key statistics display
- Downloadable filtered data
- Responsive layout

## Setup and Installation

1. Install dependencies:

```bash
uv sync
```

2. Generate demo data:

```bash
uv run python3 fake_data_generator.py
```

3. Run the Streamlit app:

```bash
uv run streamlit run app.py
```

## Project Structure

- `app.py` - Streamlit application with interactive map and filters
- `fake_data_generator.py` - Generates realistic fake apartment listings

## Data Generation

The fake data generator creates realistic apartment listings with:

- Random locations within Gdańsk
- Real district and street names
- Realistic price ranges based on area
- Various apartment sizes and features
- Links to humorous cat pictures from http.cat

## Visualization Features

- Interactive map with:
    - City center marker
    - Clustered apartment markers
    - Popup information for each listing
- Filterable data table
- Download option for filtered data
- Key statistics display

## Disclaimer

This is a demo application using randomly generated data. All listings, prices, and other information are fictional and
should not be used for real estate decisions.

