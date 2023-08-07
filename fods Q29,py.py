from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# Load the dataset
data = load_iris()
X = data.data
y = data.target

# Split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a model (you can replace this with your own trained model)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Ask the user for input
feature_names = data.feature_names
target_names = data.target_names

print("Available features:", feature_names)
selected_features = input("Enter the indices of the features (separated by space): ").split()
selected_features = [int(idx) for idx in selected_features]
selected_target = int(input("Enter the index of the target variable: "))

# Evaluate the model
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted', labels=[selected_target])
f1 = f1_score(y_test, y_pred, average='weighted')

# Display the evaluation metrics
print("Evaluation Metrics:")
print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-Score: {f1:.2f}")
