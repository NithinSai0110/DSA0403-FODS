import pandas as pd

# Sample data (replace this with your actual data)
data = {
    'Age': [25, 30, 35, 40, 25, 30, 40, 35, 30, 25, 40, 30, 35, 25],
    'Purchase': [1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1],
    'Purchase_Date': pd.date_range(start='2023-07-01', periods=14, freq='D')
}

# Create a Pandas DataFrame
sales_data = pd.DataFrame(data)

# Filter data for customers who made a purchase in the past month
current_date = pd.to_datetime('2023-08-03')
past_month_purchases = sales_data[sales_data['Purchase_Date'] >= current_date - pd.DateOffset(months=1)]

# Calculate the frequency distribution of ages for customers who made a purchase in the past month
age_frequency = past_month_purchases['Age'].value_counts().sort_index()

# Print the frequency distribution
print(age_frequency)
