from ChessPieces import ChessPiece, KNIGHT
from BoardSquare import Colors, White, Black

class Knight(ChessPiece):
    
    def __init__(self,color):
        super(Knight,self).__init__(Knight,color)
    
    def is_valid_move(self,board,from_row,from_col,
                             to_row,to_col,turn,turn_number):
        if not (super(Knight,self).is_valid_move(board,from_row,from_col,
                                               to_row,to_col,turn,turn_number)):
            return False
        if abs(to_row-from_row) > 2 or abs(to_col-from_col) > 2 or to_row == from_row or to_col == from_col:
            return False
        elif abs(to_row-from_row) == 2 and abs(to_col-from_col) == 1:
            #Unsure about translation
            if board[to_row,to_col].ChessPiece == None:
                return True
            elif board[to_row,to_col].ChessPiece.color != turn:
                return True
            else:
                return False
        elif abs(to_row-from_row) == 1 and abs(to_col-from_col) == 2:
            if board[to_row,to_col].ChessPiece == None:
                return True
            elif board[to_row,to_col].ChessPiece.color != turn:
                return True
            else:
                return False
        else:
            return False
