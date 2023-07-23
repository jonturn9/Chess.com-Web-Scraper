def pull_chess_data(target_player, start_year, end_year):
    chess_raw = ScrapeChessData(target_player, start_year, end_year)
    entries = index_chess(chess_raw)
    ouptut = structure_data(entries, target_player)
    return(ouptut)
