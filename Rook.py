class Rook(ChessPiece):
    def __init__(self,color):
        super(Rook,self).__init__(self,Rook,color)
    
    @overrides(IsValidMove)
    def override IsValidMove(board,fromRow,fromCol,toRow,toCol,turn,turnNumber):
