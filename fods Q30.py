import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import export_text

# Load the car dataset (replace 'your_dataset.csv' with the actual file name and path)
dataset_path = 'your_dataset.csv'
df = pd.read_csv(dataset_path)

# Extract features and target
X = df.drop('Price', axis=1)
y = df['Price']

# Create and train the Decision Tree Regression model
model = DecisionTreeRegressor()
model.fit(X, y)

def predict_car_price(new_car_features):
    # Convert the user input features into a DataFrame
    new_car_df = pd.DataFrame([new_car_features])

    # Predict the price for the new car
    predicted_price = model.predict(new_car_df)[0]

    # Get the decision path of the prediction
    decision_path = model.decision_path(new_car_df)

    # Convert the decision path to a human-readable format
    decision_rules = export_text(model, feature_names=list(new_car_df.columns))

    return predicted_price, decision_rules

if __name__ == "__main__":
    # Example usage
    new_car_features = {
        'Mileage': 50000,
        'Age': 3,
        'Brand': 'Toyota',
        'EngineType': 'Gas'
    }

    predicted_price, decision_rules = predict_car_price(new_car_features)
    print("Predicted Price:", predicted_price)
    print("\nDecision Path:")
    print(decision_rules)
