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
