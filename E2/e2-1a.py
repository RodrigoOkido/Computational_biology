def needleman_wunsch(seq1, seq2):

    #Score
    score = 0

    #Transform in list
    seq1_list = list(seq1)
    seq2_list = list(seq2)

    #Take the size of each sequence
    size_seq1 = len(seq1) + 1
    size_seq2 = len(seq2) + 1

    if size_seq1 > 0 and size_seq2 > 0:

        #Inicialize filled of zeros
        needle_table = [0] * (size_seq2) #lines
        for i in range(size_seq2):
            needle_table[i] = [0] * (size_seq1) #columns

        #Inicialize the gap in column
        gap_seq1 = 0
        for i in range(size_seq1):
            if i == 0:
                continue
            else:
                gap_seq1 = gap_seq1 - 4
                needle_table[0][i] = gap_seq1

        #Inicialize the gap in line
        gap_seq2 = 0
        for j in range(size_seq2):
            if j == 0:
                continue
            else:
                gap_seq2 = gap_seq2 - 4
                needle_table[j][0] = gap_seq2

        #Loop to fill the rest with values
        for x in range(size_seq2):
            if x+1 == size_seq2:
                break
            for y in range(size_seq1):
                if y+1 == size_seq1:
                    break
                needle_table[x+1][y+1] = check_max(seq1_list, seq2_list, x, y, needle_table[x][y], needle_table[x][y+1], needle_table[x+1][y] )


        #Calculate score
        x_calc = size_seq2-1
        y_calc = size_seq1-1
        while x_calc != 0 and y_calc != 0:
            path1 = needle_table[x_calc-1][y_calc-1]
            path2 = needle_table[x_calc][y_calc-1]
            path3 = needle_table[x_calc-1][y_calc]
            if x_calc == 0 and y_calc != 0:
                score = score + path2
                y_calc = y_calc - 1
            elif x_calc != 0 and y_calc == 0:
                score = score + path3
                x_calc = x_calc - 1
            elif path1 > path2 and path1 > path3:
                score = score + path1
                x_calc = x_calc -1
                y_calc = y_calc -1
            elif path2 > path1 and path2 > path3:
                score = score + path2
                x_calc = x_calc
                y_calc = y_calc -1
            else:
                score = score + path3
                x_calc = x_calc -1
                y_calc = y_calc

        return score
        print needle_table

    else:
        return None


def check_max (sequence_list1, sequence_list2, x, y, pos_table, pos_table_x, pos_table_y):

    #Points
    match = 5
    mismatch = -3
    gap = -4

    if sequence_list1[y] == sequence_list2[x]:
        #print "IGUAL"
        return max(match + pos_table, match + pos_table_x, match + pos_table_y)
    elif sequence_list1[y] in sequence_list2:
        #print "GAP"
        return max(pos_table + gap, pos_table_x + gap, pos_table_y + gap)
    else:
        #print "MISMATCH"
        return max(pos_table + mismatch, pos_table_x + mismatch, pos_table_y + mismatch)

def main():
    #Open and read file.
    content1 = ""
    content2 = ""
    content3 = ""
    content4 = ""
    content5 = ""
    content6 = ""
    content7 = ""
    content8 = ""

    results = {}


    with open("human.txt") as file:
        next(file)
        next(file)
        for line in file:
            line = line.rstrip('\n')
            content1+= line

    with open("horse.txt") as file2:
        next(file2)
        next(file2)
        for line1 in file2:
            line1 = line1.rstrip('\n')
            content2= line1

    with open("chicken.txt") as file3:
        next(file3)
        next(file3)
        for line2 in file3:
            line2 = line2.rstrip('\n')
            content3= line2

    with open("cow.txt") as file4:
        next(file4)
        next(file4)
        for line3 in file4:
            line3 = line3.rstrip('\n')
            content4= line3

    with open("deer.txt") as file5:
        next(file5)
        next(file5)
        for line4 in file5:
            line4 = line4.rstrip('\n')
            content5= line4

    with open("pig.txt") as file6:
        next(file6)
        next(file6)
        for line5 in file6:
            line5 = line5.rstrip('\n')
            content6= line5

    with open("trout.txt") as file7:
        next(file7)
        next(file7)
        for line6 in file7:
            line6 = line6.rstrip('\n')
            content7= line6

    with open("wolf.txt") as file8:
        next(file8)
        next(file8)
        for line7 in file8:
            line7 = line7.rstrip('\n')
            content8= line7


    cmp1 = needleman_wunsch(content1,content2) #human - horse
    cmp2 = needleman_wunsch(content1,content3) #human - chicken
    cmp3 = needleman_wunsch(content1,content4) #human - cow
    cmp4 = needleman_wunsch(content1,content5) #human - deer
    cmp5 = needleman_wunsch(content1,content6) #human - pig
    cmp6 = needleman_wunsch(content1,content7) #human - trout
    cmp7 = needleman_wunsch(content1,content8) #human - wolf
    results["Human - Horse"] = cmp1
    results["Human - Chicken"] = cmp2
    results["Human - Cow"] = cmp3
    results["Human - Deer"] = cmp4
    results["Human - Pig"] = cmp5
    results["Human - Trout"] = cmp6
    results["Human - Wolf"] = cmp7

    print results
    key_max = max(results.keys(), key=(lambda k: results[k]))
    print results[key_max]

if __name__ == "__main__":
    main()
