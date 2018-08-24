def smith_waterman(seq1, seq2):
    #Score
    score = 0

    #Transform in list
    seq1_list = list(seq1) #column
    seq2_list = list(seq2) #lines

    #Take the size of each sequence
    size_seq1 = len(seq1) + 1
    size_seq2 = len(seq2) + 1

    if size_seq1 > 0 and size_seq2 > 0:

        #Inicialize filled of zeros
        smith_watertable = [0] * (size_seq2) #lines
        for i in range(size_seq2):
            smith_watertable[i] = [0] * (size_seq1) #columns


        biggest_value = -1
        x_index_biggest_number = -1
        y_index_biggest_number - -1
        #Loop to fill the rest with values
        for x in range(size_seq2):
            if x+1 == size_seq2:
                break
            for y in range(size_seq1):
                if y+1 == size_seq1:
                    break
                smith_watertable[x+1][y+1] = check_max(seq1_list, seq2_list, x, y, smith_watertable[x][y], smith_watertable[x][y+1], smith_watertable[x+1][y] )
                if smith_waterman[x+1][y+1] > biggest_value:
                    biggest_value = smith_waterman[x+1][y+1]
                    x_index_biggest_number = x+1
                    y_index_biggest_number = y+1


        #Calculate score and check identity
        score = smith_watertable[x_index_biggest_number][y_index_biggest_number]
        id1 = ""
        id2 = ""

        path1 = smith_watertable[x_index_biggest_number-1][y_index_biggest_number-1]
        path2 = smith_watertable[x_index_biggest_number][y_index_biggest_number-1]
        path3 = smith_watertable[x_index_biggest_number-1][y_index_biggest_number]

        #CALCULATE SCORE
        while path1 != 0 and path2 != 0 and path3 != 0:
            if x_index_biggest_number == 0 and y_index_biggest_number != 0:
                score = score + path2
                y_index_biggest_number = y_index_biggest_number - 1
                id2 += "-"
            elif x_index_biggest_number != 0 and y_index_biggest_number == 0:
                score = score + path3
                x_index_biggest_number = x_index_biggest_number - 1
                id1 += "-"
            elif path1 > path2 and path1 > path3:
                score = score + path1
                x_index_biggest_number = x_index_biggest_number -1
                y_index_biggest_number = y_index_biggest_number -1
                id1 += seq1_list[y_index_biggest_number]
                id2 += seq2_list[x_index_biggest_number]
            elif path2 > path1 and path2 > path3:
                score = score + path2
                x_index_biggest_number = x_index_biggest_number
                y_index_biggest_number = y_index_biggest_number -1
                id1 += seq1_list[x_index_biggest_number]
                id2 += "-"
            else:
                score = score + path3
                x_index_biggest_number = x_index_biggest_number -1
                y_index_biggest_number = y_index_biggest_number
                id1 += "-"
                id2 += seq2_list[y_index_biggest_number]

            path1 = smith_watertable[x_index_biggest_number-1][y_index_biggest_number-1]
            path2 = smith_watertable[x_index_biggest_number][y_index_biggest_number-1]
            path3 = smith_watertable[x_index_biggest_number-1][y_index_biggest_number]

        print smith_watertable
        print id1[::-1]
        print id2[::-1]
        global similarity_id
        similarity_id.append(check_identity(id1,id2))

        return score

    else:
        return None


#Return the max value between the 3 possibilities of the smith waterman table.
def check_max (sequence_list1, sequence_list2, x, y, pos_table, pos_table_x, pos_table_y):

    #Points
    match = 1
    mismatch = -1
    gap = -2

    if sequence_list1[y] == sequence_list2[x]:
        #print "IGUAL"
        return max(match + pos_table, gap + pos_table_x, gap + pos_table_y)
    else:
        #print "MISMATCH"
        return max(pos_table + mismatch, pos_table_x + gap, pos_table_y + gap)


#Return the identity between the 2 sequences
def check_identity(str_id1, str_id2):
    identity1 = list(str_id1)
    identity2 = list(str_id2)
    final_score = 0

    for i in range(len(identity1)):
        if identity1[i] == identity2[i]:
            final_score = final_score + 1
        elif identity1[i] != identity2[i]:
            final_score = final_score - 1
        elif identity1[i] == "-":
            final_score = final_score - 2
        else:
            final_score = final_score - 2

    return final_score



def main():
    #Open and read file.
    content1 = ""
    content2 = ""

    results = {}


    with open("human.txt") as file:
        next(file)
        for line in file:
            line = line.rstrip('\n')
            content1+= line

    with open("horse.txt") as file2:
        next(file2)
        for line1 in file2:
            line1 = line1.rstrip('\n')
            content2= line1



    cmp1 = smith_waterman(content1,content2)
    results["Human - Horse"] = cmp1

    #print results
    key_max = max(results.keys(), key=(lambda k: results[k]))
    print results[key_max]
    print max(similarity_id)

if __name__ == "__main__":
    main()
