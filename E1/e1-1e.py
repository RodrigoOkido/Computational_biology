def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

def generate_sequence(registry):
    sequence = list(registry)

    for i in range(0, len(sequence)):
        if sequence[i] == "0":
            sequence[i] = "A"
        elif sequence[i] == "1":
            sequence[i] = "T"
        elif sequence[i] == "2":
            sequence[i] = "G"
        elif sequence[i] == "3":
            sequence[i] = "C"
        elif sequence[i] == "4":
            sequence[i] = "C"
        elif sequence[i] == "5":
            sequence[i] = "G"
        elif sequence[i] == "6":
            sequence[i] = "T"
        elif sequence[i] == "7":
            sequence[i] = "A"
        elif sequence[i] == "8":
            sequence[i] = "A"
        elif sequence[i] == "9":
            sequence[i] = "C"
        else:
            print "Not a registry."
            return -1

    sequence = "".join(sequence)
    return sequence


def complement (sequence):
    modified = list(sequence)

    for i in range(0, len(modified)):
        if modified[i] == "A":
            modified[i] = "T"
        elif modified[i] == "T":
            modified[i] = "A"
        elif modified[i] == "G":
            modified[i] = "C"
        elif modified[i] == "C":
            modified[i] = "G"

    modified = "".join(modified)
    return modified


def mutate_reg_complement(sequence):
    mutated_list = []
    getSequence = list(sequence)

    if getSequence[4] == "A":
        getSequence[4] = "T"
        getSequence = "".join(getSequence)
        mutated_list.append (getSequence)
        getSequence = list(sequence)
        getSequence[4] = "C"
        getSequence = "".join(getSequence)
        mutated_list.append (getSequence)
        getSequence = list(sequence)
        getSequence[4] = "G"
        getSequence = "".join(getSequence)
        mutated_list.append (getSequence)
    elif getSequence[4] == "T":
        getSequence[4] = "A"
        getSequence = "".join(getSequence)
        mutated_list.append (getSequence)
        getSequence = list(sequence)
        getSequence[4] = "G"
        getSequence = "".join(getSequence)
        mutated_list.append (getSequence)
        getSequence = list(sequence)
        getSequence[4] = "C"
        getSequence = "".join(getSequence)
        mutated_list.append (getSequence)
    elif getSequence[4] == "C":
        getSequence[4] = "A"
        getSequence = "".join(getSequence)
        mutated_list.append (getSequence)
        getSequence = list(sequence)
        getSequence[4] = "G"
        getSequence = "".join(getSequence)
        mutated_list.append (getSequence)
        getSequence = list(sequence)
        getSequence[4] = "T"
        getSequence = "".join(getSequence)
        mutated_list.append (getSequence)
    elif getSequence[4] == "G":
        getSequence[4] = "A"
        getSequence = "".join(getSequence)
        mutated_list.append (getSequence)
        getSequence = list(sequence)
        getSequence[4] = "T"
        getSequence = "".join(getSequence)
        mutated_list.append (getSequence)
        getSequence = list(sequence)
        getSequence[4] = "C"
        getSequence = "".join(getSequence)
        mutated_list.append (getSequence)

    return mutated_list



def main():
    #Store the registry number
    registry = "00252745"
    print "MEU CARTAO: 00252745"
    #Generate sequence of the registry
    myRegistry_sequence = generate_sequence(registry)
    print myRegistry_sequence
    #Generate the complement of the sequence
    myRegistry_complement = complement(myRegistry_sequence)
    print myRegistry_complement
    #Generate 3 mutation on 5th position (list)
    myMutatedList = mutate_reg_complement(myRegistry_complement)
    print myMutatedList

    #Hash which stores the quantity of mutated ones in the Genome 7.
    counter_mutated = {}

    content = ""

    with open("sequence.fasta") as file:
        next(file)
        for line in file:
            line = line.rstrip('\n')
            content+= line

    for i in range(len(myMutatedList)):
        mutated = myMutatedList[i]
        subseq_counter = list(find_all(content,mutated))
        val = counter_mutated.get(mutated)
        if val == None:
            counter_mutated[mutated] = len(subseq_counter)

    print counter_mutated

if __name__ == "__main__":
    main()
