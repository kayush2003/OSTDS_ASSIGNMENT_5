# 🛍️ Retail Sales Analysis Using Apache Spark

This project analyzes a retail sales dataset using **Apache Spark (PySpark)** to extract insights that can help improve inventory management, optimize marketing strategies, and enhance customer satisfaction.

---

## 📌 Project Objective

To solve a real-world Big Data problem using Apache Spark by:

- Ingesting and cleaning large datasets.
- Performing meaningful data transformations.
- Analyzing sales data to uncover key insights.
- Visualizing sales trends.
- Optimizing Spark performance.
- Providing actionable business recommendations.

---

## 🧾 Dataset Description

The dataset includes the following fields:

- `TransactionID`
- `Date`
- `CustomerID`
- `Gender`
- `Age`
- `Product Category`
- `Quantity`
- `Price per Unit`
- `Total Amount`
- `StoreID`

> 📁 Dataset: [Retail Sales Data Set.csv](Retail%20Sales%20Data%20Set.csv)

---

## 🧪 Technologies Used

- **Apache Spark (PySpark)**
- **Python 3.x**
- **Matplotlib**
- **Jupyter Notebook / Python Script**
- (Optional) **VS Code / Any IDE**

---

## ⚙️ Features Implemented

### 1. Data Ingestion & Cleaning
- Load CSV using `spark.read.csv`
- Drop missing and duplicate entries
- Convert `Date` to `yyyy-MM-dd` format

### 2. Data Transformation
- Calculate total sales per product category
- Aggregate total sales by store and customer
- Extract `Month` and `Year` for trend analysis

### 3. Data Analysis & Insights
- **Top-Selling Products**: Highest total revenue by category
- **Top-Performing Stores**: Based on sales volume
- **Most Valuable Customers**: Based on purchase amount
- **Monthly Sales Trends**: Seasonal insights

### 4. Visualization
- Line plot of monthly sales (`monthly_sales_trend.png`)

### 5. Optimization Techniques
- Data caching
- Repartitioning
- Tips on using broadcast joins for small lookup tables

---

## 📊 Sample Visual Output

![Monthly Sales Trend](monthly_sales_trend.png)

---

## 📂 Folder Structure

RetailSalesAnalysis/ ├── Retail Sales Data Set.csv ├── retail_sales_analysis.py ├── report.txt ├── monthly_sales_trend.png └── README.md

---

## 📝 How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/RetailSalesAnalysis.git
cd RetailSalesAnalysis
2. Install Required Packages
pip install pyspark matplotlib
3. Run the Script
python retail_sales_analysis.py


