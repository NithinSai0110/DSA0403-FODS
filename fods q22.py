import pandas as pd
import numpy as np
import scipy.stats as stats

# Step 1: Read the CSV file and load the data into a pandas DataFrame
df = pd.read_csv("customerreviews.csv")

# Step 2: Calculate the average rating and standard deviation for the product category
average_rating = df['rating'].mean()
std_dev = df['rating'].std()

# Step 3: Define the confidence level and sample size
confidence_level = 0.95  # You can adjust this if needed (e.g., 0.99 for 99% confidence)
sample_size = len(df)

# Step 4: Calculate the confidence interval
margin_of_error = stats.norm.ppf((1 + confidence_level) / 2) * (std_dev / np.sqrt(sample_size))
lower_bound = average_rating - margin_of_error
upper_bound = average_rating + margin_of_error

# Step 5: Print the results
print("Average rating:", average_rating)
print(f"Confidence Interval ({confidence_level * 100}%): {lower_bound:.2f} to {upper_bound:.2f}")
