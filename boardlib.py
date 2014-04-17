import pieces
from pieces import Black, White

column_names = 'abcdefgh'
row_names = '12345678'

piece_functions = {
    'k': pieces.king_moves,
    'q': pieces.queen_moves,
    'b': pieces.bishop_moves,
    'r': pieces.rook_moves,
    'n': pieces.knight_moves,
    'p': pieces.pawn_moves,
    }

class Board(object):
    def __init__(self, *rows):
        if not rows:
            rows = ["rnbqkbnr", #8
                    "pppppppp", #7
                    "........", #6
                    "........", #5
                    "........", #4
                    "........", #3
                    "PPPPPPPP", #2
                    "RNBQKBNR", #1
                    #abcdefgh
                    ]
        if len(rows) != 8:
            raise ValueError('a chess board needs 8 rows but you have only'
                             ' provided {}'.format(len(rows)))
        self.rows = [list(row) for row in reversed(rows)]
        
    def __eq__(self, other_board):
        return self.rows == other_board.rows
    
    def _print(self):
        for item in self.rows:
            print item

    def move(self, from_square, to_square):
        list_of_moves = self.valid_moves(from_square)
        if to_square not in list_of_moves:
            return self
        new_board = Board(*reversed(self.rows))
        #new_board._print()
        #self._print()
        letter, number = from_square
        fx = column_names.index(letter)
        fy = row_names.index(number)
        piece = self.rows[fy][fx]
        tletter, tnumber = to_square
        tx = column_names.index(tletter)
        ty = row_names.index(tnumber)
        new_board.rows[ty][tx] = piece
        new_board.rows[fy][fx] = '.'
        return new_board
        
    def how_to_check_mate(self, color):
        if color is Black:
            opp_color = White
        else:
            opp_color = Black
        moves = list()
        for column in column_names:
            for row in row_names:
                square = '%s%s' % (column, row)
                if self.color_at_square(square) is color:
                    for move in valid_moves(square):
                        if self.move(square,move).in_checkmate(opp_color) is True:
                            moves.append("%s --> %s" %(square,move))
        return moves
    
    def in_checkmate(self, color):
        king_square = self.king_location(color)
        check = True
        for column in column_names:
            for row in row_names:
                square = '%s%s' % (column, row)
                piece_color = self.color_at_square(square)
                if piece_color is color:
                    list_of_moves = valid_moves(square)
                    for move in list_of_moves:
                        if not self.move(square,move).in_check(color):
                            check = False
        return check
    
    def valid_moves(self, square):  # 'a1'
        board = self
        letter, number = square
        y = row_names.index(number)
        x = column_names.index(letter)
        code = self.rows[y][x]
        color = self.color_at(x, y)
        get_moves = piece_functions[code.lower()]
        return set(get_moves(board, square, color))

    def _code_at_square(self, square):
        letter, number = square
        x = column_names.index(letter)
        y = row_names.index(number)
        return self.rows[y][x]

    def piece_at_square(self, square):
        code = self._code_at_square(square)
        return code.lower()

    def color_at_square(self, square):
        code = self._code_at_square(square)
        if code.isupper():
            return White
        if code.islower():
            return Black
        return None

    def color_at(self, x, y):
        code = self.rows[y][x]
        return None if code == '.' else White if code.isupper() else Black
    
    #assuming the move is already shown on the board
    def in_check(self, color):
        king_square = self.king_location(color)
        for column in column_names:
            for row in row_names:
                square = '%s%s' % (column, row)
                piece_color = self.color_at_square(square)
                if piece_color is not None and piece_color is not color:
                    list_of_moves = self.valid_moves(square)
                    if king_square in list_of_moves:
                        return True
        return False

    def king_location(self, turn):
        for column in column_names:
            for row in row_names:
                square = '%s%s' % (column, row)
                if self.piece_at_square(square) == 'k' and self.color_at_square(square) == turn:
                    return square
