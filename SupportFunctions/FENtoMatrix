def FENtoMatrix(FEN,I_am_white=1):
    lines = re.split(r"/|\s",FEN)
    matrix = np.zeros((9,8))
    for i in range(8):
        offset = 0
        for j in range(len(lines[i])):
            if lines[i][j] == "P":
                matrix[i][j+offset] = 1
            elif lines[i][j] == "p":
                matrix[i][j+offset] = -1
            elif lines[i][j] == "N":
                matrix[i][j+offset] = 2
            elif lines[i][j] == "n":
                matrix[i][j+offset] = -2
            elif lines[i][j] == "B":
                matrix[i][j+offset] = 3
            elif lines[i][j] == "b":
                matrix[i][j+offset] = -3
            elif lines[i][j] == "R":
                matrix[i][j+offset] = 4
            elif lines[i][j] == "r":
                matrix[i][j+offset] = -4
            elif lines[i][j] == "Q":
                matrix[i][j+offset] = 5
            elif lines[i][j] == "q":
                matrix[i][j+offset] = -5
            elif lines[i][j] == "K":
                matrix[i][j+offset] = 6
            elif lines[i][j] == "k":
                matrix[i][j+offset] = -6
            else:
                offset+=int(lines[i][j])-1
                
    special_row = lines[8:]
    if special_row[0]=="b":
        matrix[8,1]=1
    else:
        matrix[8,1]=0
    
    if special_row[1]=="KQk":
         matrix[8,2]=1
    elif special_row[1]=="KQq":
        matrix[8,2]=2
    elif special_row[1]=="KQ":
        matrix[8,2]=3
    elif special_row[1]=="Kkq":
        matrix[8,2]=4
    elif special_row[1]=="Kk":
        matrix[8,2]=5
    elif special_row[1]=="Kq":
        matrix[8,2]=6
    elif special_row[1]=="K":
        matrix[8,2]=7
    elif special_row[1]=="Qkq":
        matrix[8,2]=8
    elif special_row[1]=="Qk":
        matrix[8,2]=9
    elif special_row[1]=="Qq":
        matrix[8,2]=10
    elif special_row[1]=="Q":
        matrix[8,2]=11
    elif special_row[1]=="kq":
        matrix[8,2]=12
    elif special_row[1]=="k":
        matrix[8,2]=13
    elif special_row[1]=="q":
        matrix[8,2]=14
    elif special_row[1]=="-":
        matrix[8,2]=15
   
    en_passant = 0
    if special_row[2] == "-":
        matrix[8,3]=  en_passant
    else: 
        if special_row[2][0] == "b":
            en_passant +=10
        elif special_row[2][0] == "c":
             en_passant +=20
        elif special_row[2][0] == "d":
             en_passant +=30
        elif special_row[2][0] == "e":
             en_passant +=40
        elif special_row[2][0] == "e":
             en_passant +=50
        elif special_row[2][0] == "f":
             en_passant +=60
        elif special_row[2][0] == "g":
             en_passant +=70
        elif special_row[2][0] == "h":
             en_passant +=80
        
        en_passant+= int(special_row[2][1])-1
        matrix[8,3]= en_passant
    matrix[8,4]= special_row[3]
    matrix[8,5]=special_row[4]
    matrix[8,6]= I_am_white
    return(matrix)

