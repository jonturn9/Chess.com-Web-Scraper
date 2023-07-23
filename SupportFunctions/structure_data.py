def structure_data(entries, target_player):
  target_wins = []
  target_color = []
  variant = []
  stripped_pgn=[]
  fen_list=[]
  matrix_list=[]
  for i in range(len(entries["Info"])):
      if  "[White \"" + target_player + """"]""" in entries["Info"][i]:
          target_color.append(True)
          if """[Result "1-0"]""" in entries["Info"][i]:
              target_wins.append(True)
          else:
              target_wins.append(False)
      else:
          target_color.append(False)
          if """[Result "0-1"]""" in entries["Info"][i]:
              target_wins.append(True)
          else:
              target_wins.append(False)
      
      if  "[Variant]" in  entries["Info"][i]:
          variant.append(True)
      else:
          variant.append(False)
      stripped_pgn.append(stripPGN(entries["PGN"][i]))

      if variant[i] == False:
          try:
              fen_list.append(PGNtoFEN(stripped_pgn[i]))
          except:
              fen_list.append("NA")
      else:
          fen_list.append("NA")

      if fen_list[i] != "NA":
          matrix_list.append(MatrixStackFEN(fen_list[i], target_color[i]))
      else:
          matrix_list.append("NA")
    
  entries["Target_Color"]=target_color
  entries["Target_Wins"]=target_wins
  entries["Variant Game"]=variant
  entries["Stripped PGN"]=stripped_pgn
  entries["FEN"]=fen_list
  entries["Matrix"] = matrix_list

  return(entries)
