import pandas as pd
import numpy as np
import scipy.stats as stats

df = pd.read_csv("customerreviews.csv")

average_rating = df['rating'].mean()
std_dev = df['rating'].std()

confidence_level = 0.95
sample_size = len(df)

margin_of_error = stats.norm.ppf((1 + confidence_level) / 2) * (std_dev / np.sqrt(sample_size))
lower_bound = average_rating - margin_of_error
upper_bound = average_rating + margin_of_error

print("Average rating:", average_rating)
print(f"Confidence Interval ({confidence_level * 100}%): {lower_bound:.2f} to {upper_bound:.2f}")
