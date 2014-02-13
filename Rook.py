from ChessPieces import ChessPiece, ROOK
from BoardSquare import Colors, White, Black

class Rook(ChessPiece):
    
    
    def __init__(self,color):
        super(Rook,self).__init__(Rook,color)
    
    def is_valid_move(self,board,from_row,from_col,
                      to_row,to_Col,turn,turn_number):
        if not (super(Bishop,self).is_valid_move(board,from_row,
                                                 from_col,to_row,to_Col,
												 turn,turn_number)):
            return False
        if from_row != to_row and from_col != to_Col:
                return False
            #horiz or vert?
        if from_row == to_row:
            if abs(from_col - to_Col) == 1:
                if board[to_row, to_Col].ChessPiece == None:
                    return True
                elif board[to_row, to_Col].ChessPiece.color != turn:
                    return True
                else:
                    return False

                    # C#: for (int i = 1; i <= Math.Abs(to_Col - from_col) - 1; i++)
                for i in range(i,abs(to_Col - from_col) - 1):
                    if from_col > to_Col:
                        if board[from_row, from_col - i].ChessPiece != None:
                            return False
                    if from_col < to_Col:
                        if board[from_row, from_col+i].ChessPiece != None:
                            return False
                
        if from_col == to_Col:
            if abs(from_row - to_row) == 1:
                if board[to_row, to_Col].ChessPiece == None:
                    return True
                elif board[to_row, to_Col].ChessPiece.color != turn:
                    return True
                else:
                    return False
                    # C#: for (int i = 1; i <= Math.Abs(to_row - from_row) - 1; i++)
            for i in range(1,abs(to_row - from_row) - 1):
                if from_row > to_row:
                    if board[from_row-i, from_col].ChessPiece != None:
                        return False
                if from_col < to_Col:
                    if board[from_row+i, from_col].ChessPiece != None:
                        return False
                                
            if board[to_row, to_Col].ChessPiece == None:
                return True
            elif board[to_row, to_Col].ChessPiece.color != turn:
                return True
            else:
                return False
