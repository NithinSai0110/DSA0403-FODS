import numpy as np
import scipy.stats as stats

# Sample data for the drug group (replace this with your actual data)
drug_group_data = [120, 122, 118, 125, 121]  # List of 50 blood pressure measurements

# Sample data for the placebo group (replace this with your actual data)
placebo_group_data = [124, 127, 123, 128, 126]  # List of 50 blood pressure measurements

# Calculate the sample mean and standard deviation for both groups
drug_mean = np.mean(drug_group_data)
drug_std = np.std(drug_group_data, ddof=1)  # ddof=1 for sample standard deviation

placebo_mean = np.mean(placebo_group_data)
placebo_std = np.std(placebo_group_data, ddof=1)  # ddof=1 for sample standard deviation

# Calculate the standard error for both groups (standard deviation divided by the square root of sample size)
drug_se = drug_std / np.sqrt(len(drug_group_data))
placebo_se = placebo_std / np.sqrt(len(placebo_group_data))

# Calculate the t-value for a 95% confidence interval (two-tailed)
t_value = stats.t.ppf(0.975, df=len(drug_group_data) - 1)  # 0.975 for 95% confidence level (two-tailed)

# Calculate the confidence intervals
drug_ci_lower = drug_mean - t_value * drug_se
drug_ci_upper = drug_mean + t_value * drug_se

placebo_ci_lower = placebo_mean - t_value * placebo_se
placebo_ci_upper = placebo_mean + t_value * placebo_se

# Display the results
print("95% Confidence Interval for Mean Reduction in Blood Pressure (Drug Group):")
print(f"Lower Bound: {drug_ci_lower:.2f}")
print(f"Upper Bound: {drug_ci_upper:.2f}\n")

print("95% Confidence Interval for Mean Reduction in Blood Pressure (Placebo Group):")
print(f"Lower Bound: {placebo_ci_lower:.2f}")
print(f"Upper Bound: {placebo_ci_upper:.2f}")
