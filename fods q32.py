import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load the dataset (assuming you have a CSV file named 'house_data.csv')
data = pd.read_csv('house32.csv')

# Select the feature for analysis and modeling (e.g., house size)
selected_feature = 'size'

# Perform bivariate analysis
plt.scatter(data[selected_feature], data['price'])
plt.title(f'Bivariate Analysis: {selected_feature} vs. Price')
plt.xlabel(selected_feature)
plt.ylabel('Price')
plt.show()

# Split the data into training and testing sets
X = data[[selected_feature]]
y = data['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model's performance
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R-squared Score: {r2}')

# Visualize the regression line
plt.scatter(X_test, y_test, label='Actual Data')
plt.plot(X_test, y_pred, color='red', label='Regression Line')
plt.title(f'Linear Regression: {selected_feature} vs. Price')
plt.xlabel(selected_feature)
plt.ylabel('Price')
plt.legend()
plt.show()
