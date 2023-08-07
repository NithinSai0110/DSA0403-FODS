import pandas as pd
import numpy as np
from scipy.stats import norm

def calculate_confidence_interval(sample_mean, sample_std, sample_size, confidence_level):
    z_critical = norm.ppf(1 - (1 - confidence_level) / 2)
    margin_of_error = z_critical * (sample_std / np.sqrt(sample_size))
    lower_bound = sample_mean - margin_of_error
    upper_bound = sample_mean + margin_of_error
    return lower_bound, upper_bound

def main():
    # Load the data from the CSV file
    data = pd.read_csv('rare_elements.csv')

    # Ask for user input
    try:
        confidence_level = float(input("Enter the confidence level (between 0 and 1): "))
        precision = float(input("Enter the desired level of precision: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    # Calculate the sample mean and standard deviation
    sample_mean = np.mean(data['concentration'])
    sample_std = np.std(data['concentration'], ddof=1)

    # Calculate the confidence interval for the entire population
    lower_bound, upper_bound = calculate_confidence_interval(sample_mean, sample_std, len(data), confidence_level)

    print(f"Sample mean: {sample_mean:.2f}")
    print(f"Sample standard deviation: {sample_std:.2f}")
    print(f"Confidence interval: [{lower_bound:.2f}, {upper_bound:.2f}]")
    print(f"Precision: ±{precision:.2f}")

if __name__ == "__main__":
    main()
