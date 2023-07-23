def PGNtoFEN(moves, setup="standard"):
    FEN = []
    if setup != "standard":
        board = chess.Board(fen=setup)
    else:
      board = chess.Board()
    for i in range(len(moves)):
        board.push_san(moves[i])
        FEN.append(board.fen())
    return(FEN)



