class Bishop(ChessPiece):
	
	
    def __init__(self,color):
        super(Bishop,self).__init__(self,Bishop,color)
    
    @overrides(IsValidMove)
    def override IsValidMove(board,fromRow,
                             fromCol,toRow,toCol,turn,turnNumber):
        if not (super(Bishop,self).IsValidMove(board,fromRow,fromCol,
                                               toRow,toCol,turn,turnNumber)):
            return False
        if toCol == fromCol or toRow == fromRow:
                return False
        if abs(fromRow - toRow) == abs(fromCol - toCol):
            # C#: for (int i = 1; i < Math.Abs(fromRow-toRow); i++)
            for i in range(1, abs(fromRow-toRow)):
	        if fromRow > toRow and fromCol > toCol:
                    if board[fromRow-i,fromCol-i].ChessPiece != None:
		        return False
	        elif fromRow > toRow and fromCol < toCol:
	            if (board[fromRow-i,fromCol+i].ChessPiece != None:
			return False
		elif fromRow<toRow and fromCol<toCol:
	            if board[fromRow+i,fromCol+i].ChessPiece != None:
			return False    
	        elif fromRow < toRow and fromCol > toCol:
		    if board[fromRow+i,fromCol-i].ChessPiece != None:
			return False
	    if board[toRow, toCol].ChessPiece == None:
                return True
            elif board[toRow, toCol].ChessPiece.PieceColor != turn:
                return True
            else:
                return False
	else:
            return False
