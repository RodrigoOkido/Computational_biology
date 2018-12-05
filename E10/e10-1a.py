## E10 EXERCISE ##

# Function to check the difference between two sequences.
# The "max-diff" parameter is the max limit of the number of
# mutation allowed in one sequence. If max_diff = 3, and
# comparing seq1 and seq2 we obtain 3 or lower characters different,
# we accept the result.
def check_diff (seq1, seq2, max_diff):

    if len(seq1) == len(seq2):

        l_seq1 = list(seq1)
        l_seq2 = list(seq2)
        max_acceptable = max_diff
        checker = 0

        for i in range(0, len(l_seq1)):
            if l_seq1[i] != l_seq2[i]:
                checker += 1

        if checker <= max_acceptable:
            return 1
        else:
            return -1

    else:
        return -1


# Function to give the consensus of all list of sequences obtained.
# The sequence list received will be compared and the result will
# return for the user.
def consensus ( list_seq ):

    consensus = []
    score = 0
    total_dist = 0


    for i in range(0,len(list_seq[0])):
        list_qtd = [0,0,0,0]
        score_column = 0
        dist_column = 0

        for j in range(0, len(list_seq)):
            print list_seq[j][i]
            if list_seq[j][i] == "a":
                list_qtd[0] += 1
            elif list_seq[j][i] == "t":
                list_qtd[1] += 1
            elif list_seq[j][i] == "c":
                list_qtd[2] += 1
            elif list_seq[j][i] == "g":
                list_qtd[3] += 1

        l_idx = list_qtd.index(max(list_qtd))
        if l_idx == 0:
            consensus.append("a")
        elif l_idx == 1:
            consensus.append("t")
        elif l_idx == 2:
            consensus.append("c")
        elif l_idx == 3:
            consensus.append("g")

        score_column = max (list_qtd)
        dist_column = sum(list_qtd) - score_column
        score += score_column
        total_dist += dist_column

    return consensus, score


# Function to find in all list of sequences the ocurrence of "str1".
# Use the check_diff function to check for any mutation in the string
# and returns 1 if the difference is inside the interval defined by
# max_mut (max mutations).
def find_seq (str1, list_seqs, max_mut, str_len):

    tmp_output = [str1]

    for j in range(0,len(list_seqs)):
        str_l = list_seqs[j]
        for k in range (0, len(str_l)):
            cmp2 = str_l[k:k+str_len]
            if check_diff(str1,cmp2,max_mut) == 1:
                tmp_output.append(cmp2)
                break


    if len(tmp_output) != 5:
        del tmp_output[:]
        return -1

    return tmp_output


# Main function.
if __name__ == "__main__":

    cmp = ""
    seq1 = "cctgatagacgctatctggctatccacgtacataggtcctctgtgcgaatctatgcgtttccaaccat"
    seq2 = "agtactggtgtacatttgatacgtacgtacaccggcaacctgaaacaaacgctcagaaccagaagtgc"
    seq3 = "aaaagtccgtgcaccctctttcttcgtggctctggccaacgagggctgatgtataagacgaaaatttt"
    seq4 = "agcctccgatgtaagtcatagctgtaactattacctgccacccctattacatcttacgtacgtataca"
    seq5 = "ctgttatacaacgcgtcatggcggggtatgcgttttggtcgtcgtacgctcgatcgttaacgtaggtc"

    final_output = []
    best_score = []
    all_subseqs = []
    list_seqs = [seq2,seq3,seq4,seq5]

    for i in range(0, len(seq1)):
        cmp = seq1[i:i+3]
        final_output = find_seq(cmp, list_seqs, 1, 3)
        if final_output != -1:
            cns, scr = consensus(final_output)
            all_subseqs.append(cns)
            best_score.append(scr)


    bs = best_score.index(max(best_score))
    fr = all_subseqs[bs]
    print "Final Result: ", fr, "\nScore: ", best_score[bs]
