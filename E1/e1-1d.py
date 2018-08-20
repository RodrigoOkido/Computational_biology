#Place the index of the changed letter will be stored.
qtdA = 0
qtdT = 0
qtdC = 0
qtdG = 0
qtdN = 0
diff_char = False

#Content of all chromosome
content = ""
#Open and read file.
with open("sequence.fasta") as file:
    next(file)
    for line in file:
        line = line.rstrip('\n')
        content+= line

check = list(content)
#Checks every single character of the subsequence and search what char are mutated
for i in range(0, len(check)):

    if check[i] == "C":
        qtdC = qtdC + 1
    elif check[i] == "A":
        qtdA = qtdA + 1
    elif check[i] == "G":
        qtdG = qtdG + 1
    elif check[i] == "T":
        qtdT = qtdT + 1
    elif check[i] == "N":
        qtdN = qtdN + 1
        diff_char = True

print "Quantidades: \n C - ", qtdC, "\n G - ", qtdG, "\n T - ", qtdT, "\n A - ", qtdA, "\nCaracter Diferente - SIM: \n N - ", qtdN
