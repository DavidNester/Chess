from ChessPieces import ChessPiece, PAWN
from BoardSquare import Colors, White, Black

class Pawn(ChessPiece):
    
    
    def __init__(self,color):
        super(Pawn, self).__init__(PAWN, color)
    
    def IsValidMove(self,board,fromRow,fromCol,
                    toRow,toCol,turn,turnNumber):
        if not (super(Pawn,self).IsValidMove(board,fromRow,fromCol,toRow,
                                             toCol,turn,turnNumber)):
            return False
        if turn ==  Black:
            if fromRow < toRow:
                return False
        if turn == White:
            if fromRow > toRow:
                return False
        if board[toRow,toCol].ChessPiece is None:
            if abs(fromRow - toRow) == 1 and fromCol == toCol:
                return True
            #en passant(complex move). might just delete it because I'm not sure it worked in original
            #elif abs(fromRow - toRow) == 1 and abs(toCol - fromCol) == 1:
                    #   if board[fromRow, toCol].ChessPiece.Name == #ChessPieces.Pawn
                    #and board[fromRow, toCol].ChessPiece.PieceColor != turn
                    #   and board[fromRow, toCol].ChessPiece.LastMove == turnNumber - 1:
                    #return True
                    #else:
            #return False
            elif abs(fromRow - toRow) == 2 and toCol == fromCol:
                if turn == Black and fromRow == 6:
                    return True
                elif turn == White and fromRow == 1:
                    return True
                else:
                    return False
            else:
                return False
        if board[toRow, toCol].ChessPiece is not None:
            if board[toRow, toCol].ChessPiece.color != self.color and abs(fromRow - toRow) == abs(fromCol - toCol) == 1:
                return True
            else:
                return False
        return False
                
