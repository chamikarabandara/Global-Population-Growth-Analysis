import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Global Population Analysis",
    page_icon="🌍",
    layout="wide"
)


# =========================================================
# TITLE
# =========================================================

st.title("🌍 Global Population Growth Analysis & Prediction")

st.markdown(
    """
    Explore historical population trends and future population
    predictions for 217 countries using Machine Learning.
    """
)


# =========================================================
# LOAD DATA
# =========================================================

historical_df = pd.read_csv(
    "data/processed/Global_Population_Cleaned.csv"
)

future_df = pd.read_csv(
    "outputs/tables/final_country_population_forecasts_2026_2035.csv"
)

global_forecast = pd.read_csv(
    "outputs/tables/final_global_population_forecast_2026_2035.csv"
)

prediction_results = pd.read_csv(
    "outputs/tables/linear_regression_predictions.csv"
)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.header("🎛️ Dashboard Controls")

countries = sorted(
    historical_df["Country Name"].unique()
)

selected_country = st.sidebar.selectbox(
    "🌍 Select Country",
    countries
)

selected_year = st.sidebar.selectbox(
    "📅 Select Prediction Year",
    list(range(2026, 2036))
)


# =========================================================
# FILTER COUNTRY DATA
# =========================================================

country_historical = historical_df[
    historical_df["Country Name"] == selected_country
].copy()

country_future = future_df[
    future_df["Country Name"] == selected_country
].copy()

country_actual_predicted = prediction_results[
    prediction_results["Country Name"] == selected_country
].copy()


# =========================================================
# CONVERT POPULATION VALUES
# =========================================================

country_historical["Population_Millions"] = (
    country_historical["Population"] / 1e6
)

country_future["Predicted_Population_Millions"] = (
    country_future["Predicted_Population"] / 1e6
)

country_actual_predicted["Actual_Population_Millions"] = (
    country_actual_predicted["Population"] / 1e6
)

country_actual_predicted["Predicted_Population_Millions"] = (
    country_actual_predicted["Predicted_Population"] / 1e6
)


# =========================================================
# SELECTED YEAR PREDICTION
# =========================================================

selected_prediction = country_future[
    country_future["Year"] == selected_year
]


# =========================================================
# CURRENT POPULATION
# =========================================================

population_2025 = country_historical[
    country_historical["Year"] == 2025
]["Population"].iloc[0]

population_2025_millions = population_2025 / 1e6


# =========================================================
# SELECTED YEAR POPULATION
# =========================================================

predicted_population = (
    selected_prediction["Predicted_Population"].iloc[0]
)

predicted_population_millions = (
    predicted_population / 1e6
)


# =========================================================
# GROWTH CALCULATION
# =========================================================

population_2026 = country_future[
    country_future["Year"] == 2026
]["Predicted_Population"].iloc[0]

population_2035 = country_future[
    country_future["Year"] == 2035
]["Predicted_Population"].iloc[0]

growth_percentage = (
    (population_2035 - population_2026)
    / population_2026
) * 100


# =========================================================
# GLOBAL OVERVIEW
# =========================================================

st.subheader("🌍 Global Population Forecast")

global_2026 = global_forecast[
    global_forecast["Year"] == 2026
]["Predicted_Population_Billion"].iloc[0]

global_2035 = global_forecast[
    global_forecast["Year"] == 2035
]["Predicted_Population_Billion"].iloc[0]

global_growth = (
    (global_2035 - global_2026)
    / global_2026
) * 100


col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Global Population 2026",
        f"{global_2026:.3f} B"
    )

with col2:
    st.metric(
        "Global Population 2035",
        f"{global_2035:.3f} B"
    )

with col3:
    st.metric(
        "Predicted Growth (2026–2035)",
        f"{global_growth:.2f}%"
    )


# =========================================================
# GLOBAL FORECAST CHART
# =========================================================

st.subheader("📈 Global Population Forecast (2026–2035)")

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    global_forecast["Year"],
    global_forecast["Predicted_Population_Billion"],
    marker="o"
)

ax.set_xlabel("Year")
ax.set_ylabel("Population (Billions)")

ax.set_title(
    "Global Population Forecast — 2026 to 2035"
)

ax.grid(True)

st.pyplot(fig)

plt.close(fig)


# =========================================================
# COUNTRY POPULATION OVERVIEW
# =========================================================

st.subheader(
    f"📊 Population Overview — {selected_country}"
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Population in 2025",
        f"{population_2025_millions:,.2f} M"
    )

with col2:
    st.metric(
        f"Prediction for {selected_year}",
        f"{predicted_population_millions:,.2f} M"
    )

with col3:
    st.metric(
        "Predicted Growth (2026–2035)",
        f"{growth_percentage:.2f}%"
    )


# =========================================================
# MODEL PERFORMANCE
# =========================================================

st.subheader("🤖 Final Model Performance")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "MAE",
        "60,514.59"
    )

with col2:
    st.metric(
        "RMSE",
        "243,507.42"
    )

with col3:
    st.metric(
        "R² Score",
        "0.999997"
    )

st.caption(
    "Validation period: 2021–2025 | 217 countries"
)


# =========================================================
# HISTORICAL POPULATION
# =========================================================

st.subheader("📈 Historical Population Trend")

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    country_historical["Year"],
    country_historical["Population_Millions"]
)

ax.set_xlabel("Year")
ax.set_ylabel("Population (Millions)")

ax.set_title(
    f"Historical Population — {selected_country}"
)

ax.grid(True)

st.pyplot(fig)

plt.close(fig)


# =========================================================
# ACTUAL VS PREDICTED
# =========================================================

st.subheader(
    "🎯 Validation: Actual vs Predicted Population"
)

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    country_actual_predicted["Year"],
    country_actual_predicted["Actual_Population_Millions"],
    marker="o",
    label="Actual Population"
)

ax.plot(
    country_actual_predicted["Year"],
    country_actual_predicted["Predicted_Population_Millions"],
    marker="o",
    label="Predicted Population"
)

ax.set_xlabel("Year")
ax.set_ylabel("Population (Millions)")

ax.set_title(
    f"Actual vs Predicted — {selected_country}"
)

ax.legend()

ax.grid(True)

st.pyplot(fig)

plt.close(fig)


# =========================================================
# FUTURE COUNTRY PREDICTION
# =========================================================

st.subheader(
    f"🔮 Future Population Prediction — {selected_country}"
)

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    country_future["Year"],
    country_future["Predicted_Population_Millions"],
    marker="o"
)

ax.set_xlabel("Year")
ax.set_ylabel("Population (Millions)")

ax.set_title(
    f"Population Prediction — {selected_country} (2026–2035)"
)

ax.grid(True)

st.pyplot(fig)

plt.close(fig)


# =========================================================
# PREDICTION TABLE
# =========================================================

st.subheader(
    "📋 Future Population Predictions"
)

display_table = country_future[
    [
        "Year",
        "Predicted_Population_Millions"
    ]
].copy()

display_table.columns = [
    "Year",
    "Predicted Population (Millions)"
]

display_table[
    "Predicted Population (Millions)"
] = (
    display_table[
        "Predicted Population (Millions)"
    ].round(2)
)

st.dataframe(
    display_table,
    use_container_width=True,
    hide_index=True
)


# =========================================================
# MODEL INFORMATION
# =========================================================

st.subheader("🧠 Machine Learning Model")

st.info(
    """
    Final Model: Global Linear Regression

    Data Source: World Bank World Development Indicators

    Historical Data: 1960–2025

    Validation Period: 2021–2025

    Future Prediction Period: 2026–2035

    Number of Countries: 217

    Features Used:
    • Year
    • Previous Year Population
    • Population Lag 2
    • Previous 3-Year Average Population

    Model Validation:
    • MAE: 60,514.59
    • RMSE: 243,507.42
    • R²: 0.999997
    """
)


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption(
    "Global Population Growth Analysis & Prediction | "
    "Machine Learning Capstone Project"
)