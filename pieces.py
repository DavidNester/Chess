
n = ( 0, +1)
s = ( 0, -1)
w = (+1,  0)
e = (-1,  0)
nw = ( -1, +1)
sw = ( -1, -1)
se = (+1,  -1)
ne = (+1,  +1)

column_names = 'abcdefgh'
row_names = '12345678'

def queen_moves(board, square, color):
    return set(valid_moves(board, square, color, [n, s, e, w, ne, se, nw, sw]))

def rook_moves(board, square, color):
    return set(valid_moves(board, square, color, [n, s, e, w]))

def bishop_moves(board, square, color):
    return set(valid_moves(board, square, color, [ne, se, nw, sw]))

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
        other_piece_color = board.color_at(x, y)
        if other_piece_color is color:
            break
        yield x, y
        if other_piece_color is not None:
           break
