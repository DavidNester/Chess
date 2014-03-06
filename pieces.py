from BoardSquare import Black, White

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

def king_moves(board, square, color):
    column, row = square
    x = column_names.index(column)
    y = row_names.index(row)
    for dx in -1, 0, 1:
        for dy in -1, 0, 1:
            if dx or dy:
                if can_move_to(board, color, x + dx, y + dy):
                    file = column_names[x + dx]
                    rank = row_names[y + dy]
                    yield file + rank

def queen_moves(board, square, color):
    return set(valid_moves(board, square, color, [n, s, e, w, ne, se, nw, sw]))

def rook_moves(board, square, color):
    return set(valid_moves(board, square, color, [n, s, e, w]))

def bishop_moves(board, square, color):
    return set(valid_moves(board, square, color, [ne, se, nw, sw]))

def knight_moves(board, square, color):
    column, row = square
    x = column_names.index(column)
    y = row_names.index(row)
    for a, b in (1, 2), (2, 1):
        for dx in -a, a:
            for dy in -b, b:
                if can_move_to(board, color, x + dx, y + dy):
                    file = column_names[x + dx]
                    rank = row_names[y + dy]
                    yield file + rank

def pawn_moves(board, square, color):
    column, row = square
    x = column_names.index(column)
    y = row_names.index(row)
    dy = +1 if color == White else -1
    for dx in -1, +1:
        x2 = x + dx
        y2 = y + dy
        if can_move_to(board, color, x2, y2):
            if board.color_at(x2, y2) is not None:
                file = column_names[x2]
                rank = row_names[y2]
                yield file + rank
    x2 = x
    y2 = y + dy
    if can_move_to(board, color, x2, y2):
        if board.color_at(x2, y2) is None:
            file = column_names[x2]
            rank = row_names[y2]
            yield file + rank
            y2 = y2 + dy
            if y in (1, 6) and can_move_to(board, color, x2, y2):
                if board.color_at(x2, y2) is None:
                    file = column_names[x2]
                    rank = row_names[y2]
                    yield file + rank

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
        if not can_move_to(board, color, x, y):
            break
        yield x, y
        if board.color_at(x, y) is not None:
            break

def can_move_to(board, color, x, y):
    return 0 <= x < 8 and 0 <= y < 8 and board.color_at(x, y) is not color
