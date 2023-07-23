def stripPGN(PGN):
    #times = re.findall("{\[%clk .{0,1}\d:.\d:\d\d\]\}",PGN)
    moves=re.findall(r"\d+\.+ [BKNQR]?[a-h]?x?[a-h]x?\d\+?|\d+\.+ O-O\+?|\d+\.+ O-O-O\+?",PGN)
    moves_clean=[]    
    for i in range(len(moves)):
        moves_clean.append(re.sub("\d{1,4}\.{1,3} ","",moves[i]))
    return(moves_clean)

