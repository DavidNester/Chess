class Pawn(ChessPiece):
    def __init__(self,color):
        super(Pawn,self).__init__(self,Pawn,color)
    
    @overrides(IsValidMove)
    def override IsValidMove(board,fromRow,fromCol,toRow,toCol,turn,turnNumber):
        if not (super(Pawn,self).IsValidMove(board,fromRow,fromCol,toRow,toCol,turn,turnNumber)):
            return False
        if turn == ChessColors.Black:
            if fromRow > toRow:
                return False
        if turn == ChessColors.White:
            if fromRow < toRow:
                return False
        if board[toRow,toCol].ChessPiece == None:
            if abs(fromRow - toRow) == 1 and fromCol == toCol:
                return True
            #en passant(complex move). might just delete it because I'm not sure it worked in original
            elif abs(fromRow - toRow) == 1 and abs(toCol - fromCol) == 1:
                if board[fromRow, toCol].ChessPiece.Name == ChessPieces.Pawn and board[fromRow, toCol].ChessPiece.PieceColor != turn and board[fromRow, toCol].ChessPiece.LastMove == turnNumber - 1:
                    return True
                else:
                    return False
            elif abs(fromRow - toRow) == 2 and toCol == fromCol:
                if board[fromRow,fromCol].ChessPiece.LastMove == 0:
                    return True
                else:
                    return False
            else:
                return False
        elif board[toRow, toCol].ChessPiece != None:
            if board[toRow, toCol].ChessPiece.PieceColor != turn and abs(fromRow - toRow) == 1 and Math.Abs(toCol-fromCol) == 1:
                return True
            else:
                return False
        return False
                
