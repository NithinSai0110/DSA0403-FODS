import numpy as np
from sklearn.linear_model import LogisticRegression

# Sample dataset - Replace this with your own dataset
# Format: [usage minutes, contract duration] -> churn status (0: not churned, 1: churned)
# You should replace this with your actual dataset
dataset = [
    [1000, 12, 0],
    [800, 6, 1],
    [1200, 24, 0],
    [600, 18, 1],
    [1500, 36, 0]
]

# Extract features (X) and target (y) from the dataset
X = np.array([data[:2] for data in dataset])
y = np.array([data[2] for data in dataset])

# Create a logistic regression model and fit it to the data
model = LogisticRegression()
model.fit(X, y)

def predict_churn(usage_minutes, contract_duration):
    # Prepare the input features as a numpy array
    new_customer = np.array([[usage_minutes, contract_duration]])

    # Predict the churn status for the new customer
    predicted_churn = model.predict(new_customer)[0]
    return predicted_churn

if __name__ == "__main__":
    print("Enter the features of the new customer:")
    usage_minutes = float(input("Usage minutes: "))
    contract_duration = int(input("Contract duration (in months): "))

    churn_status = predict_churn(usage_minutes, contract_duration)
    if churn_status == 0:
        print("The new customer is not likely to churn.")
    else:
        print("The new customer is likely to churn.")
