import math

def euclidean_distance(point, cluster_center):
    return math.sqrt((point[0] - cluster_center[0])**2 + (point[1] - cluster_center[1])**2)

def assign_clusters(points, cluster_centers):
    assignments = []
    for point in points:
        distances = [(euclidean_distance(point, center), f'C{i+1}') for i, center in enumerate(cluster_centers)]
        assigned_cluster = min(distances)[1]
        assignments.append((point, distances, assigned_cluster))
    return assignments

def calculate_new_centroids(assignments, cluster_labels):
    new_centroids = {}
    for label in cluster_labels:
        cluster_points = [p[0] for p in assignments if p[2] == label]
        if cluster_points:
            new_centroids[label] = (
                sum(p[0] for p in cluster_points) / len(cluster_points),
                sum(p[1] for p in cluster_points) / len(cluster_points)
            )
        else:
            new_centroids[label] = (0, 0)
    return new_centroids

# Given data points and initial cluster centers
data_points = [(2,3), (3,5), (5,3), (6,8), (8,8), (7,6), (9,5), (4,2), (2,8), (6,4)]
initial_clusters = [(3, 4), (7, 7), (8, 5)]  # Supports flexible cluster count

# Assign points to clusters
assignments = assign_clusters(data_points, initial_clusters)

# Print assignments
print("Point | Distances | Assigned Cluster")
for a in assignments:
    distances_str = " | ".join([f"{d[1]}: {d[0]:.2f}" for d in a[1]])
    print(f"{a[0]} | {distances_str} | {a[2]}")

# Compute new centroids
new_centroids = calculate_new_centroids(assignments, [f'C{i+1}' for i in range(len(initial_clusters))])
print("\nNew Cluster Centers:")
for label, center in new_centroids.items():
    print(f"{label}: {center}")
