def complement_checkpalindrome(subsequence):
    original = subsequence
    modified = list(subsequence)

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

    #print "ORIGINAL: ", original
    #print "MODIFICADA: ", modified
    #modified = str(modified)[::-1]
    #print "MODIFICADA INVERTIDA: ", modified

    if str(original) == str(modified)[::-1]:
        return True
    else:
        return False


def main():
    #Open and read file.
    content = ""
    palindrome = {}

    with open("sequence.fasta") as file:
        next(file)
        for line in file:
            line = line.rstrip('\n')
            content+= line

    j = 0
    for i in content:
        subseq = content[j:j+8]
        #print len(subseq)
        if "N" not in subseq and len(subseq) == 8:
            if complement_checkpalindrome(subseq) == True:
                val = palindrome.get(subseq)
                if val == None:
                    palindrome[subseq] = 1
                else:
                    val = val + 1
                    palindrome[subseq] = val

        j = j + 1

    print palindrome


if __name__ == "__main__":
    main()
