class Pawn(ChessPiece):
    def __init__(self,color):
        super(Pawn,self).__init__(self,Pawn,color)
    
    @overrides(IsValidMove)
    def override IsValidMove(board,fromRow,fromCol,toRow,toCol,turn,turnNumber):
