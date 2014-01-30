class Pawn(ChessPiece):
    def __init__(self,color):
        super(Queen,self).__init__(self,Queen,color)
    
    @overrides(IsValidMove)
    def override IsValidMove(board,fromRow,fromCol,toRow,toCol,turn,turnNumber):
