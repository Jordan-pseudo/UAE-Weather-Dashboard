# UAE-Weather-Dashboard

## 📍 Project Overview

This project analyzes long-term weather trends in the United Arab Emirates, focusing on average temperature and precipitation patterns.
The goal is to explore how climatic variables change across months and years, and to present these insights through clear data visualizations.

## 🧠 Objectives

Clean and prepare raw weather data for analysis

Explore temperature and precipitation trends over time

Visualize seasonal patterns (e.g., hottest and coolest months)

Build a foundation for an interactive weather dashboard

## 📂 Dataset

Source: (Insert your source — e.g., Kaggle: UAE Weather Data 1990–2023)

File: uae_weather.csv

Columns used:

time – date of observation

Average Temperature (°C)

Minimum Temperature (°C)

Maximum Temperature (°C)

Precipitation (mm)

## 🧹 Data Cleaning Steps

Converted the time column to a datetime object

Extracted year and month for trend analysis

Removed missing or irrelevant data (e.g., snow depth)

Grouped by month to calculate average temperature and total precipitation

## 📊 Key Insights (Example: Abu Dhabi 1990–2023)
## 🌡️ Temperature

The average temperature reaches its lowest values in January and February, followed by a steady increase through spring.
It peaks between June and August, before gradually declining toward the end of the year.
This consistent cycle reflects Abu Dhabi’s desert climate.

## 🌧️ Precipitation

Rainfall is low throughout the year, with occasional peaks between January and March.
Outside these months, precipitation levels remain minimal, aligning with the UAE’s arid weather conditions.

## 🛠️ Tools & Libraries

Python – Data processing and visualization

Pandas – Data cleaning and aggregation

Matplotlib – Static visualizations

(Optional: add Plotly, Streamlit, etc., once you use them)

## 📈 Example Visualization

(Insert a screenshot or chart later)

plt.figure(figsize=(10,5))
plt.plot(monthly_avg["month"], monthly_avg["Average Temperature (°C)"], marker="o")
plt.title("Average Monthly Temperature in Abu Dhabi - 2023")
plt.xlabel("Month")
plt.ylabel("Average Temperature (°C)")
plt.grid(True)
plt.show()

## 💭 Reflections

This project helped me strengthen my skills in:

Data cleaning and preprocessing using Pandas

Grouping and aggregating data by time periods

Building visual narratives with Matplotlib

Interpreting climate data in a real-world context

## 🚀 Next Steps

Extend the analysis to multiple UAE cities

Add interactive visualizations using Plotly or Streamlit

Explore correlations between temperature, humidity, and precipitation

Incorporate predictive models for future weather patterns

## 👨‍💻 Author

Jordan Legesse — NYU Abu Dhabi ‘29 | Aspiring AI Engineer/Data Scientist
📬 Feel free to connect with me on LinkedIn or GitHub!
