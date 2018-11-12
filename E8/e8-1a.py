import random
import numpy as np

# Definition of centroids values.
centroids = []


# Function to calculate the euclidian distance.
# This is calculated taking the centroid value and the point which is
# being analyzed.
def euclidian_distance (x0, y0):
    return np.sqrt(np.sum((x0 - y0)**2))


# Function to generate centroids.
# Randomic initials values between -3 and 3.
def generate_centroids(k):
    gen_cent = []
    for i in range(k):
        gen_cent.append(random.randint(-3,3))
    return gen_cent


# Set the point to a cluster. Defined by the min calculated in Euclidian Distance.
def define_point_to_cluster(distance, data_point, centroids):
    min_index = min(distance, key=distance.get)
    return [min_index, data_point, centroids[min_index]]


# Function to modify the centroids.
def new_centroids(clusters, centroids):
    return np.array(clusters + centroids)/2


# Main function k-means.
def k_means(data, centroids, total_iteration):

    # Variable to store each point.
    label = []

    # List of list to store each cluster.
    clusters = [[] for i in range(len(centroids))]

    # The size of the total data (In this case is the CSV file).
    total_points = len(data)

    # The number of centroids correspond to the k value (clusters).
    k = len(centroids)

    # Starts the k-means (Each iteration (First Loop)).
    for iteration in range(0, total_iteration):
        # Checking values in the csv file (Second Loop).
        for index_point in range(0, total_points):
            distance = {}
            # Calculate the distance of each point between all centroids.
            for index_centroid in range(0, k):
                distance[index_centroid] = euclidian_distance(data[index_point][iteration], centroids[index_centroid])
            # Includes the point to the cluster which are most closest of one centroid.
            label = define_point_to_cluster(distance, data[index_point][iteration], centroids)
            # Insert the data point to the correct cluster.
            clusters[label[0]].append(label[1])
            # Update centroids.
            centroids[label[0]] = new_centroids(label[1], centroids[label[0]])

    # Return the clusters and the centroids.
    return [clusters, centroids]

# Main function.
if __name__ == "__main__":
    # Defining the K param for the k-means.
    K = 2
    # Opening and readning file.
    with open('leukemia_big.csv', 'rb') as filename:
        next(filename)
        data = np.genfromtxt(filename, delimiter=",")
        # [# DEBUG: ]print data
        # Defining the centroids.
        centroids = generate_centroids(K)
        # Defining the iterations. How many iterations the algorithm will keep
        # running.
        total_iteration = 5

        # Executes the k-means algorithm.
        [clusters, new_centroids] = k_means(data, centroids, total_iteration)
        # Return the clusters with the number of points in each one.
        for i in range(len(centroids)):
            print "Cluster ", i , ":", len(clusters[i])
