from ChessPieces import ChessPiece, KING
from BoardSquare import Colors, White, Black

nw = ( -1, +1)
sw = ( -1, -1)
se = (+1,  -1)
ne = (+1,  +1)
n = ( 0, +1)
s = ( 0, -1)
w = (+1,  0)
e = (-1,  0)

def king_go(board, color, direction, x, y):
    dx, dy = direction
    while True:
        x += dx
        y += dy
        if not (0 <= x < 8 and 0 <= y < 8):
            break
        piece = board[y,x].ChessPiece
        if (piece is not None) and (piece.color is color):
            break
        yield x, y
		break
		
class King(ChessPiece):
    
    directions = n, s, e, w, nw, sw, ne, se
	
    def __init__(self,color):
        super(King, self).__init__(KING, color)
	
	def valid_moves(self, board, position, turn, turn_number):
		column, row = position
        x = column_names.index(column)
        y = row_names.index(row)
        for direction in directions:
            for x2, y2 in king_go(board, self.color, direction, x, y):
                file = column_names[x2]
                rank = row_names[y2]
                yield file + rank
		
    def is_valid_move(self, board,from_row,from_col,
                    to_row,to_col,turn,turn_number):
        if not (super(King,self).is_valid_move(board,from_row,from_col,
                                             to_row,to_col,turn,turn_number)):
            return False
        if abs(to_row-from_row) > 1 or abs(to_col-from_col) > 1:
            return False
        #Wasnt sure about translation of next line
        other_piece = board[to_row,to_col].ChessPiece
        if other_piece is None:
            return True
        if other_piece.color != self.color:
            return True
        return False        
    
        
    
