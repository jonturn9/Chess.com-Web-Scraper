def get_headings(chess_clean):
    headings = set()
    for i in range(len(chess_clean)):
        for j in range(len(chess_clean[i])):
            if chess_clean[i][j][0] =="[":
                header = chess_clean[i][j].split(" ")
                headings.add(header[0][1:])
    return(headings)

