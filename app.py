import folium
import pandas as pd
import streamlit as st
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static

# Constants
CENTER_LAT = 54.3520
CENTER_LON = 18.6466
ZOOM_START = 12
DATA_FILE = "apartments_gdansk.csv"
MAP_HEIGHT = 800
TABLE_HEIGHT = 800


def load_data():
    """Load apartment data from CSV file."""
    try:
        return pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        st.error("No data file found. Please run the fake data generator first.")
        return None


def create_map(df):
    """Create an interactive map with apartment markers."""
    m = folium.Map(
        location=[CENTER_LAT, CENTER_LON],
        zoom_start=ZOOM_START,
        width="100%",
        height="100%",
    )

    # Add city center marker
    folium.Marker(
        location=[CENTER_LAT, CENTER_LON],
        popup="Gdańsk Center",
        icon=folium.Icon(color="red", icon="info-sign"),
    ).add_to(m)

    # Create marker cluster
    marker_cluster = MarkerCluster().add_to(m)

    # Add apartment markers
    for _, row in df.iterrows():
        popup_html = f"""
            <b>{row["title"]}</b><br>
            Price: {row["price"]:,.0f} PLN<br>
            Area: {row["area"]} m²<br>
            Rooms: {row["rooms"]}<br>
            Floor: {row["floor"]}<br>
            <a href='{row["url"]}' target='_blank'>View offer</a>
        """

        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=folium.Popup(popup_html, max_width=300),
            tooltip=row["address"],
        ).add_to(marker_cluster)

    return m


def create_sidebar_filters(df):
    """Create and return sidebar filters."""
    st.sidebar.header("Search Filters")

    # Price range filter
    price_range = st.sidebar.slider(
        "Price Range (PLN)",
        min_value=int(df["price"].min()),
        max_value=int(df["price"].max()),
        value=(int(df["price"].min()), int(df["price"].max())),
    )

    # Area range filter
    area_range = st.sidebar.slider(
        "Area Range (m²)",
        min_value=int(df["area"].min()),
        max_value=int(df["area"].max()),
        value=(int(df["area"].min()), int(df["area"].max())),
    )

    # Number of rooms filter
    rooms = sorted(df["rooms"].unique())
    room_options = [f"{room}-room" for room in rooms if room < 5] + ["5+ rooms"]
    room_mapping = {"5+ rooms": 5}
    room_mapping.update({f"{room}-room": room for room in rooms if room < 5})
    selected_room_types = st.sidebar.multiselect(
        "Number of Rooms", options=room_options, default=room_options
    )
    selected_rooms = [room_mapping[room] for room in selected_room_types]

    # District filter
    districts = sorted(df["district"].unique())
    selected_districts = st.sidebar.multiselect(
        "Neighborhood", options=districts, default=districts
    )

    return price_range, area_range, selected_rooms, selected_districts


def display_statistics(df):
    """Display key statistics."""
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Listings", len(df))
    with col2:
        st.metric("Average Price", f"{df['price'].mean():,.0f} PLN")
    with col3:
        st.metric("Average Area", f"{df['area'].mean():.1f} m²")


def apply_filters(df, price_range, area_range, selected_rooms, selected_districts):
    """Apply all filters to the dataframe."""
    filtered_df = df[
        (df["price"].between(*price_range)) & (df["area"].between(*area_range))
    ]

    if selected_rooms:
        if 5 in selected_rooms:
            filtered_df = filtered_df[
                (filtered_df["rooms"].isin(selected_rooms))
                | (filtered_df["rooms"] >= 5)
            ]
        else:
            filtered_df = filtered_df[filtered_df["rooms"].isin(selected_rooms)]

    if selected_districts:
        filtered_df = filtered_df[filtered_df["district"].isin(selected_districts)]

    return filtered_df


def main():
    # Page config
    st.set_page_config(
        page_title="Gdańsk Apartments",
        page_icon="🏠",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Header
    st.title("🏠 Gdańsk Apartment Market")
    st.warning(
        "⚠️ This is a demo application with randomly generated data. All listings and prices are fictional."
    )

    # Load data
    df = load_data()
    if df is None:
        return

    # Create filters and apply them
    price_range, area_range, selected_rooms, selected_districts = (
        create_sidebar_filters(df)
    )
    filtered_df = apply_filters(
        df, price_range, area_range, selected_rooms, selected_districts
    )

    # Display statistics
    display_statistics(filtered_df)

    # Create two columns for map and table with adjusted ratios
    map_col, table_col = st.columns([1, 1])

    # Map
    with map_col:
        m = create_map(filtered_df)
        folium_static(m, height=MAP_HEIGHT)

    # Table
    with table_col:
        # Format price with PLN for display
        display_df = filtered_df.copy()
        display_df["price"] = display_df["price"].apply(lambda x: f"{x:,.0f} PLN")

        st.dataframe(
            display_df[["title", "price", "area", "rooms", "district", "address"]],
            use_container_width=True,
            height=TABLE_HEIGHT,
        )

        # Download button
        csv = filtered_df.to_csv(index=False)
        st.download_button(
            label="Download listings",
            data=csv,
            file_name="filtered_gdansk_apartments.csv",
            mime="text/csv",
            use_container_width=True,
        )


if __name__ == "__main__":
    main()
