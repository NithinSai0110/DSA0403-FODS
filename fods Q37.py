import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load and Prepare Data
data = pd.read_csv("csv37.csv")

# Step 3: Explore the Data
print(data.head())
print(data.describe())

# Step 4: Visualize the Data

# Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(data['study_time'], data['exam_score'])
plt.title('Study Time vs Exam Score')
plt.xlabel('Study Time (hours)')
plt.ylabel('Exam Score')
plt.show()

# Regression Plot
plt.figure(figsize=(10, 6))
sns.regplot(x='study_time', y='exam_score', data=data)
plt.title('Study Time vs Exam Score')
plt.xlabel('Study Time (hours)')
plt.ylabel('Exam Score')
plt.show()

# Correlation Heatmap
correlation_matrix = data.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
