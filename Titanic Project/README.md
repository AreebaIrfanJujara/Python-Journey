
# Titanic Data Analysis

A data exploration project focused on cleaning historical passenger data and visualizing survival outcomes using Python.

## 📊 Overview
This project analyzes the demographics and survival rates of passengers aboard the Titanic. The goal is to ingest raw passenger records, handle missing information, and generate visual insights regarding survival distributions.

## 🛠️ Tech Stack & Libraries Used
* **Python 3** - Core scripting logic
* **Pandas** - Data ingestion, handling missing values, and structural data cleaning
* **Matplotlib** - Generating data visualizations and distribution charts

## 🧼 Data Cleaning Process
Before analyzing the results, the dataset is processed to ensure accuracy:
1. **Handling Missing Values:** Dropping or imputing critical columns with null values (such as Passenger Age or Cabin designations).
2. **Data Filtering:** Isolating key features including passenger status, age, gender, and survival indicators.
3. **Data Structuring:** Formatting categories for optimal plotting efficiency.

## 📈 Visualizations
The main analysis produces visualizations to contrast outcomes directly:
* **Survival vs. Non-Survival Distribution:** A bar/pie chart generated via Matplotlib displaying the exact count and proportions of survivors against those who perished.

## 📁 Repository Structure
* `Titanic-Data-Analysis/`
  * `README.md` — Project documentation and summary.
  * `titanic_analysis.py` — The core script containing data manipulation and plotting code.
  * `train.csv` — The underlying passenger dataset.
