import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

# Step 1: Load and preprocess the data
data = pd.read_csv('car33.csv')  # Replace with your dataset path
# Perform data preprocessing here (e.g., handling missing values, encoding categorical variables)

# Step 2: Select features and target
selected_features = ['engine_size', 'horsepower', 'fuel_efficiency']  # Choose relevant features
target_feature = 'price'

# Step 3: Data Splitting
X = data[selected_features]
y = data[target_feature]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Model Evaluation
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)

print("Mean Absolute Error:", mae)

# Step 6: Feature Importance Analysis
coefficients = model.coef_
feature_importance = pd.Series(coefficients, index=selected_features).sort_values(ascending=False)

print("Feature Importance:")
print(feature_importance)

# Step 7: Provide Insights
# Interpret the coefficients and insights from the feature importance analysis
# For example, if 'engine_size' has the highest positive coefficient, it indicates that as engine size increases, car prices tend to increase.

# Step 8: Visualization (optional)
# You can create visualizations to better understand the relationships between features and target.
