
#Gorila, Orangotango, Humano, Chimpanze, Gibao
#GORILA = 0 , ORANGOTANGO = 1, HUMANO = 2, CHIMPANZE = 3, GIBAO = 4
upgma_matrix = [
[0.1890],
[0.1100, 0.1790],
[0.1130, 0.1920, 0.09405],
[0.2150, 0.2110, 0.2050, 0.2140]]

matrix_temp = 0
result = {}
list = []

#Executes the UPGMA Method
def upgma_method ():
    #Slowest value start with high number for initialization purpose
    slowest_value = 100000
    row = 0
    column = 0

    #Search for the lowest number comparison between species
    for i in range(len(upgma_matrix)):
        for j in range(len(upgma_matrix[i])):
            if upgma_matrix[i][j] < slowest_value and upgma_matrix[i][j] != 0:
                slowest_value = upgma_matrix[i][j]
                row = i
                column = j

    distance = slowest_value / 2
    cluster = "%d - %d" % (row , column)
    #Put the distance of the cluster on final result
    result[cluster] = distance
    print result
    #Values - GOR: Gorila , OR: Orangotango, H: Humano, CHI: Chimpanze, GI: Gibao
    for i in range(len(upgma_matrix[i])):
        if i != row and i != column:
            dist = (upgma_matrix[i][column]+upgma_matrix[i][row])/2
            list.append(dist);



    #Calculate the new distance matrix after clustering the slowest values



def main():
    upgma_method()


if __name__ == "__main__":
    main()
