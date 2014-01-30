class King(ChessPiece):
    def __init__(self,color):
        super(King,self).__init__(self,King,color)
    
    @overrides(IsValidMove)
    def override IsValidMove(board,fromRow,fromCol,toRow,toCol,turn,turnNumber):
