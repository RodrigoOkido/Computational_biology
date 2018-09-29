
#Gorila, Orangotango, Humano, Chimpanze, Gibao
upgma_matrix = [[0, 0.1890, 0.1100, 0.1130, 0.2150],
[0.1890, 0, 0.1790, 0.1920, 0.2110],
[0.1100, 0.1790, 0, 0.0940, 0.2050],
[0.1130, 0.1920, 0.09405, 0, 0.2140],
[0.2150, 0.2110, 0.2050, 0.2140, 0]]


#Executes the UPGMA Method
def upgma_method ():
    #Slowest value start with high number for initialization purpose
    slowest_value = 100000

    #Search for the lowest number comparison between species
    for i in range(len(upgma_matrix)):
        for j in range(len(upgma_matrix[i])):
            if upgma_matrix[i][j] < slowest_value and upgma_matrix[i][j] != 0:
                slowest_value = upgma_matrix[i][j]
    print slowest_value



def main():
    upgma_method()


if __name__ == "__main__":
    main()
