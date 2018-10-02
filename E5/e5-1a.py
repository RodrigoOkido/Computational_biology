# Hash containing the distance between species
dist_species = {}

# List containing the distance of the species from Ux (where x >= 0)
dist_calculated_nodes = []

# List containing all the calculations from step 1
# (Sx = (Sum all Dx) / (N - 2))
s_dist = []

# Counter of number of nodes generated until the final
node_counter = 0

# Calculates for each specie the distance for all others species.
# Takes the lowest pair distance species and return their coordinates.
# (Step 1 and Step 2 are made in this function)
def calculate_distance(matrix, labels):
    # initialize with high number for initialization purpose
    lowest_pair_dist = 1000000000
    pair_distances = []

    # index coordinates
    x = 0
    y = 0

    # Built list adding all distances between species (Step 1)
    for i in range(len(matrix)):
        dist = 0
        for j in range(len(labels)):
            if i != j:
                dist += matrix[j][i]

        result_specie = dist/(len(matrix[i]) - 2)
        s_dist.append(result_specie)

    # Take the species with the lowest distance (Step 2)
    for i in range(len(matrix)):
        dist = 0
        for j in range(len(labels)):
            if i != j:
                dist = matrix[i][j] - s_dist[i] - s_dist[j]
                pair_distances.append(dist)
                if dist < lowest_pair_dist:
                    lowest_pair_dist = dist
                    x, y = i, j


    pair = "[" + labels[x] + " - " + labels[y] + "]"
    dist_species[pair] = lowest_pair_dist

    return x,y



# Create a "Node" with the distance of the pair found on step 2
# (Step 3, 4 and 5)
def create_node_and_update_matrix (matrix, labels, x, y):
    global node_counter

    s_xU = matrix[x][y]/2 + ((s_dist[x] - s_dist[y])/2)
    s_yU = matrix[x][y]/2 + ((s_dist[y] - s_dist[x])/2)

    new_dist = 0

    # Update entire column (i, x), where i > x.
    for i in range(x+1, y):
        matrix[i][x] = (matrix[i][x] + matrix[y][i] - matrix[x-1][y])/2

    # Rest values from row i.
    for i in range(y+1, len(matrix)):
        matrix[i][x] = (matrix[i][x] + matrix[i][y])/2
        # Remove the column.
        del matrix[i][y]

    # Remove row.
    del matrix[y]


    labels[x] = "[U{0} : ".format(node_counter) + labels[x] + ": {0} || ".format(s_xU) + labels[y] + ": {0} ]".format(s_yU)
    node_counter = node_counter + 1
    dist_calculated_nodes.append(labels[x])
    del labels[y]


    del s_dist[:]


def neighbor_joining(matrix, assoc_label):
    # Keep running until have no more element in matrix.
    while len(assoc_label) > 1:
        # Locate the coordinates with the lowest number in the matrix.
        x, y = calculate_distance(matrix, assoc_label)

        # Update matrix after finding the lowest distance (cluster).
        # After updating matrix, the labels are updated (joining the labels
        # with the lowest distance).
        create_node_and_update_matrix(matrix, assoc_label, x, y)

    # Return the final label
    return assoc_label[0]



def main():
    # Association of each element of the matrix.
    assoc_label = ["GOR", "ORANG", "HUM", "CHI", "GIB"]
    species_count = len(assoc_label)
    # Building the matrix. This will be an triangular matrix. The other half
    # is symmetric and the main diagonal is filled with zeros.
    nj_matrix = [
        [0, 0.1890, 0.1100, 0.1130, 0.2150],
        [0.1890, 0, 0.1790, 0.1920, 0.2110],
        [0.1100, 0.1790, 0, 0.09405, 0.2050],
        [0.1130, 0.1920, 0.09405, 0, 0.2140],
        [0.2150, 0.2110, 0.2050, 0.2140, 0]
        ]

    ix, iy = calculate_distance(nj_matrix, assoc_label)
    create_node_and_update_matrix(nj_matrix, assoc_label, ix, iy)

    # Printing results after Neighbor Joining Method.
    print neighbor_joining(nj_matrix, assoc_label)
    print "\nDistance between especies:\n", dist_species

if __name__ == "__main__":
    main()
