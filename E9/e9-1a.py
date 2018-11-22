import random
import numpy as np

# Definition of centroids values in a list.
centroids = []


# Function to calculate the euclidian distance.
# This is calculated taking the centroid value and the point which is
# being analyzed.
def euclidian_distance (x0, y0):
    return np.sqrt(np.sum((x0 - y0)**2))


# Function to generate centroids.
def generate_centroids(k, data):
    gen_cent = []
    for i in range(k):
        index = random.randint(1,71)
        cen = list(data[index])
        cen = cen[2:]
        gen_cent.append(np.mean(cen))
    return gen_cent


# Set the point to a cluster. Defined by the min calculated in Euclidian Distance.
def define_point_to_cluster(distance, data_point, centroids):
    min_index = min(distance, key=distance.get)
    return [min_index, data_point, centroids[min_index]]


# Function to modify the centroids.
def new_centroids(clusters, centroids):
    return np.array(clusters + centroids)/2


# Function to build independent new sets selecting 3572 genes from the data
# randomly. Is used to run k-means with subsets selected randomly inside
# the data.
# Need to pass per parameter the data and the number of sets wanted.
def build_random_groups(data, sets_number):

    # List to store the lists of new independent sets included in data.
    independent_sets = []

    for i in range (0, 100):
        list_i = random.sample(data, 3572)
        independent_sets.append(list_i)
        
    return independent_sets



# Main function k-means.
def k_means(data, centroids, total_iteration):

    # Variable to store each point.
    label = []

    # List of list to store each cluster.
    clusters = [[] for i in range(len(centroids))]

    #AML and ALL quantities:
    aml_c1 = 0
    all_c1 = 0
    aml_c2 = 0
    all_c2 = 0
    aml_c3 = 0
    all_c3 = 0

    # The size of the total data (In this case is the CSV file).
    total_points = len(data)

    # The number of centroids correspond to the k value (clusters).
    k = len(centroids)

    # Starts the k-means (Each iteration (First Loop)).
    for iteration in range(0, total_iteration):
        # Checking values in the csv file (Second Loop).
        for index_point in range(0, total_points):
            distance = {}
            mean_line = []
            line_label = ""
            # Calculate the distance of each point between all centroids and put
            # on the dict distance.
            mean_line = list(data[index_point])
            line_label = str(mean_line[0])
            mean_line = mean_line[2:]
            for index_centroid in range(0, k):
                distance[index_centroid] = euclidian_distance(np.mean(mean_line), centroids[index_centroid])
            # Includes the point to the cluster which are most closest of one centroid.
            label = define_point_to_cluster(distance, np.mean(mean_line), centroids)
            # DEBUG: print label
            # Insert the data point to the correct cluster.
            if label[1] not in clusters[label[0]]:
                clusters[label[0]].append(label[1])
                if label[0] == 0 and line_label == "ALL":
                    all_c1 += 1
                elif label[0] == 0 and line_label == "AML":
                    aml_c1 += 1
                elif label[0] == 1 and line_label == "ALL":
                    all_c2 += 1
                elif label[0] == 1 and line_label == "AML":
                    aml_c2 += 1
                elif label[0] == 2 and line_label == "ALL":
                    all_c3 += 1
                elif label[0] == 2 and line_label == "AML"::
                    aml_c3 += 1
                else:
                    continue
            # Update centroids.
            centroids[label[0]] = new_centroids(label[1], centroids[label[0]])

    # Return the clusters and the centroids.
    print "ALL / AML Cluster 1: ", all_c1, "/", aml_c1
    print "ALL / AML Cluster 2: ", all_c2, "/", aml_c2
    print "ALL / AML Cluster 3: ", all_c3, "/", aml_c3
    return [clusters, centroids]

# Main function.
if __name__ == "__main__":
    # Defining the K param for the k-means (Change K value between 2 and 3).
    K = 2

    # Opening and reading file.
    # Output.csv is the transpose data of the leukemia_big.csv
    with open('output.csv', 'rb') as filename:
        data = np.genfromtxt(filename, delimiter=",", dtype=None)

        # [# DEBUG: ]print data
        # Defining the centroids.
        centroids = generate_centroids(K, data)
        # DEBUG: print centroids
        # Defining the iterations. How many iterations the algorithm will keep
        # running.
        total_iteration = 5

        # Executes the k-means algorithm.
        [clusters, new_centroids] = k_means(data, centroids, total_iteration)
        # Return the clusters with the number of points in each one.
        for i in range(len(centroids)):
            print "Cluster ", i , ":", len(clusters[i])
