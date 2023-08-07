import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

# Load and preprocess the data
data = pd.read_csv('medicalcsv34.csv')  # Replace with your dataset path

# Preprocessing: Convert categorical variables to numerical using label encoding
label_encoder = LabelEncoder()
data['gender'] = label_encoder.fit_transform(data['gender'])
data['treatment_outcome'] = label_encoder.fit_transform(data['treatment_outcome'])

# Perform one-hot encoding for 'blood_pressure' and 'cholesterol'
data = pd.get_dummies(data, columns=['blood_pressure', 'cholesterol'], drop_first=True)

# Split data into features (X) and target (y)
X = data.drop('treatment_outcome', axis=1)
y = data['treatment_outcome']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build and train the KNN model
k = 3  # Number of neighbors
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Convert class labels back to their original values
y_test_original = label_encoder.inverse_transform(y_test)
y_pred_original = label_encoder.inverse_transform(y_pred)

# Evaluate the model's performance
accuracy = accuracy_score(y_test_original, y_pred_original)
precision = precision_score(y_test_original, y_pred_original, pos_label='Good')
recall = recall_score(y_test_original, y_pred_original, pos_label='Good')
f1 = f1_score(y_test_original, y_pred_original, pos_label='Good')

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

# Display classification report for more detailed metrics
print("Classification Report:\n", classification_report(y_test_original, y_pred_original))
