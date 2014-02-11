from ChessPieces import ChessPiece, KING
from BoardSquare import Colors, White, Black

class King(ChessPiece):
    
    
    def __init__(self,color):
        super(King, self).__init__(KING, color)
    
    def is_valid_move(self, board,from_row,from_col,
                    to_row,to_Col,turn,turn_number):
        if not (super(King,self).is_valid_move(board,from_row,from_col,
                                             to_row,to_Col,turn,turn_number)):
            return False
        if abs(to_row-from_row) > 1 or abs(to_Col-from_col) > 1:
            return False
        #Wasnt sure about translation of next line
        other_piece = board[to_row,to_Col].ChessPiece
        if other_piece is None:
            return True
        if other_piece.color != self.color:
            return True
        return False        
    
        
    
