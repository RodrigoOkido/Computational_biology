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
    # Initialize with high number for initialization purpose.
    lowest_pair_dist = 1000000000

    # Index coordinates
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

    # Take the pair of species with the lowest distance (Step 2)
    # If equals distances found, the first is chosen
    for i in range(len(matrix)):
        dist = 0
        for j in range(len(labels)):
            if i != j:
                dist = matrix[i][j] - s_dist[i] - s_dist[j]
                if dist < lowest_pair_dist:
                    lowest_pair_dist = dist
                    x, y = i, j


    pair = "[" + labels[x] + " - " + labels[y] + "]"
    dist_species[pair] = lowest_pair_dist

    return x,y



# Create a "Node" with the distance of the pair found on step 2 and update the
# matrix with the new distances. The labels are updated in the final and s_dist
# values calculated before are erased for next iteration (if necessary).
# (Step 3, 4 and 5)
def create_node_and_update_matrix (matrix, labels, x, y):
    global node_counter

    # Calculate the distance of the especie to the node U. (Step 3)
    s_xU = matrix[x][y]/2 + ((s_dist[x] - s_dist[y])/2)
    s_yU = matrix[x][y]/2 + ((s_dist[y] - s_dist[x])/2)

    # (Steps 4 and 5)
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

    # Update label.
    labels[x] = "[U{0} : ".format(node_counter) + labels[x] + ": {0} || ".format(s_xU) + labels[y] + ": {0} ]".format(s_yU)
    # Increment the node counter.
    node_counter = node_counter + 1
    # Add this node to an list of calculated nodes.
    dist_calculated_nodes.append(labels[x])
    # Delete one of the species (due to joining)
    del labels[y]

    # Erase the list of s_dist for calculations again in the next iteration.
    del s_dist[:]


# Executes the algorith Neighbor Joining
def neighbor_joining(matrix, assoc_label):
    # Keep running until have no more element in matrix.
    while len(assoc_label) > 1:
        # Locate the coordinates with the lowest number in the matrix.
        x, y = calculate_distance(matrix, assoc_label)

        # Creates a node of the chosen species and update the distance nj_matrix
        # table. Deletes one label after joining two species.
        create_node_and_update_matrix(matrix, assoc_label, x, y)

    # Return the final label
    return assoc_label[0]



def main():
    # Association of each element of the matrix.
    assoc_label = ["GOR", "ORANG", "HUM", "CHI", "GIB"]

    # Building the matrix.
    nj_matrix = [
        [0, 0.1890, 0.1100, 0.1130, 0.2150],
        [0.1890, 0, 0.1790, 0.1920, 0.2110],
        [0.1100, 0.1790, 0, 0.09405, 0.2050],
        [0.1130, 0.1920, 0.09405, 0, 0.2140],
        [0.2150, 0.2110, 0.2050, 0.2140, 0]
        ]


    # Printing results after Neighbor Joining Method.
    print neighbor_joining(nj_matrix, assoc_label)
    print "\nDistance between especies:\n", dist_species

if __name__ == "__main__":
    main()
