#Hash containing the distance between species
dist_species = {}
dist_calculated_nodes = {}

# Calculates for each specie the distance for all others species.
# Takes the lowest pair distance species and return their coordinates.
# (Step 1 and Step 2 are made in this function)
def calculate_distance(matrix, labels):
    # initialize with high number for initialization purpose
    lowest_pair_dist = 1000000000
    s_dist = []
    pair_distances = []

    # index coordinates
    x = 0
    y = 0

    # Built list adding all distances between species (Step 1)
    for i in range(len(matrix)):
        dist = 0
        for j in range(len(matrix[i])):
            if i != j:
                dist += matrix[j][i]

        s_dist.append(dist)


    # Take the species with the lowest distance (Step 2)
    for i in range(len(matrix)):
        dist = 0
        for j in range(len(matrix[i])):
            if i != j:
                dist = matrix[i][j] - s_dist[i] - s_dist[j]
                pair_distances.append(dist)
                if dist < lowest_pair_dist:
                    lowest_pair_dist = dist
                    x, y = i, j

    pair = "[" + labels[x] + " - " + labels[y] + "]"
    dist_species[pair] = lowest_pair_dist
    return x,y


def main():
    # Association of each element of the matrix.
    assoc_label = ["GOR", "ORANG", "HUM", "CHI", "GIB"]

    # Building the matrix. This will be an triangular matrix. The other half
    # is symmetric and the main diagonal is filled with zeros.
    nj_matrix = [
        [0, 0.1890, 0.1100, 0.1130, 0.2150],
        [0.1890, 0 , 0.1790, 0.1920, 0.2110],
        [0.1100, 0.1790, 0 , 0.09405, 0.2050],
        [0.1130, 0.1920, 0.09405, 0, 0.2140],
        [0.2150, 0.2110, 0.2050, 0.2140, 0]
        ]

    calculate_distance(nj_matrix, assoc_label)
    # Printing results after Neighbor Joining Method.
    # print neighbor_joining(upgma_matrix, assoc_label)
    # print "\nDistance between especies:\n", dist_species

if __name__ == "__main__":
    main()
