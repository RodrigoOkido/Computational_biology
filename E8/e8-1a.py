import random
import numpy as np

# Definition of clusters numbers (K param)
clusters = 0
# Definition of centroids values
centroids = []


# Function to calculate the euclidian distance.
# This is calculated taking the centroid value and the point which is
# being analyzed.
def euclidian_distance (x0, y0):
    return np.sqrt(np.sum((x0 - y0)**2))


# Function to generate centroids.
# Randomic initials values between -3 and 3
def generate_centroids(k):
    gen_cent = []
    for i in range(k):
        gen_cent.append(random.randint(-3,3))
    return gen_cent


# Set the point to a cluster. Defined by the min calculated in Euclidian Distance.
def define_point_to_cluster(distance, data_point, centroids):
    index_of_minimum = min(distance, key=distance.get)
    return [index_of_minimum, data_point, centroids[index_of_minimum]]


# Function to modify the centroids.
def new_centroids(cluster_label, centroids):
    return np.array(cluster_label + centroids)/2


# Main function k-means.
def k_means(data, centroids, total_iteration):
    label = []
    cluster_label = [[] for i in range(len(centroids))]

    total_points = len(data)
    k = len(centroids)
    for iteration in range(0, total_iteration):
        for index_point in range(0, total_points):
            distance = {}
            # Calculate the distance of each point between all centroids.
            for index_centroid in range(0, k):
                distance[index_centroid] = euclidian_distance(data[index_point][iteration], centroids[index_centroid])

            label = define_point_to_cluster(distance, data[index_point][iteration], centroids)
            cluster_label[label[0]].append(label[1])
            centroids[label[0]] = new_centroids(label[1], centroids[label[0]])

    return [cluster_label, centroids]


if __name__ == "__main__":
    with open('leukemia_big.csv', 'rb') as filename:
        next(filename)
        data = np.genfromtxt(filename, delimiter=",")
        # print data
        centroids = generate_centroids(3)
        total_iteration = 5

        [cluster_label, new_centroids] = k_means(data, centroids, total_iteration)

        for i in range(len(centroids)):
            print "Cluster ", i , ":", len(cluster_label[i])
