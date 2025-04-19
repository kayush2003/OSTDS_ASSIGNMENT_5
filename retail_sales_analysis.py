# retail_sales_analysis.py

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum, desc, to_date, month, year
import matplotlib.pyplot as plt

# Step 1: Spark Session
spark = SparkSession.builder \
    .appName("Retail Sales Analysis") \
    .getOrCreate()

# Step 2: Load Dataset
file_path = "Retail Sales Data Set.csv"  # Adjust path if needed
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Step 3: Data Cleaning
df_cleaned = df.dropna().dropDuplicates()

# Optional: Rename columns for ease
df_cleaned = df_cleaned.withColumnRenamed("Price per Unit", "PricePerUnit") \
                       .withColumnRenamed("Total Amount", "TotalAmount") \
                       .withColumnRenamed("Product Category", "ProductCategory")

# Convert Date to proper format
df_cleaned = df_cleaned.withColumn("Date", to_date(col("Date"), "yyyy-MM-dd"))

# Step 4: Data Transformation
# Total sales per product
sales_per_product = df_cleaned.groupBy("ProductCategory") \
    .agg(_sum("TotalAmount").alias("TotalSales")) \
    .orderBy(desc("TotalSales"))

# Total sales per store
sales_per_store = df_cleaned.groupBy("StoreID") \
    .agg(_sum("TotalAmount").alias("TotalSales")) \
    .orderBy(desc("TotalSales"))

# Total sales per customer
sales_per_customer = df_cleaned.groupBy("CustomerID") \
    .agg(_sum("TotalAmount").alias("TotalSales")) \
    .orderBy(desc("TotalSales"))

# Step 5: Monthly Sales Trend
df_with_month = df_cleaned.withColumn("Month", month("Date")).withColumn("Year", year("Date"))

monthly_sales = df_with_month.groupBy("Year", "Month") \
    .agg(_sum("TotalAmount").alias("MonthlySales")) \
    .orderBy("Year", "Month")

# Collect for visualization
monthly_pd = monthly_sales.toPandas()

# Step 6: Visualization
plt.figure(figsize=(12, 6))
plt.plot(monthly_pd["Month"].astype(str) + "-" + monthly_pd["Year"].astype(str), monthly_pd["MonthlySales"], marker='o')
plt.xticks(rotation=45)
plt.title("Monthly Sales Trend")
plt.xlabel("Month-Year")
plt.ylabel("Sales")
plt.tight_layout()
plt.grid(True)
plt.savefig("monthly_sales_trend.png")
plt.show()

# Step 7: Optimization Tips (Document in Report)
# - Use `.cache()` if reused multiple times: df.cache()
# - Use partitioning if working with large dataset: .repartition("StoreID")
# - Use broadcast joins for small dimension tables
# - Persist data to memory/disk selectively

# Step 8: Save Insights (Optional)
sales_per_product.write.mode("overwrite").csv("output/sales_per_product")
sales_per_store.write.mode("overwrite").csv("output/sales_per_store")
sales_per_customer.write.mode("overwrite").csv("output/sales_per_customer")

spark.stop()
