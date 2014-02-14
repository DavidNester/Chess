from ChessPieces import ChessPiece, QUEEN
from BoardSquare import Colors, White, Black

class Queen(ChessPiece):
    
    
    def __init__(self,color):
        super(Queen,self).__init__(Queen,color)
    
    def is_valid_move(self,board,from_row,from_col,
                             to_row,to_col,turn,turn_number):
        if not (super(Bishop,self).is_valid_move(board,from_row,from_col,
                                               to_row,to_col,turn,turn_number)):
            return False
        if from_row != to_row and from_col != to_col and abs(from_row -         to_row) != abs(from_col - to_col):
            return False 
        if from_row == to_row:
            if abs(from_col - to_col) == 1:
                if board[to_row, to_col].ChessPiece == None:
                    return True
                elif board[to_row, to_col].ChessPiece.color != turn:
                    return True
                else:
                    return False
                # C#: for (int i = 1; i <= Math.Abs(to_col - from_col) - 1; i++)
            for i in range(1,abs(to_col-from_col)-1):
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
                elif board[to_row, to_col].ChessPiece.color != turn:
                    return True
                else:
                    return False
                # C#: for (int i = 1; i <= Math.Abs(to_row - from_row) - 1; i++)
            for i in range(1,abs(to_row - from_row) - 1):
                if from_row > to_row:
                    if board[from_row - i, from_col].ChessPiece != None:
                        return False
                if from_row < to_row:
                    if board[from_row + i, from_col].ChessPiece != None:
                        return False
            
            if board[to_row, to_col].ChessPiece == None:
                return True
            elif board[to_row, to_col].ChessPiece.color != turn:
                return True
            
        if abs(from_row - to_row) == abs(from_col - to_col):
            # C#: for (int i = 1; i < Math.Abs(from_row - to_row); i++)
            for i in range(1,abs(from_row - to_row)):
                if from_row > to_row and from_col > to_col:
                    if board[from_row - i, from_col - i].ChessPiece != None:
                        return False
                if from_row > to_row and from_col < to_col:
                    if board[from_row - i, from_col + i].ChessPiece != None:
                        return False
                if from_row < to_row and from_col < to_col:
                    if board[from_row + i, from_col + i].ChessPiece != None:
                        return False
                if from_row < to_row and from_col > to_col:
                    if board[from_row + i, from_col - i].ChessPiece != None:
                        return False

            if board[to_row, to_col].ChessPiece == None:
                return True
            elif board[to_row, to_col].ChessPiece.color != turn:
                return True
            else:
                return False
        else:
            return False
