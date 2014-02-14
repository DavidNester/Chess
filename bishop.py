from ChessPieces import ChessPiece, BISHOP
from BoardSquare import Colors, White, Black

class Bishop(ChessPiece):
	
	
    def __init__(self,color):
        super(Bishop,self).__init__(Bishop,color)
    
    def is_valid_move(self,board,from_row,
                             from_col,to_row,to_col,turn,turn_number):
        if not (super(Bishop,self).is_valid_move(board,from_row,from_col,
                                               to_row,to_col,turn,turn_number)):
            return False
        if to_col == from_col or to_row == from_row:
            return False
        if abs(from_row - to_row) != abs(from_col - to_col):
            return False
        if abs(from_row - to_row) == abs(from_col - to_col):
            # C#: for (int i = 1; i < Math.Abs(from_row-to_row); i++)
            for i in range(1, abs(from_row-to_row)):
                if from_row > to_row and from_col > to_col:
                    if board[from_row-i,from_col-i].ChessPiece != None:
                        return False
                elif from_row > to_row and from_col < to_col:
                    if board[from_row-i,from_col+i].ChessPiece != None:
                        return False
                elif from_row < to_row and from_col < to_col:
                    if board[from_row+i,from_col+i].ChessPiece != None:
                        return False
                elif from_row < to_row and from_col > to_col:
                    if board[from_row+i,from_col-i].ChessPiece != None:
                        return False
        if board[to_row, to_col].ChessPiece == None:
            return True
        elif board[to_row, to_col].ChessPiece.color != turn:
            return True
        else:
            return False
	
