class Knight(ChessPiece):
    def __init__(self,color):
        super(Knight,self).__init__(self,Knight,color)
    
    @overrides(IsValidMove)
    def override IsValidMove(board,fromRow,fromCol,toRow,toCol,turn,turnNumber):
        
