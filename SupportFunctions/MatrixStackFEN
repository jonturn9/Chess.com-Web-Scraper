def MatrixStackFEN(FEN, I_am_white=1):
    tmpList = []
    for i in range(len(FEN)):
        tmpList.append(FENtoMatrix(FEN[i], I_am_white))
    try:
        MatStack = np.stack(tmpList)
    except:
        MatStack=tmpList
    return(MatStack)

