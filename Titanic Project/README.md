# 🚢 Titanic: Data Analysis & Machine Learning

## 📖 Project Overview
This project analyzes passenger demographics from the tragic 1912 Titanic sinking to uncover patterns influencing survival rates. 

* **Data Source:** [Kaggle's Titanic Competition](https://kaggle.com)
* **Goal:** Ingest passenger records, clean missing values, and visualize survival outcomes based on class, age, and gender.

## 📊 Dataset Reference (`train.csv`)
* **PassengerId / Name / Ticket / Cabin:** Passenger identifiers.
* **Survived:** Survival indicator (`0` = No, `1` = Yes).
* **Pclass:** Ticket class (`1` = 1st, `2` = 2nd, `3` = 3rd).
* **Sex / Age:** Demographics.
* **SibSp / Parch:** Count of family members aboard (siblings/spouses/parents/children).
* **Fare:** Price paid for the ticket.
* **Embarked:** Port of boarding (`C` = Cherbourg, `Q` = Queenstown, `S` = Southampton).

## 🛠️ Tech Stack & Workflow
* **Python 3**: Core script logic.
* **Pandas**: Structural data cleaning, filtering, and handling missing null values.
* **Matplotlib**: Generating distribution charts (Survival vs. Non-Survival distribution).

## 📁 Repository Structure
* `Titanic/`
  * `README.md` — Project documentation.
  * `titanic_analysis.py` — Python script containing cleaning and plotting logic.
  * `train.csv` — Passenger dataset.

