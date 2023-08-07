import numpy as np
from sklearn.cluster import KMeans

# Sample dataset - Replace this with your own dataset
# Format: [feature1, feature2, ...] -> segment (0, 1, 2, ...)
# You should replace this with your actual dataset
dataset = [
    [10, 5],
    [15, 8],
    [3, 6],
    [12, 4],
    [8, 3]
]

# Extract features (X) from the dataset
X = np.array(dataset)

# Define the number of clusters (segments) you want to create
num_clusters = 3

# Create a KMeans clustering model and fit it to the data
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(X)

def segment_new_customer(features):
    # Prepare the input features as a numpy array
    new_customer = np.array([features])

    # Assign the new customer to one of the existing segments
    segment = kmeans.predict(new_customer)[0]
    return segment

if __name__ == "__main__":
    print("Enter the shopping-related features of the new customer:")
    feature1 = float(input("Feature 1: "))
    feature2 = float(input("Feature 2: "))

    segment = segment_new_customer([feature1, feature2])
    print(f"The new customer belongs to segment {segment}.")
