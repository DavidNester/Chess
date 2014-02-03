class King(ChessPiece):
    
    
    def __init__(self,color):
        super(King,self).__init__(self,King,color)
    
    @overrides(IsValidMove)
    def override IsValidMove(board,fromRow,fromCol,
                             toRow,toCol,turn,turnNumber):
        if not (super(King,self).IsValidMove(board,fromRow,fromCol,
                                             toRow,toCol,turn,turnNumber)):
            return False
        if abs(toRow-fromRow) > 1 or abs(toCol-fromRow) > 1:
            return False
        #Wasnt sure about translation of next line
        elif board[toRow,toCol].ChessPiece == None:
            return True
        elif board[toRow,toCol].ChessPiece.PieceColor != turn:
            return True
        return False        
    
        
    
