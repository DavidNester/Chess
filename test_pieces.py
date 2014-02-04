import unittest
from BoardSquare import Black, White
from King import King

class Square(object):
    """Test board square."""
    def __init__(self, piece=None):
        self.ChessPiece = piece

def make_3x3_board():
    return {(0,0): Square(),
            (1,0): Square(),
            (2,0): Square()}

class PieceTests(unittest.TestCase):

    def test_king_staying_in_one_place(self):
        king = King(Black)
        board = make_3x3_board()
        is_valid = king.IsValidMove(board, 0,0, 0,0, Black, 6)
        self.assertEqual(is_valid, False)

    def test_king_moving_one_square(self):
        king = King(Black)
        board = make_3x3_board()
        is_valid = king.IsValidMove(board, 0,0, 1,0, Black, 6)
        self.assertEqual(is_valid, True)

    def test_king_moving_back_one_square(self):
        king = King(Black)
        board = make_3x3_board()
        is_valid = king.IsValidMove(board, 1,0, 0,0, Black, 6)
        self.assertEqual(is_valid, True)

    def test_king_moving_two_squares(self):
        king = King(Black)
        board = make_3x3_board()
        is_valid = king.IsValidMove(board, 0,0, 2,0, Black, 6)
        self.assertEqual(is_valid, False)

    def test_king_taking_another_black_piece(self):
        king = King(Black)
        board = make_3x3_board()
        board[2,0] = Square(King(Black))
        is_valid = king.IsValidMove(board, 1,0, 2,0, Black, 6)
        self.assertEqual(is_valid, False)

    def test_king_taking_a_white_piece(self):
        king = King(Black)
        board = make_3x3_board()
        board[2,0] = Square(King(White))
        is_valid = king.IsValidMove(board, 1,0, 2,0, Black, 6)
        self.assertEqual(is_valid, True)

    def test_king_that_cannot_move(self):
        b = Board("rnbqkbnr", #8
                  "pppppppp", #7
                  "........", #6
                  "........", #5
                  "........", #4
                  "........", #3
                  "PPPPPPPP", #2
                  "RNBQKBNR", #1
                  #abcdefgh
                  )
        moves = b.valid_moves('e1')
        self.assertEqual(moves, [])

    def test_king_that_can_move_up(self):
        b = Board("rnbqkbnr", #8
                  ".p.ppp.p", #7
                  "..p.....", #6
                  "p.....p.", #5
                  "....P...", #4
                  "...P.P..", #3
                  "PPP...PP", #2
                  "RNBQKBNR", #1
                  #abcdefgh
                  )
        moves = b.valid_moves('e1')
        self.assertEqual(moves, ['d2', 'e2', 'f2'])

column_names = 'abcdefgh'
row_names = '12345678'

class Board(object):
    def __init__(self, *rows):
        self.rows = [list(row) for row in reversed(rows)]

    def valid_moves(self, square):  # 'a1'
        board = self
        letter, number = square
        y = row_names.index(number)
        x = column_names.index(letter)
        piece = King(White)  # TODO: detect what the piece really is
        moves = []
        for column in column_names:
            x2 = column_names.index(column)
            for row in row_names:
                y2 = row_names.index(row)
                if piece.IsValidMove(board, y,x, y2,x2, piece.color, 12):
                    moves.append(column + row)
        return moves

    def __getitem__(self, yx_coordinate):
        y, x = yx_coordinate
        code = self.rows[y][x]
        piece_class = piece_classes[code.lower()]
        color = White if code.isupper() else Black
        piece = piece_class(color)
        square = Square(piece)
        return square

Queen = Bishop = Rook = Knight = Pawn = King

def return_none(color):
    return None

piece_classes = {
    'k': King,
    'q': Queen,
    'b': Bishop,
    'n': Knight,
    'r': Rook,
    'p': Pawn,
    '.': return_none,
    }
