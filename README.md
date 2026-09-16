# 🌍 Global Population Growth Analysis and Future Population Prediction Using Machine Learning

## 📌 Project Overview

This project analyzes global population growth patterns using historical population data and applies Machine Learning techniques to predict future population trends.

The project uses population data from the World Bank World Development Indicators and covers 217 countries from 1960 to 2025.

Future population predictions are generated for the period 2026–2035 using a Global Linear Regression model.

---

## 🎯 Project Objectives

- Analyze historical global population trends.
- Explore population growth patterns across countries.
- Clean and preprocess population data.
- Perform Exploratory Data Analysis (EDA).
- Create meaningful features for Machine Learning.
- Develop and evaluate Machine Learning models.
- Validate the final model using historical data.
- Predict population for 2026–2035.
- Develop an interactive Streamlit dashboard for population analysis and prediction.

---

## 📊 Dataset

### Data Source

**World Bank — World Development Indicators (WDI)**

### Indicator

**Population, total**

### Indicator Code

`SP.POP.TOTL`

### Coverage

- Countries: 217
- Historical period: 1960–2025
- Forecast period: 2026–2035

---

## 🗂️ Project Structure

```text
Global Population Growth Analysis/
│
├── data/
│   ├── raw/
│   │   ├── API_SP.POP.TOTL_DS2_en_csv_v2_350115.csv
│   │   ├── Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_350115.csv
│   │   └── Metadata_Indicator_API_SP.POP.TOTL_DS2_en_csv_v2_350115.csv
│   │
│   └── processed/
│       └── Global_Population_Cleaned.csv
│
├── notebooks/
│   ├── 01_Data_Acquisition.ipynb
│   ├── 02_Data_Understanding.ipynb
│   ├── 03_Data_Cleaning.ipynb
│   ├── 04_EDA.ipynb
│   ├── 05_Feature_Engineering.ipynb
│   ├── 06_ML_Data_Preparation.ipynb
│   ├── 07_Machine_Learning_Models.ipynb
│   ├── 08_Model_Visualization.ipynb
│   ├── 09_Future_Population_Prediction.ipynb
│   └── 15_Model_Validation_and_Improvement.ipynb
│
├── src/
│   ├── data_acquisition.py
│   ├── data_understanding.py
│   ├── data_cleaning.py
│   ├── eda.py
│   ├── feature_engineering.py
│   └── prediction.py
│
├── outputs/
│   ├── figures/
│   ├── tables/
│   └── models/
│
├── reports/
│
├── app.py
├── requirements.txt
└── README.md