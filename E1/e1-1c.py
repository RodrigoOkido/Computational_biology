def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches


def main():
    #Open and read file.
    content = ""
    list_subseqs = {}

    with open("sequence.fasta") as file:
        next(file)
        for line in file:
            line = line.rstrip('\n')
            content+= line

    j = 0
    for i in content:
        subseq = content[j:j+37]
        if "N" not in subseq and len(subseq) == 37:
            subseq_it = list(find_all(content,subseq))
            #print subseq_it
            val = list_subseqs.get(subseq)
            if val == None:
                list_subseqs[subseq] = len(subseq_it)
                print list_subseqs

        j = j + 1

    print list_subseqs


if __name__ == "__main__":
    main()
