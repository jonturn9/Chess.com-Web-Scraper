def FENtoVect(FEN):
    lines = re.split(r"/|\s",FEN)
    Vector = np.zeros((64,11))
    for i in range(8):
        offset = 0
        for j in range(len(lines[i])):
            if lines[i][j] == "P":
                #array[i][j+offset][0] = 1
                array[i][j+offset][1] = 1
            elif lines[i][j] == "p":
                #array[i][j+offset][0] = -1
                array[i][j+offset][1] = -1
            elif lines[i][j] == "N":
                #array[i][j+offset][0] = 2
                array[i][j+offset][2] = 1
            elif lines[i][j] == "n":
                #array[i][j+offset][0] = -2
                array[i][j+offset][2] = -1
            elif lines[i][j] == "B":
                #array[i][j+offset][0] = 3
                array[i][j+offset][3] = 1
            elif lines[i][j] == "b":
                #array[i][j+offset][0] = -3
                array[i][j+offset][3] = -1
            elif lines[i][j] == "R":
                #array[i][j+offset][0] = 4
                array[i][j+offset][4] = 1
            elif lines[i][j] == "r":
                #array[i][j+offset][0] = -4
                array[i][j+offset][4] = -1
            elif lines[i][j] == "Q":
                #array[i][j+offset][0] = 5
                array[i][j+offset][5] = 1
            elif lines[i][j] == "q":
                #array[i][j+offset][0] = -5
                array[i][j+offset][5] = -1
            elif lines[i][j] == "K":
                #array[i][j+offset][0] = 6
                array[i][j+offset][6] = 1
            elif lines[i][j] == "k":
                #array[i][j+offset][0] = -6
                array[i][j+offset][6] = -1
            else:
                offset+=int(lines[i][j])-1
                
    special_row = lines[8:]
    if special_row[0]=="b":
        array[7,:,:]=1
    else:
        array[7,:,:] = 0
    
    if special_row[1]=="KQk":
        array[:,:,8]=1
    elif special_row[1]=="KQq":
        array[:,:,8]=2
    elif special_row[1]=="KQ":
        array[:,:,8]=3
    elif special_row[1]=="Kkq":
        array[:,:,8]=4
    elif special_row[1]=="Kk":
        array[:,:,8]=5
    elif special_row[1]=="Kq":
        array[:,:,8]=6
    elif special_row[1]=="K":
        array[:,:,8]=7
    elif special_row[1]=="Qkq":
        array[:,:,8]=8
    elif special_row[1]=="Qk":
        array[:,:,8]=9
    elif special_row[1]=="Qq":
        array[:,:,8]=10
    elif special_row[1]=="Q":
        array[:,:,8]=11
    elif special_row[1]=="kq":
        array[:,:,8]=12
    elif special_row[1]=="k":
        array[:,:,8]=13
    elif special_row[1]=="q":
        array[:,:,8]=14
    elif special_row[1]=="-":
        array[:,:,8]=15
   
    en_passant = 0
    if special_row[2] == "-":
        array[:,:,9] = en_passant
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
        array[:,:,9] = en_passant
    array[:,:,10] = special_row[3]
    #array[:,:,11]=special_row[4]
    array[:,:,0]=special_row[4]
    return(array)
