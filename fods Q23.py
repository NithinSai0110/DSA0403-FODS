import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Sample data (replace these with your actual data)
control_group = np.array([3.1, 3.2, 2.9, 3.3, 2.8, 3.0, 3.1, 3.4, 3.2, 3.3])
treatment_group = np.array([3.6, 3.7, 3.8, 3.5, 3.9, 3.4, 3.6, 3.5, 3.7, 3.8])

# Calculate the sample means
mean_control = np.mean(control_group)
mean_treatment = np.mean(treatment_group)

# Calculate the sample sizes
n_control = len(control_group)
n_treatment = len(treatment_group)

# Perform two-sample t-test
t_statistic, p_value = stats.ttest_ind(control_group, treatment_group, equal_var=True)

# Define significance level (alpha)
alpha = 0.05

# Check if p-value is less than alpha
if p_value < alpha:
    print("The new treatment has a statistically significant effect compared to the placebo.")
else:
    print("There is no statistically significant effect of the new treatment compared to the placebo.")

# Create a box plot to visualize the data
plt.boxplot([control_group, treatment_group], labels=['Control', 'Treatment'])
plt.xlabel('Groups')
plt.ylabel('Response')
plt.title('Effectiveness of New Treatment')
plt.show()
