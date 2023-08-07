import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Sample dataset - Replace this with your own dataset
# Format: [area, number of bedrooms, location] -> price
# You should replace this with your actual dataset
dataset = [
    [1000, 2, 'City A', 250000],
    [1200, 3, 'City B', 300000],
    [1500, 4, 'City A', 400000],
    [800, 1, 'City B', 180000],
    [2000, 5, 'City C', 550000]
]

# Convert the dataset to a pandas DataFrame
columns = ['area', 'num_bedrooms', 'location', 'price']
df = pd.DataFrame(dataset, columns=columns)

# Perform one-hot encoding on the 'location' feature
df_encoded = pd.get_dummies(df, columns=['location'], drop_first=True)

# Extract features (X) and target (y) from the dataset
X = df_encoded.drop(columns='price').values
y = df_encoded['price'].values

# Create a linear regression model and fit it to the data
model = LinearRegression()
model.fit(X, y)

def predict_house_price(area, num_bedrooms, location):
    # Prepare the input features as a numpy array with one-hot encoding
    location_values = [0] * (len(df['location'].unique()) - 1)
    location_values[df['location'].unique().tolist().index(location) - 1] = 1

    new_house = np.array([[area, num_bedrooms] + location_values])

    # Predict the price of the new house
    predicted_price = model.predict(new_house)[0]
    return predicted_price

if __name__ == "__main__":
    print("Enter the features of the new house:")
    area = float(input("Area (in sq. ft.): "))
    num_bedrooms = int(input("Number of bedrooms: "))
    location = input("Location: ")

    predicted_price = predict_house_price(area, num_bedrooms, location)
    print(f"Predicted price for the new house: ${predicted_price:.2f}")
