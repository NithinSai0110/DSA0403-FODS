from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np

def get_user_input():
    features = []
    num_features = int(input("Enter the number of symptom features: "))
    for i in range(num_features):
        feature_value = float(input(f"Enter value for feature {i+1}: "))
        features.append(feature_value)
    return np.array(features).reshape(1, -1)

def main():
    # Sample dataset with symptoms and labels
    # Replace this with your actual dataset
    symptoms = [[1.2, 2.3], [2.1, 3.4], [3.5, 2.9], [2.8, 1.5], [1.0, 3.0]]
    labels = [0, 0, 1, 1, 1]

    # Create a KNN classifier
    k = int(input("Enter the value of k (number of neighbors): "))
    knn = KNeighborsClassifier(n_neighbors=k)

    # Train the model using the dataset
    knn.fit(symptoms, labels)

    # Get user input for new patient's features
    new_patient_features = get_user_input()

    # Predict the medical condition for the new patient
    prediction = knn.predict(new_patient_features)

    if prediction[0] == 0:
        print("The patient is predicted to have no medical condition.")
    else:
        print("The patient is predicted to have the medical condition.")

if __name__ == "__main__":
    main()
