# Hash containing the distance between species.
dist_species = {}

# Executes the UPGMA Method.
def upgma_method(matrix, assoc_label):
    # Keep running until have no more element in matrix.
    while len(assoc_label) > 1:
        # Locate the coordinates with the lowest number in the matrix.
        x, y = find_lowest_distance(matrix, assoc_label)

        # Update matrix after finding the lowest distance (cluster).
        # After updating matrix, the labels are updated (joining the labels
        # with the lowest distance).
        update_matrix(matrix, assoc_label, x, y)


    # Return the final label
    return assoc_label[0]


# Locates the coordinates (i,j) with the lowest value (distance) in the matrix.
# The result (coordinates i,j) will be stored in x,y.
# (Step 1 of UPGMA)
def find_lowest_distance(matrix, labels):

    # Initialize with high number for initialization purpose.
    lowest_distance = 1000000000
    # Index coordinates.
    x = 0
    y = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < lowest_distance:
                lowest_distance = matrix[i][j]
                x, y = i, j

    # Calculate the distance between the two species with the lowest distance.
    calc_dist = labels[y] + " - " + labels[x]
    dist_species[calc_dist] = lowest_distance/2

    # Return coordinates.
    return x, y


# Update matrix after finding the lowest distance (cluster).
# (Step 2 of UPGMA)
def update_matrix(matrix, labels, a, b):

    row = []

    # Swap if the indices are not ordered.
    if b < a:
        a, b = b, a

    # Updating row (a, i), where i < a.
    for i in range(0, a):
        row.append((matrix[a][i] + matrix[b][i])/2)

    matrix[a] = row

    # Update entire column (i, a), where i > a.
    for i in range(a+1, b):
        matrix[i][a] = (matrix[i][a] + matrix[b][i])/2

    # Rest values from row i.
    for i in range(b+1, len(matrix)):
        matrix[i][a] = (matrix[i][a] + matrix[i][b])/2
        # Remove the column.
        del matrix[i][b]

    # Remove row.
    del matrix[b]

    # Joins label (cluster) and delete the redundancy after joining.
    # (Step 3 of UPGMA)
    labels[a] = "[" + labels[a] + " - " + labels[b] + "]"
    del labels[b]



def main():
    # Association of each element of the matrix.
    assoc_label = ["GOR", "ORANG", "HUM", "CHI", "GIB"]

    # Building the matrix. This will be an triangular matrix. The other half
    # is symmetric and the main diagonal is filled with zeros.
    upgma_matrix = [
        [],
        [0.1890],
        [0.1100, 0.1790],
        [0.1130, 0.1920, 0.09405],
        [0.2150, 0.2110, 0.2050, 0.2140]
        ]

    # Printing results after UPGMA Method.
    print upgma_method(upgma_matrix, assoc_label)
    print "\nDistance between especies:\n", dist_species

if __name__ == "__main__":
    main()
