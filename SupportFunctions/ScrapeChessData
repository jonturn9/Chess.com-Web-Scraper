def ScrapeChessData(username, start_year, end_year):
  Annual_Chess = []

  for i in range(start_year, end_year):
      for j in range(1, 13):
          Annual_Chess.append(ch.get_player_games_by_month_pgn(username, i, j))

  Chess_Text = []
  for i in range(len(Annual_Chess)):
      if Annual_Chess[i] != "":
          Chess_Text.append(Annual_Chess[i].text)

  Chess_Text_Split = []
  for i in range(len(Chess_Text)):
      Chess_Text_Split.append(Chess_Text[i].splitlines())

  Chess_Clean = Chess_Text_Split
      
  for i in range(len(Chess_Clean)):
      j = 0
      while j < len(Chess_Clean[i]):
          if Chess_Clean[i][j] == "":
              del Chess_Clean[i][j]
              j -= 2
          elif Chess_Clean[i][j] == "[Event \"Let\'s Play!\"]":
              del Chess_Clean[i][j]
              j -= 2
          elif Chess_Clean[i][j] == "[Site \"Chess.com\"]":
              del Chess_Clean[i][j]
              j -= 2
          elif Chess_Clean[i][j] == "[Round \"-\"]":
              del Chess_Clean[i][j]
              j -= 2
          elif "ECO" in Chess_Clean[i][j]:
              del Chess_Clean[i][j]
              j -= 2
          elif "UTC" in Chess_Clean[i][j]:
              del Chess_Clean[i][j]
              j -= 2
          elif "End" in Chess_Clean[i][j]:
              del Chess_Clean[i][j]
              j -= 2
          elif "CurrentPosition" in Chess_Clean[i][j]:
              del Chess_Clean[i][j]
              j -= 2
          elif "Link" in Chess_Clean[i][j]:
              del Chess_Clean[i][j]
              j -= 2
          elif "FEN" in Chess_Clean[i][j]:
              del Chess_Clean[i][j]
              j -= 2
          elif "Event" in Chess_Clean[i][j]:
              del Chess_Clean[i][j]
              j -= 2
          j += 1

  del Chess_Clean[0]
  return(Chess_Clean)

