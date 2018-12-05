## E10 EXERCISE ##

seq1 = "cctgatagacgctatctggctatccacgtacataggtcctctgtgcgaatctatgcgtttccaaccat"
seq2 = "agtactggtgtacatttgatacgtacgtacaccggcaacctgaaacaaacgctcagaaccagaagtgc"
seq3 = "aaaagtccgtgcaccctctttcttcgtggctctggccaacgagggctgatgtataagacgaaaatttt"
seq4 = "agcctccgatgtaagtcatagctgtaactattacctgccacccctattacatcttacgtacgtataca"
seq5 = "ctgttatacaacgcgtcatggcggggtatgcgttttggtcgtcgtacgctcgatcgttaacgtaggtc"


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



def consensus ( list_seq ):

    consensus = []
    score = 0
    total_dist = 0
    score_column = 0
    dist_column = 0

    for i in range(0,len(list_seq)):
        list_qtd = [0,0,0,0]
        for j in range(0, len(list_seq[i])):
            if list_seq[j][i] == "a"
                list_qtd[0] += 1
            else if list_seq[i][j] == "t":
                list_qtd[1] += 1
            else if list_seq[i][j] == "c"
                list_qtd[2] += 1
            else if list_seq[i][j] == "g"
                list_qtd[3] += 1

        l_idx = list_qtd.index(max(list_qtd))
        if l_idx == 0:
            consensus[i] = "a"
        else if l_idx == 1:
            consensus[i] = "t"
        else if l_idx == 2:
            consensus[i] = "c"
        else if l_idx == 3:
            consensus[i] = "g"

        score_column = max (a_qtd, t_qtd, c_qtd, g_qtd)
        dist_column = sum(list_qtd) - score_column
        score += score_column
        total_dist += dist_column
