import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load your customer data into a DataFrame (replace 'data.csv' with your data file)
data = pd.read_csv('csv31.csv')

# Drop any irrelevant columns for clustering
data = data.drop(['customer_id', 'other_irrelevant_columns'], axis=1)

# Handle missing values if needed
data = data.dropna()

# Standardize the data (scaling)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Determine the optimal number of clusters using the Elbow Method
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_data)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(8, 6))
plt.plot(range(1, 11), inertia, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.show()

# Choose the optimal number of clusters based on the Elbow Method (let's assume it's 4 in this case)
num_clusters = 4

# Apply KMeans clustering
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
clusters = kmeans.fit_predict(scaled_data)

# Add the cluster labels back to the original DataFrame
data['cluster'] = clusters

# Analyze the characteristics of each cluster
cluster_summary = data.groupby('cluster').mean()
print(cluster_summary)

# Create scatter plots to visualize clusters
plt.figure(figsize=(10, 8))
for cluster_id in range(num_clusters):
    cluster_data = data[data['cluster'] == cluster_id]
    plt.scatter(cluster_data['feature1'], cluster_data['feature2'], label=f'Cluster {cluster_id}')
    
plt.title('Customer Segmentation')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()
