import unittest
from BoardSquare import Black, White
from King import King
from pawn import Pawn

class Square(object):
    """Test board square."""
    def __init__(self, piece=None):
        self.ChessPiece = piece

def make_3x3_board():
    return {(0,0): Square(),
            (1,0): Square(),
            (2,0): Square()}

class PieceTests(unittest.TestCase):

    #def test_king_taking_a_white_piece(self):
    #    king = King(Black)
    #    board = make_3x3_board()
    #   board[2,0] = Square(King(White))
    #   is_valid = king.IsValidMove(board, 1,0, 2,0, Black, 6)
    #   self.assertEqual(is_valid, True)
    
    #def test_king_that_cannot_move(self):
    #   b = Board("rnbqkbnr", #8
    #             "pppppppp", #7
    #             "........", #6
    #             "........", #5
    #             "........", #4
    #             "........", #3
    #             "PPPPPPPP", #2
    #             "RNBQKBNR", #1
    #             #abcdefgh
    #             )
    #   moves = b.valid_moves('e1')
    #   self.assertEqual(moves, [])
    #def test_king_taking_a_piece(self):
    #     b = Board("rnbqkbnr", #8
    #             "pppppppp", #7
    #             "....K...", #6
    #             "........", #5
    #             "........", #4
    #             "........", #3
    #             "PPPPPPPP", #2
    #             "RNBQ.BNR", #1
                  #abcdefgh
    #              )
    #   moves = b.valid_moves('e6')
    #   self.assertEqual(moves, ['d5', 'd6', 'd7', 'e5',
    #                            'e7', 'f5', 'f6', 'f7'])

    def test_pawn(self):
        b = Board("rnbqkbnr", #8
                  "pppppppp", #7
                  "........", #6
                  "........", #5
                  "........", #4
                  ".P......", #3
                  "P.PPPPPP", #2
                  "RNBQKBNR", #1
                  #abcdefgh
                  )
        moves = b.valid_moves('b3')
        self.assertEqual(moves, ['c4'])





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
        piece = Pawn(White)  # TODO: detect what the piece really is
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

Queen = Bishop = Rook = Knight = King
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
