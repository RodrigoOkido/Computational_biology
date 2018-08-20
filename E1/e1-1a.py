#Place the index of the changed letter will be stored.
changed_index = 0
#Mutated subsequence
wrong_sentence = "CAGGAGATCTTCGTGGCCAC"
#Storing the wrong_sentence in another var to manipulate
tentative = wrong_sentence
#Content of all chromosome
content = ""
#Open and read file.
with open("sequence.fasta") as file:
    next(file)
    for line in file:
        line = line.rstrip('\n')
        content+= line

#Checks every single character of the subsequence and search what char are mutated
for i in range(0, len(wrong_sentence)):
    tentative = list(wrong_sentence)
    if tentative[i] == "C":
        tentative[i] = "G"
        tentative = "".join(tentative)
        changed_index = content.find(tentative)
        if changed_index >= 0:
            print "Subsequence starts at index: ",changed_index, "\nMutation happened at index: ", changed_index+i, "\nChanged: G -> C"
            break
        else:
            tentative = wrong_sentence


    elif tentative[i] == "A":
        tentative[i] = "T"
        tentative = "".join(tentative)
        changed_index = content.find(tentative)
        if changed_index >= 0:
            print "Subsequence starts at index: ",changed_index, "\nMutation happened at index: ", changed_index+i, "\nChanged: T -> A"
            break
        else:
            tentative = wrong_sentence

    elif tentative[i] == "G":
        tentative[i] = "C"
        tentative = "".join(tentative)
        changed_index = content.find(tentative)
        if changed_index >= 0:
            print "Subsequence starts at index: ",changed_index, "\nMutation happened at index: ", changed_index+i, "\nChanged: C -> G"
            break
        else:
            tentative = wrong_sentence

    elif tentative[i] == "T":
        tentative[i] = "A"
        tentative = "".join(tentative)
        changed_index = content.find(tentative)
        if changed_index >= 0:
            print "Subsequence starts at index: ",changed_index, "\nMutation happened at index: ", changed_index+i, "\nChanged: A -> T"
            break
        else:
            tentative = wrong_sentence
