import numpy as np
import scipy.stats as stats

# Sample data for website design A and website design B (replace this with your actual data)
design_a_conversion_rates = [0.12, 0.15, 0.10, 0.14, 0.18]  # List of conversion rates for design A
design_b_conversion_rates = [0.09, 0.11, 0.08, 0.10, 0.12]  # List of conversion rates for design B

# Perform the independent two-sample t-test
t_statistic, p_value = stats.ttest_ind(design_a_conversion_rates, design_b_conversion_rates)

# Set the significance level (alpha)
alpha = 0.05

# Compare the p-value with the significance level
if p_value < alpha:
    print("There is a statistically significant difference in the mean conversion rates between website design A and website design B.")
else:
    print("There is no statistically significant difference in the mean conversion rates between website design A and website design B.")
