#enum(Knight,Pawn,Rook,Bishop,Queen,King)
KING = 'K'
QUEEN = 'Q'
ROOK = 'R'
BISHOP = 'B'
KNIGHT = 'N'
PAWN = 'P'
pieces = [KING, QUEEN, ROOK, BISHOP, KNIGHT, PAWN]

column_names = 'abcdefgh'
row_names = '12345678'

class ChessPiece(object):

    def __init__(self,type,color): 
        self.type = type
        self.color = color
        self.lastMove = 0

    def __repr__(self):
        return '<%s %s>' % (self.color, self.__class__.__name__)

    def valid_moves(self, board, position):
        """Position looks like 'a5'."""
        column, row = position
        x = column_names.index(column)
        y = row_names.index(row)
        directions = self.directions
        for direction in directions:
            for x2, y2 in go(board, self.color, direction, x, y):
                file = column_names[x2]
                rank = row_names[y2]
                yield file + rank

    def is_valid_move(self,board, from_row, from_col,
                      to_row, to_col, turn, turn_number):
        if not (in_range(from_row) and in_range(from_col)
                and in_range(to_row) and in_range(to_col)):
            return False
        elif from_row == to_row and from_col == to_col:
            return False
        elif board[from_row,from_col].ChessPiece.color != turn:
            return True
        else:
            return True


def go(board, color, direction, x, y):
    dx, dy = direction
    while True:
        x += dx
        y += dy
        if not (0 <= x < 8 and 0 <= y < 8):
            break
        piece = board[y,x].ChessPiece
        if (piece is not None) and (piece.color is color):
            break
        if (piece is not None) and (piece.color is not color):
           yield x, y
           break
        yield x, y


def in_range(value):
    if 0 <= value < 8:
        return True
    else:
        return False
