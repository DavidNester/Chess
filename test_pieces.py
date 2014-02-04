import unittest
from BoardSquare import Black
from King import King

class PieceTests(unittest.TestCase):

    def test_king_staying_in_one_place(self):
        king = King(Black)
        board = {(0,0): None,
                 (1,0): None,
                 (2,0): None}
        is_valid = king.IsValidMove(board, 0,0, 0,0, Black, 6)
        self.assertEqual(is_valid, False)
