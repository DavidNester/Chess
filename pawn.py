from ChessPieces import ChessPiece, PAWN
from BoardSquare import Colors, White, Black

class Pawn(ChessPiece):
    
    
    def __init__(self,color):
        super(Pawn, self).__init__(PAWN, color)
    
    def is_valid_move(self,board,from_row,from_col,
                    to_row,to_col,turn,turn_number):
        if not (super(Pawn,self).is_valid_move(board,from_row,from_col,to_row,
                                             to_col,turn,turn_number)):
            return False
        if turn ==  Black:
            if from_row < to_row:
                return False
        if turn == White:
            if from_row > to_row:
                return False
        if board[to_row,to_col].ChessPiece is None:
            if abs(from_row - to_row) == 1 and from_col == to_col:
                return True
            #en passant(complex move). might just delete it because I'm not sure it worked in original
            #elif abs(from_row - to_row) == 1 and abs(to_col - from_col) == 1:
                    #   if board[from_row, to_col].ChessPiece.Name == #ChessPieces.Pawn
                    #and board[from_row, to_col].ChessPiece.PieceColor != turn
                    #   and board[from_row, to_col].ChessPiece.LastMove == turn_number - 1:
                    #return True
                    #else:
            #return False
            elif abs(from_row - to_row) == 2 and to_col == from_col:
                if turn == Black and board[5,to_col].ChessPiece != None:
                    return False
                elif turn == White and board[2,to_col].ChessPiece != None:
                    return False
                elif turn == Black and from_row == 6:
                    return True
                elif turn == White and from_row == 1:
                    return True
                else:
                    return False
            else:
                return False
        if board[to_row, to_col].ChessPiece is not None:
            if board[to_row, to_col].ChessPiece.color != self.color and abs(from_row - to_row) == abs(from_col - to_col) == 1:
                return True
            else:
                return False
        return False
                
