# UAE Weather Trends Dashboard

An interactive Streamlit dashboard that explores temperature and rainfall trends across the UAE over time.

---

## Overview

This project analyzes historical weather data from across the United Arab Emirates to uncover long-term trends in temperature and precipitation. It provides visual and analytical insights into how climate patterns have evolved across different regions and years.

The dashboard is designed to help users, researchers, and policymakers better understand the UAE's environmental conditions, supporting data-driven climate and sustainability initiatives in the region.

---

## Tech Stack

| Category | Tools Used |
|-----------|-------------|
| Programming | Python 3, Pandas, NumPy |
| Visualization | Matplotlib, Plotly Express |
| Dashboard Framework | Streamlit |
| Machine Learning (optional) | Scikit-learn (for regression and trend analysis) |
| Data Source | UAE historical weather dataset (temperature and rainfall) |

---

## Key Features

- **Interactive Filters:** Explore data by year, city, and weather metric (temperature or rainfall).  
- **Multi-Year Comparison:** Compare trends between different years side by side.  
- **Animated Climate Timeline:** Watch how UAE’s temperature changes over decades.  
- **Rolling Averages:** Smooth monthly data to reveal longer-term patterns.  
- **Trend Modeling (Optional):** Use regression to estimate temperature progression.

---

## Insights

- The **lowest average temperatures** occur in January and February, followed by a steady rise into the summer months.  
- **Rainfall** is concentrated mainly between January and March, with little precipitation in the rest of the year.  
- Over the years, a **gradual warming trend** is visible across most UAE regions.

---

## Project Structure

UAE_Weather_Dashboard/
├── data/
│ └── uae_weather.csv
├── app.py
├── requirements.txt
├── README.md
└── assets/
└── screenshots/


---

## How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/UAE-Weather-Dashboard.git
cd UAE-Weather-Dashboard

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the Streamlit dashboard
streamlit run app.py
