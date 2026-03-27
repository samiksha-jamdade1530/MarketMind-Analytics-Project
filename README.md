<<<<<<< HEAD
# MarketMind Analytics: Retail & FMCG Analysis

## Project Overview

**MarketMind Analytics** is a retail data analytics project developed to analyze FMCG and retail sales data to extract meaningful business insights. The system performs customer behavior analysis, sales trend analysis, and price prediction using data analytics and machine learning techniques.

The project helps retailers answer important business questions such as:

* Who are the most valuable customers?
* Which products sell the most?
* When do sales increase or decrease?
* How can future prices be predicted?
* Which store factors affect sales?

The system is built using **Python, Streamlit, Pandas, Plotly, and Scikit-learn** to provide interactive dashboards and predictions.

---

## Project Objectives

* Analyze retail sales data
* Understand customer purchase behavior
* Perform RFM customer segmentation
* Visualize sales patterns
* Predict product prices using Machine Learning
* Help businesses make data-driven decisions

---

## System Modules

The project contains **3 main modules**:

1. Market Basket Analysis
2. Price Prediction
3. Sales Analysis

---

## Module 1: Market Basket Analysis (MBA)

### Description

This module analyzes customer transactions and sales behavior. The system accepts a CSV dataset and performs multiple analytical operations to understand customer purchasing patterns.

### Operations Performed

The following analysis is performed:

* Number of Sales Weekly
* Number of Customers Weekly
* Sales per Customer Weekly
* Frequency of Items Sold
* Top Customers by Items Purchased
* Sales per Week Days
* Sales per Months
* Sales per Month Days
* Recency Distribution
* Visit Frequency Distribution
* Monetary Distribution
* RFM Segmentation
* Relationship Between Frequency and Recency

### RFM Segmentation Categories

Customers are grouped based on:

* Recency
* Frequency
* Monetary Value

Customer categories include:

* Premium Customers
* Loyal Customers
* At Risk Customers
* New Customers

### Business Value

This module helps businesses:

* Identify loyal customers
* Improve marketing strategy
* Improve customer retention
* Understand buying patterns

---

## Module 2: Price Prediction

### Description

This module uses **Linear Regression** to predict product prices based on historical sales data.

### Operations

The system predicts prices based on:

* Item features
* Sales history
* Outlet factors
* Product demand

### Algorithm Used

**Linear Regression**

Reason for selection:

* Simple
* Fast
* Interpretable
* Good for trend prediction

### Business Value

Helps businesses:

* Set optimal prices
* Forecast revenue
* Improve profit margins
* Understand price trends

---

## Module 3: Sales Analysis

### Description

This module analyzes how product attributes and outlet characteristics affect sales performance.

### Operations

Analysis includes:

* Item Fat Content (Low Fat vs Regular)
* Outlet Establishment Year
* Outlet Size comparison
* Outlet Location Type (Tier 1, Tier 2, Tier 3)
* Outlet Type comparison
* Item Outlet Sales performance

### Business Value

Helps businesses:

* Optimize inventory
* Understand store performance
* Improve outlet strategy
* Identify high performing products

---

## Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### Libraries Used

### Data Processing

* Pandas
* NumPy

### Visualization

* Plotly
* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn

### Development Tools

* Jupyter Notebook
* VS Code

---

## Project Workflow

The system works in the following steps:

1. Upload CSV dataset
2. Data preprocessing
3. Data cleaning
4. Feature analysis
5. Visualization generation
6. Machine learning prediction
7. Result dashboard display

---

## Dataset Requirements

The dataset should contain fields such as:

Example fields:

* Transaction_ID
* Customer_ID
* Item_ID
* Item_Name
* Quantity
* Price
* Date
* Outlet_Type
* Outlet_Size
* Location_Type

---

## Key Features

* Interactive Dashboard
* CSV Upload Support
* Customer Segmentation
* RFM Analysis
* Sales Trend Analysis
* Machine Learning Prediction
* Business Insight Visualization
* Simple UI

---

## Project Structure

```
MarketMind-Analytics/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── modules/
│     ├── market_basket_analysis.py
│     ├── price_prediction.py
│     ├── sales_analysis.py
│
├── data/
│     ├── sample_data.csv
│
├── database/
│     └── users.db
│
├── assets/
│     └── screenshots
```

---

## Installation and Setup

### Step 1: Clone repository

```
git clone https://github.com/yourusername/MarketMind-Analytics.git
```

### Step 2: Navigate to folder

```
cd MarketMind-Analytics
```

### Step 3: Install dependencies

```
pip install -r requirements.txt
```

### Step 4: Run project

```
streamlit run app.py
```

---

## Results

The system generates:

* Customer segmentation insights
* Sales trend dashboards
* Product performance charts
* Price predictions
* Business decision insights

---

## Future Enhancements

Future improvements may include:

* Deep Learning price prediction
* Recommendation system
* Customer churn prediction
* Demand forecasting
* Real time dashboard
* Power BI integration
* Cloud deployment

---

## Author

**Samiksha Jamdade**

Computer Engineering Student
Data Analytics & AI Enthusiast
Interested in Data Science, AI, and Business Analytics

---

## License

This project is developed for academic and learning purposes.
=======
# MarketMind-Analytics-Project
>>>>>>> 25d2ee989eb50000eab203b45f890b82c686790b
