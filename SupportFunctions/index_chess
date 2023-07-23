def index_chess(chess_clean):
  headings = get_headings(chess_clean)
  info_list = []
  pgn_list = []
  tmpList = []

  for i  in range(len(chess_clean)):
    for j in range(len(chess_clean[i])):
        if chess_clean[i][j].split(" ")[0][1:] in headings:
            tmpList.append(chess_clean[i][j])
        else:
          info_list.append(tmpList)
          tmpList = []
          pgn_list.append(chess_clean[i][j])

  entries = pd.DataFrame({"Info":info_list, "PGN": pgn_list})
  return(entries)

