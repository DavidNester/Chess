
n = ( 0, +1)
s = ( 0, -1)
w = (+1,  0)
e = (-1,  0)

column_names = 'abcdefgh'
row_names = '12345678'

def rook_moves(board, square, color):
    return set(valid_moves(board, square, color, [n, s, e, w]))

def valid_moves(board, square, color, directions):
    """Square looks like 'a5'."""
    column, row = square
    x = column_names.index(column)
    y = row_names.index(row)
    for direction in directions:
        for x2, y2 in go(board, color, direction, x, y):
            file = column_names[x2]
            rank = row_names[y2]
            yield file + rank

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
