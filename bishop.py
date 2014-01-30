class Bishop(ChessPiece):
    def __init__(self,color):
        super(Bishop,self).__init__(self,Bishop,color)
    
    @overrides(IsValidMove)
    def override IsValidMove(board,fromRow,fromCol,toRow,toCol,turn,turnNumber):
