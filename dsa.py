import pandas as pd
import numpy as np
from io import StringIO

# Example input
data = StringIO("""
order_id,product_id,promotion_id,currency,order_value,order_date,origin,order_value_column
1,100,,USD,278.77,2021-01-01,Offline,2124.86
2,200,PROMO_2,,130.73,2021-01-02,Online,4283.22
3,200,,USD,112.01,2021-02-04,Direct,1055.08
4,200,,USD,112.01,2021-02-03,Direct,1055.08
""")

# Load the data
df = pd.read_csv(data)

# Replace missing values in the promotion_id column with "No Promotion"
df['promotion_id'].fillna('No Promotion', inplace=True)

# Convert order_date to datetime and extract month
df['order_date'] = pd.to_datetime(df['order_date'])
df['month'] = df['order_date'].dt.month

# Calculate the total sales for a specific product_id in a given month
df['total_sales'] = df.groupby(['product_id', 'month'])['order_value_column'].transform('sum')

# Pivot the data to get monthly total sales columns
df_pivot = df.pivot_table(index=['order_id', 'product_id', 'promotion_id'], columns='month', values='total_sales', fill_value=0.0).reset_index()

# Ensure the final dataset contains only order_id, product_id, promotion_id, and the monthly total sales columns
final_df = df_pivot[['order_id', 'product_id', 'promotion_id'] + sorted(df_pivot.columns[3:])]

# Return the cleaned dataset as a NumPy array
final_array = final_df.to_numpy()

print(final_array)
