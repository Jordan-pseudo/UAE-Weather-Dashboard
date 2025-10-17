import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.linear_model import LinearRegression
import numpy as np

#List and Dictionary for cities and cities files

cities = ["Abu Dhabi", "Ajman", "Dubai", "Fujairah", "Ras Al Khaimah", "Sharjah", "Umm Al Quwain"]

cities_files = {
    "Abu Dhabi": "Abu_Dhabi_weather_1990_today.csv",
    "Ajman": "Ajman_weather_1990_today.csv",
    "Dubai": "Dubai_weather_1990_today.csv",
    "Fujairah": "Fujairah_weather_1990_today.csv",
    "Ras Al Khaimah": "Ras_Al_Khaimah_weather_1990_today.csv",
    "Sharjah": "Sharjah_weather_1990_today.csv",
    "Umm Al Quwain": "Umm_Al_Quwain_weather_1990_today.csv"
}

#City Coordinates
city_coords = {
    "Abu Dhabi": [24.4539, 54.3773],
    "Dubai": [25.2048, 55.2708],
    "Sharjah": [25.3575, 55.3910],
    "Al Ain": [24.2075, 55.7447],
    "Ras Al Khaimah": [25.8007, 55.9762],
    "Fujairah": [25.1288, 56.3265],
    "Ajman": [25.4052, 55.5136]
}

#Creates a dataframe for city coordinates
city_df = pd.DataFrame([
    {"City": city, "Latitude": lat, "Longitude": lon}
    for city, (lat, lon) in city_coords.items()
])

# Sidebar
st.sidebar.title("UAE Weather Dashboard")


#City Selection 
selected_city = st.sidebar.radio("Select City", sorted(cities))
df = pd.read_csv("data/" + cities_files[selected_city])
df["time"] = pd.to_datetime(df["time"])
df["year"] = df["time"].dt.year
df["month"] = df["time"].dt.month

selected_year = st.sidebar.selectbox("Select Year", sorted(df["year"].unique()))

#Year Comparision
st.sidebar.markdown("### Year Comparison")
years_available = sorted(df['year'].unique())
year_1 = st.sidebar.selectbox("Select First Year", years_available)
year_2 = st.sidebar.selectbox("Select Second Year", years_available)


st.sidebar.markdown("Use this menu to explore weather data for " + selected_city)

#Filter Data
df_year = df[df["year"] == selected_year]

#Compute Monthly Averages and Totals
monthly_temp = df_year.groupby("month")["Average Temperature (°C)"].mean().reset_index()
monthly_rain = df_year.groupby("month")["Precipitation (mm)"].sum().reset_index()


st.markdown("## UAE Weather Overview")

# Create two columns: main content (70%) and map (30%)
col_main, col_map = st.columns([100,1])

with col_main:
    st.subheader("UAE Weather Stations")

    # Get coordinates of selected city
    selected_coords = city_coords.get(selected_city, [24.4539, 54.3773])  # Default to Abu Dhabi if missing

    # Create map figure centered on the selected city
    fig_map = px.scatter_mapbox(
        city_df,
        lat="Latitude",
        lon="Longitude",
        hover_name="City",
        zoom=7, 
        height = 400,
        width=400,  
        mapbox_style="carto-positron",
    )

    # Recenter map dynamically
    fig_map.update_layout(
        mapbox_center={"lat": selected_coords[0], "lon": selected_coords[1]},
        mapbox_zoom=9,  
        margin={"r":0, "t":0, "l":0, "b":0} 
    )

    st.plotly_chart(fig_map, use_container_width=True)
    #Title
    st.title(f"{selected_city} Trends - {selected_year}")

    #Insights highlight
    st.markdown("### Yearly Highlights")

    hottest_month = monthly_temp.loc[monthly_temp['Average Temperature (°C)'].idxmax(), 'month']
    coldest_month = monthly_temp.loc[monthly_temp['Average Temperature (°C)'].idxmin(), 'month']
    total_rain = monthly_rain['Precipitation (mm)'].sum()

    col1, col2, col3 = st.columns(3)
    col1.metric("Hottest Month", ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][hottest_month-1])
    col2.metric("Coldest Month", ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][coldest_month-1])
    col3.metric("Total Rainfall (mm)", f"{total_rain:.1f}")

    st.markdown("This dashboard shows temeprature and rainfall patterns across months")

    #Temperature Chart
    st.subheader("Average Monthly Temperature (°C)")
    fig_temp = px.line(
        monthly_temp,
        x="month",
        y="Average Temperature (°C)",
        title=f"Average Monthly Temperature in {selected_year}",
        markers=True
    )
    fig_temp.update_layout(
        xaxis=dict(
            tickmode="array",
            tickvals=list(range(1, 13)),
            ticktext=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        )
    )
    st.plotly_chart(fig_temp, use_container_width=True)

    

    #Rainfall Chart
    st.subheader("Total Monthly Rainfall (mm)")
    fig_temp = px.line(
        monthly_rain,
        x="month",
        y="Precipitation (mm)",
        title=f"Average Monthly rainfall in {selected_year}",
        markers=True
    )
    fig_temp.update_layout(
        xaxis=dict(
            tickmode="array",
            tickvals=list(range(1, 13)),
            ticktext=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        )
    )
    st.plotly_chart(fig_temp, use_container_width=True)


    #Comparision Graph Temperature

    st.subheader(f"Average Monthly Temperature Comparison: {year_1} vs {year_2}")

    # Filter and group
    df_compare = df[df['year'].isin([year_1, year_2])]
    monthly_avg_compare = (
        df_compare.groupby(['year', 'month'])['Average Temperature (°C)'].mean().reset_index()
    )

    # Plot
    fig3, ax3 = plt.subplots(figsize=(10, 4))
    for year in [year_1, year_2]:
        data = monthly_avg_compare[monthly_avg_compare['year'] == year]
        ax3.plot(data['month'], data['Average Temperature (°C)'], marker='o', label=str(year))
    ax3.set_xticks(range(1, 13))
    ax3.set_xticklabels(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    ax3.set_xlabel("Month")
    ax3.set_ylabel("Average Temperature (°C)")
    ax3.legend()
    ax3.grid(True)
    st.pyplot(fig3)

    #Animated chart
    monthly_avg_all = df.groupby(['year', 'month'])['Average Temperature (°C)'].mean().reset_index()

    fig_anim = px.line(
    monthly_avg_all,
    x="month",
    y="Average Temperature (°C)",
    animation_frame="year",
    range_y=[15, 45],  # adjust for your dataset
    title=f"Monthly Temperature Changes in {selected_city} Over the Years",
    labels={"month": "Month", "Average Temperature (°C)": "Temperature (°C)"}
    )

    fig_anim.update_layout(
        xaxis=dict(
            tickmode="array",
            tickvals=list(range(1, 13)),
            ticktext=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        )
    )

    st.plotly_chart(fig_anim, use_container_width=True)

    #Temperature trend Prediction
    annual_avg = df.groupby('year')['Average Temperature (°C)'].mean().reset_index()

    #Trains a Linear Regression model
    X = annual_avg['year'].values.reshape(-1, 1)
    y = annual_avg['Average Temperature (°C)'].values

    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)

    #Plots the Prediction
    st.subheader("Temperature Trend Over the Years (with Linear Fit)")

    fig, ax = plt.subplots(figsize=(10,5))
    ax.scatter(annual_avg['year'], y, label="Actual", color='blue')
    ax.plot(annual_avg['year'], y_pred, color='red', label="Predicted Trend")
    ax.set_xlabel("Year")
    ax.set_ylabel("Average Temperature (°C)")
    ax.legend()
    st.pyplot(fig)

    

    


    # --- Footer ---
    st.markdown("---")
    st.markdown("*Built by Jordan Legesse — NYUAD AI Enthusiast*")