from ChessPieces import ChessPiece, KING

class King(ChessPiece):
    
    
    def __init__(self,color):
        super(King, self).__init__(KING, color)
    
    def IsValidMove(self, board,fromRow,fromCol,
                    toRow,toCol,turn,turnNumber):
        if not (super(King,self).IsValidMove(board,fromRow,fromCol,
                                             toRow,toCol,turn,turnNumber)):
            return False
        if abs(toRow-fromRow) > 1 or abs(toCol-fromCol) > 1:
            return False
        #Wasnt sure about translation of next line
        other_piece = board[toRow,toCol].ChessPiece
        if other_piece is None:
            return True
        if other_piece.color != self.color:
            return True
        return False        
    
        
    
