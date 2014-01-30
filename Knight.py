class Knight(ChessPiece):
    def __init__(self,color):
        super(Knight,self).__init__(self,Knight,color)
    
    @overrides(IsValidMove)
    def override IsValidMove(board,fromRow,fromCol,toRow,toCol,turn,turnNumber):
        if not (super(Knight,self).IsValidMove(board,fromRow,fromCol,toRow,toCol,turn,turnNumber)):
            return False
        if abs(toRow-fromRow) > 2 or abs(toCol-fromRow) > 2 or toRow == fromRow or toCol == fromCol:
            return False
        elif abs(toRow-fromRow) == 2 and abs(toCol-fromCol) == 1:
            #Unsure about translation
            if board[toRow,toCol].ChessPiece == None:
                return True
            elif board[toRow,toCol].ChessPiece.PieceColor != turn:
                return True
            else:
                return False
        elif abs(toRow-fromRow) == 1 and abs(toCol-fromCol) == 2:
            if board[toRow,toCol].ChessPiece == None:
                return True
            elif board[toRow,toCol].ChessPiece.PieceColor != turn:
                return True
            else:
                return False
        else:
            return False
        
        
