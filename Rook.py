from ChessPieces import ChessPiece, ROOK
from BoardSquare import Colors, White, Black

class Rook(ChessPiece):
    
    
    def __init__(self,color):
        super(Rook,self).__init__(Rook,color)
    
    def is_valid_move(self,board,from_row,from_col,
                      to_row,to_col,turn,turn_number):
        if not (super(Rook,self).is_valid_move(board,from_row,
                                                 from_col,to_row,to_col,
												 turn,turn_number)):
            return False
        if from_row != to_row and from_col != to_col:
                return False
            #horiz or vert?
        if from_row == to_row:
            if abs(from_col - to_col) == 1:
                if board[to_row, to_col].ChessPiece == None:
                    return True
                if board[to_row, to_col].ChessPiece.color != turn:
                    return True
                else:
                    return False
            if abs(from_col - to_col) == 2:
                if from_col > to_col:
                    if board[from_row, from_col-1].ChessPiece != None:
                        return False
                if from_col < to_col:
                    if board[from_row, from_col+1].ChessPiece != None:
                        return False
        # C#: for (int i = 1; i <= Math.Abs(to_col - from_col) - 1; i++)
            else:
                for i in range(1,abs(to_col - from_col)):
                    if from_col > to_col:
                        if board[from_row, from_col - i].ChessPiece != None:
                            return False
                    if from_col < to_col:
                        if board[from_row, from_col + i].ChessPiece != None:
                            return False
        if from_col == to_col:
            if abs(from_row - to_row) == 1:
                if board[to_row, to_col].ChessPiece == None:
                    return True
                if board[to_row, to_col].ChessPiece.color != turn:
                    return True
                else:
                    return False
            if abs(from_row - to_row) == 2:
                if from_row > to_row:
                    if board[from_row-1, from_col].ChessPiece != None:
                        return False
                if from_row < to_row:
                    if board[from_row+1, from_col].ChessPiece != None:
                        return False
        # C#: for (int i = 1; i <= Math.Abs(to_row - from_row) - 1; i++)
            else:
                for i in range(1,abs(to_row - from_row)):
                    if from_row > to_row:
                        if board[from_row-i, from_col].ChessPiece != None:
                            return False
                    if from_row < to_row:
                        if board[from_row+i, from_col].ChessPiece != None:
                            return False
        if board[to_row, to_col].ChessPiece == None:
            return True
        elif board[to_row, to_col].ChessPiece.color != turn:
            return True
        else:
            return False
