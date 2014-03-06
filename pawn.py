from ChessPieces import ChessPiece, PAWN
from BoardSquare import Colors, White, Black

nw = ( -1, +1)
sw = ( -1, -1)
se = (+1,  -1)
ne = (+1,  +1)
n = ( 0, +1)
s = ( 0, -1)

column_names = 'abcdefgh'
row_names = '12345678'

def pawn_go(board, color, direction, x, y):
    dx, dy = direction
    i = 0
    if color is White:
        if y == 1:
            start = True
        else:
            start = False
    else:
        if y == 6:
            start = True
        else:
            start = False  
    while True:
        i += 1
        x += dx
        y += dy
        if not (0 <= x < 8 and 0 <= y < 8):
            break
        piece = board[y,x].ChessPiece
        if direction == n or direction == s:
            if start:
                if (piece is not None):
                    break
                yield x, y
                if i == 2:
                    break
            else:
                if piece is not None:
                    break
                else:
                    yield x, y
                    break
        else:        
            if (piece is not None) and (piece.color is color):
                break
            if (piece is None):
                break
            yield x, y
            break

class Pawn(ChessPiece):
    
    def __init__(self,color):
        super(Pawn, self).__init__(PAWN, color)
        if self.color is White:
            self.directions = nw, n, ne
        if self.color is Black:
            self.directions = sw, s, se
    
    def valid_moves(self, board, position, turn, turn_number):
        column, row = position
        x = column_names.index(column)
        y = row_names.index(row)
        for direction in self.directions:
            for x2, y2 in pawn_go(board, self.color, direction, x, y):
                file = column_names[x2]
                rank = row_names[y2]
                yield file + rank
