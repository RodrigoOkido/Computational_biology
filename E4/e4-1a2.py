dist_specie = {}

#Executes the UPGMA Method
def upgma_method(matrix, assoc_label):
    # Keep running until have no more element in table
    while len(assoc_label) > 1:
        # Locate lowest cell in the table
        x, y = find_lowest_distance(matrix, assoc_label)

        # Update matrix after finding the lowest distance (cluster)
        update_matrix(matrix, x, y)

        # Update the label
        join_labels(assoc_label, x, y)

    # Return the final label
    return assoc_label[0]


# Locates the cell with the lowest distance in the matrix
def find_lowest_distance(matrix, labels):
    # initialize with high number for initialization purpose
    lowest_distance = 1000000000

    # index coordinates
    x = 0
    y = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < lowest_distance:
                lowest_distance = matrix[i][j]
                x, y = i, j


    calc_dist = labels[y] + " - " + labels[x]
    dist_specie[calc_dist] = lowest_distance/2

    # Return coordinates
    return x, y


# Update matrix after finding the lowest distance (cluster)
def update_matrix(matrix, a, b):
    # Swap if the indices are not ordered
    if b < a:
        a, b = b, a

    # For the lower index, reconstruct the entire row (A, i), where i < A
    row = []
    for i in range(0, a):
        row.append((matrix[a][i] + matrix[b][i])/2)
    matrix[a] = row

    # Then, reconstruct the entire column (i, A), where i > A
    for i in range(a+1, b):
        matrix[i][a] = (matrix[i][a]+matrix[b][i])/2


    # We get the rest of the values from row i
    for i in range(b+1, len(matrix)):
        matrix[i][a] = (matrix[i][a]+matrix[i][b])/2
        # Remove the column
        del matrix[i][b]

    # Remove row
    del matrix[b]


# Function to join two label (cluster)
def join_labels(labels, a, b):
    # Swap if the indices are not ordered
    if b < a:
        a, b = b, a

    # Join the labels in the first index
    labels[a] = "[" + labels[a] + " - " + labels[b] + "]"
    del labels[b]



def main():
    # Association of each element of the matrix.
    assoc_label = ["GOR", "ORANG", "HUM", "CHI", "GIB"]
    upgma_matrix = [
        [],
        [0.1890],
        [0.1100, 0.1790],
        [0.1130, 0.1920, 0.09405],
        [0.2150, 0.2110, 0.2050, 0.2140]
        ]

    print upgma_method(upgma_matrix, assoc_label)
    print "\nDistance between especies:\n", dist_specie

if __name__ == "__main__":
    main()
