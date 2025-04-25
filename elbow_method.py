import numpy as np
import matplotlib.pyplot as plt
import random

# Function to calculate Euclidean Distance
def euclidean_distance(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2))

# K-Means Algorithm (Custom Implementation)
def kmeans(points, k, max_iters=100):
    n = points.shape[0]
    
    # Randomly Initialize k Centroids
    centroids = points[random.sample(range(n), k)]
    
    for _ in range(max_iters):
        # Assign Points to the Nearest Centroid
        clusters = [[] for _ in range(k)]
        for p in points:
            distances = [euclidean_distance(p, c) for c in centroids]
            cluster_index = np.argmin(distances)
            clusters[cluster_index].append(p)
        
        # Compute New Centroids
        new_centroids = np.array([np.mean(cluster, axis=0) if cluster else centroids[i] for i, cluster in enumerate(clusters)])

        # Stop if Centroids Don't Change
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids
    
    # Compute Sum of Squared Errors (SSE)
    sse = sum(euclidean_distance(p, centroids[np.argmin([euclidean_distance(p, c) for c in centroids])]) ** 2 for p in points)
    
    return sse

# Generate Example Data Points (Change This for an Exam)
data_points = np.array([
    [2,3], [3,5], [5,3], [6,8], [8,8], [7,6], [9,5], [4,2], [2,8], [6,4]
])

# Run the Elbow Method for Different k Values
k_values = range(1, 10)  # Test k from 1 to 10
sse_values = [kmeans(data_points, k) for k in k_values]

# Plot the Elbow Curve
plt.figure(figsize=(8, 5))
plt.plot(k_values, sse_values, marker='o', linestyle='-', color='b')
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Sum of Squared Errors (SSE)")
plt.title("Elbow Method for Finding Optimal k")
plt.xticks(k_values)
plt.show()