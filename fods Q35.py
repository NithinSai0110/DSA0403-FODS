import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Step 1: Load and preprocess the data
# Load your dataset here, replace 'your_dataset.csv' with your actual data file
data = pd.read_csv('csv35.csv')

# Assuming your data has columns: 'CustomerID', 'TotalSpent', 'Frequency'
X = data[['TotalSpent', 'Frequency']]

# Step 1: Data Preprocessing
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 2: Determine the number of clusters using the Elbow Method
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

# From the elbow method, choose the optimal number of clusters (K)
optimal_k = 3

# Step 3: Building the K-Means Model
kmeans = KMeans(n_clusters=optimal_k, init='k-means++', max_iter=300, n_init=10, random_state=0)
kmeans.fit(X_scaled)

# Step 4: Analyze the Results
data['Cluster'] = kmeans.labels_

# Step 5: Tailoring Marketing Strategies
cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)

# Visualize the clusters
plt.scatter(X['TotalSpent'], X['Frequency'], c=data['Cluster'], cmap='rainbow')
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], s=300, c='black', marker='X')
plt.title('Customer Segmentation')
plt.xlabel('Total Amount Spent')
plt.ylabel('Frequency of Visits')
plt.show()

# Interpret clusters
for i in range(optimal_k):
    cluster_data = data[data['Cluster'] == i]
    print(f"Cluster {i} - Mean Total Spent: {cluster_data['TotalSpent'].mean()}, Mean Frequency: {cluster_data['Frequency'].mean()}")

# Now you can tailor your marketing strategies based on the customer segments you've identified.
