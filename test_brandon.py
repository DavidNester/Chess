"""Suggested first tests for the Chess project.

What will the outside interface to the chess program look like?
Obviously, it could support as many as its wants.  This is just one
possibility and we can do something completely different instead if the
author wants to!  But something like getting this test working should be
the project's first goal.

I am imagining that many users will want an API call that builds a board
for them from a string which is a picture of the board, with white as
capital letters and black as lower case.

From the project directory, tests can be auto-discovered and run with::

    python -m unittest discover

"""
import unittest
from api import build_board

class BoardTests(unittest.TestCase):

    def test_start_position(self):
        s = """rnbqkbnr
               pppppppp
               ........
               ........
               ........
               ........
               PPPPPPPP
               RNBQKBNR"""
        b = build_board(s)
        self.assertEqual(b.white_in_check(), False)
        self.assertEqual(b.black_in_check(), False)

    def test_endgame_position(self):
        s = """...k..R.
               ........
               ...K....
               ........
               ........
               ........
               ........
               ........"""
        b = build_board(s)
        self.assertEqual(b.white_in_check(), False)
        self.assertEqual(b.black_in_check(), True)
