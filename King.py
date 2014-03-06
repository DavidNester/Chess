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

column_names = 'abcdefgh'
row_names = '12345678'

def king_go(board, color, direction, x, y):
    dx, dy = direction
    while True:
        x += dx
        y += dy
        if not (0 <= x < 8 and 0 <= y < 8):
            break
        other_piece_color = board.color_at(x, y)
        if other_piece_color == color:
            break
        yield x, y
        break

class King(ChessPiece):
    
    
    directions = n, s, e, w, nw, sw, ne, se

    def __init__(self,color):
        super(King, self).__init__(KING, color)

    def valid_moves(self, board, position):
        column, row = position
        x = column_names.index(column)
        y = row_names.index(row)
        for direction in self.directions:
            for x2, y2 in king_go(board, self.color, direction, x, y):
                file = column_names[x2]
                rank = row_names[y2]
                yield file + rank  

