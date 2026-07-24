## Superstore Sales: Data Cleaning & EDA Pipeline
A Python-based data engineering and analysis project. This pipeline imports raw retail transaction data, cleans structural anomalies, performs exploratory data analysis (EDA), and exports analytical visualizations along with a cleaned spreadsheet backup.
## 📂 Project Structure
The repository contains exactly 5 core files:

* superstore_sales.csv – The raw, uncleaned input dataset.
* main.py – The master Python script handling the entire pipeline.
* superstore_cleaned.xlsx – The finalized, clean data exported to Excel.
* requirements.txt – The list of Python library dependencies.
* README.md – This project documentation. [1] 

------------------------------
## 🛠️ Technology Stack
The entire pipeline is engineered using standard Python data science libraries:

* Pandas: Handles data loading, structural cleaning, aggregations, and exporting to Excel.
* NumPy: Powers vectorised calculations, conditional feature engineering, and mathematical logic.
* Matplotlib: Renders, customizes, and exports all 2D analytical charts.

------------------------------
## ⚙️ Core Pipeline Stages## 1. Data Cleaning & Transformation

* Missing Values: Imputes missing numeric values with the column mean and categorical blanks with "Unknown". [2] 
* Deduplication: Automatically finds and removes duplicate rows using Pandas.
* Type Casting: Converts date strings into proper datetime format.
* Feature Engineering:
* Uses NumPy to generate a Profit Status column (Profit, Break Even, Loss).
   * Calculates a new Discounted Sales column (Sales * (1 - Discount)).

## 2. Exploratory Data Analysis (EDA)
Computes key business questions using Pandas aggregations:

* Sales performance by product Category and Region.
* Top customers by order count and gross sales volume.
* Average discount trends across categories.
* Monthly sales trends, yearly profit margins, and shipping mode preferences.

## 3. Outlier & Correlation Analysis

* Identifies and filters sales outliers using the Interquartile Range (IQR) method.
* Calculates and maps a correlation matrix across financial variables.

------------------------------
## 🚀 Setup & Execution## Installation
Clone this repository, navigate to the folder, and install the exact dependencies listed in requirements.txt:

pip install -r requirements.txt

## Running the Script
Execute the main file to run the analysis, generate the Excel backup, and save the charts:

python main.py

------------------------------
## 📊 Visualizations Output
Running the script automatically generates and saves the following plots to a /plots directory using Matplotlib:

   1. Bar Chart: Category vs Total Sales
   2. Pie Chart: Sales Distribution by Region
   3. Histogram: Distribution of Sales Values
   4. Scatter Plot: Sales vs Profit Margins
   5. Line Chart: Monthly Sales Trend over time
   6. Box Plot: Profit Spread across Categories
   7. Heatmap: Color-coded Correlation Matrix




