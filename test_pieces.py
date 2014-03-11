import pieces
import unittest
from pieces import Black, White

piece_functions = {
    'k': pieces.king_moves,
    'q': pieces.queen_moves,
    'b': pieces.bishop_moves,
    'r': pieces.rook_moves,
    'n': pieces.knight_moves,
    'p': pieces.pawn_moves,
    # '.': return_none,
    }

class PieceTests(unittest.TestCase):

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
       self.assertEqual(moves, set())
  
    def test_king_taking_a_piece(self):
        b = Board("rnbqkbnr", #8
                 "pppppppp", #7
                 "....K...", #6
                 "........", #5
                 "........", #4
                 "........", #3
                 "PPPPPPPP", #2
                 "RNBQ.BNR", #1
                  #abcdefgh
                  )
        moves = b.valid_moves('e6')
        self.assertEqual(moves, {'d5', 'd6', 'd7', 'e5',
                                'e7', 'f5', 'f6', 'f7'})

    def test_white_pawn_free(self):
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
        self.assertEqual(moves, {'b4'})

    def test_white_pawn_starting(self):
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
        moves = b.valid_moves('e2')
        self.assertEqual(moves, {'e3', 'e4'})

    def test_white_pawn_attack(self):
        b = Board("rnbqkbnr", #8
                  ".p.ppppp", #7
                  "........", #6
                  "........", #5
                  "p.p.....", #4
                  ".P......", #3
                  "P.PPPPPP", #2
                  "RNBQKBNR", #1
                  #abcdefgh
                  )
        moves = b.valid_moves('b3')
        self.assertEqual(moves, {'a4', 'b4', 'c4'})

    def test_white_pawn_attack_starting(self):
        b = Board("rnbqkbnr", #8
                  "...ppppp", #7
                  "........", #6
                  "........", #5
                  "........", #4
                  "ppp.....", #3
                  "PPPPPPPP", #2
                  "RNBQKBNR", #1
                  #abcdefgh
                  )
        moves = b.valid_moves('b2')
        self.assertEqual(moves, {'a3', 'c3'})

    def test_black_pawn_free(self):
        b = Board("rnbqkbnr", #8
                  "p.pppppp", #7
                  ".p......", #6
                  "........", #5
                  "........", #4
                  "........", #3
                  "PPPPPPPP", #2
                  "RNBQKBNR", #1
                  #abcdefgh
                  )
        moves = b.valid_moves('b6')
        self.assertEqual(moves, {'b5'})

    def test_black_pawn_starting(self):
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
        moves = b.valid_moves('e7')
        self.assertEqual(moves, {'e5', 'e6'})

    def test_black_pawn_attack(self):
        b = Board("rnbqkbnr", #8
                  "p.pppppp", #7
                  ".p......", #6
                  "P.P.....", #5
                  "........", #4
                  "........", #3
                  ".P.PPPPP", #2
                  "RNBQKBNR", #1
                  #abcdefgh
                  )
        moves = b.valid_moves('b6')
        self.assertEqual(moves, {'a5', 'b5', 'c5'})

    def test_black_pawn_attack_starting(self):
        b = Board("rnbqkbnr", #8
                  "pppppppp", #7
                  "PPP.....", #6
                  "........", #5
                  "........", #4
                  "........", #3
                  "...PPPPP", #2
                  "RNBQKBNR", #1
                  #abcdefgh
                  )
        moves = b.valid_moves('b7')
        self.assertEqual(moves, {'a6', 'c6'})
    
    def test_white_knight(self):
        b = Board("rnbqkbnr", #8
                  "pppppppp", #7
                  "........", #6
                  "........", #5
                  "........", #4
                  "..N.....", #3
                  "PPPPPPPP", #2
                  "R.BQKBNR", #1
                  #abcdefgh
                  )
        moves = b.valid_moves('c3')
        self.assertEqual(moves, {'a4', 'b1', 'b5', 'd5', 'e4'})

    def test_white_knight_start(self):
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
        moves = b.valid_moves('b1')
        self.assertEqual(moves, {'a3', 'c3'})

    def test_white_knight_attack(self):
        b = Board("rnbqkbnr", #8
                  ".ppp.ppp", #7
                  "........", #6
                  "........", #5
                  "p...p...", #4
                  "..N.....", #3
                  "PPPPPPPP", #2
                  "R.BQKBNR", #1
                  #abcdefgh
                  )
        moves = b.valid_moves('c3')
        self.assertEqual(moves, {'a4', 'b1', 'b5', 'd5', 'e4'})
        
    def test_black_knight(self):
        b = Board("r.bqkbnr", #8
                  "pppppppp", #7
                  "..n.....", #6
                  "........", #5
                  "........", #4
                  "........", #3
                  "PPPPPPPP", #2
                  "RNBQKBNR", #1
                  #abcdefgh
                  )
        moves = b.valid_moves('c6')
        self.assertEqual(moves, {'a5', 'b4', 'b8', 'd4', 'e5'})


    def test_black_knight_start(self):
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
        moves = b.valid_moves('b8')
        self.assertEqual(moves, {'a6', 'c6'})
    
    def test_black_knight_attack(self):
        b = Board("r.bqkbnr", #8
                  "pppppppp", #7
                  "..n.....", #6
                  "P...P...", #5
                  "........", #4
                  "........", #3
                  "PPPPPPPP", #2
                  "RNBQKBNR", #1
                  #abcdefgh
                  )
        moves = b.valid_moves('c6')
        self.assertEqual(moves, {'a5', 'b4', 'b8', 'd4', 'e5'})

    def test_white_bishop(self):
        b = Board("rnbqkbnr", #8
                  "pppppppp", #7
                  "........", #6
                  "........", #5
                  "........", #4
                  "BP......", #3
                  "P.PPPPPP", #2
                  "RN.QKBNR", #1
                  #abcdefgh
                  )
        moves = b.valid_moves('a3')
        self.assertEqual(moves, {'b2', 'b4', 'c1', 'c5', 'd6', 'e7'})
    
    def test_white_bishop_start(self):
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
        moves = b.valid_moves('c1')
        self.assertEqual(moves, set())
    
    def test_white_bishop_attack(self):
        b = Board("rnbqkbnr", #8
                  ".ppp.ppp", #7
                  "........", #6
                  "........", #5
                  ".p......", #4
                  "BP......", #3
                  "PbPPPPPP", #2
                  "RN.QKBNR", #1
                  #abcdefgh
                  )
        moves = b.valid_moves('a3')
        self.assertEqual(moves, {'b2', 'b4'})

    def test_black_bishop(self):
        b = Board("rn.qkbnr", #8
                  "p.pppppp", #7
                  "bp......", #6
                  "........", #5
                  "........", #4
                  "........", #3
                  "PPPPPPPP", #2
                  "RNBQKBNR", #1
                  #abcdefgh
                  )
        moves = b.valid_moves('a6')
        self.assertEqual(moves, {'b5', 'b7', 'c4', 'c8', 'd3', 'e2'})
    
    
    def test_black_bishop_start(self):
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
        moves = b.valid_moves('c8')
        self.assertEqual(moves, set())
    
    def test_black_bishop_attack(self):
        b = Board("rn.qkbnr", #8
                  "pBpppppp", #7
                  "bp......", #6
                  ".P......", #5
                  "........", #4
                  "........", #3
                  "PPPPPPPP", #2
                  "RNBQKBNR", #1
                  #abcdefgh
                  )
        moves = b.valid_moves('a6')
        self.assertEqual(moves, {'b5', 'b7'})
    
    def test_white_rook(self):
        b = Board("rnbqkbnr", #8
                  "pppppppp", #7
                  "........", #6
                  "P.......", #5
                  "........", #4
                  "R.......", #3
                  ".PPPPPPP", #2
                  ".NBQKBNR", #1
                  #abcdefgh
                  )
        moves = b.valid_moves('a3')
        self.assertEqual(moves, {'a1', 'a2', 'a4', 'b3', 'c3',
                                 'd3', 'e3', 'f3', 'g3', 'h3'})
    
    def test_white_rook_start(self):
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
        moves = b.valid_moves('a1')
        self.assertEqual(moves, set())
    
    def test_white_rook_attack(self):
        b = Board("rnbqkbnr", #8
                  "p.pp..pp", #7
                  "........", #6
                  ".p.R.p..", #5
                  "P.......", #4
                  "...b....", #3
                  ".PPPPPPP", #2
                  ".NBQKBNR", #1
                  #abcdefgh
                  )
        moves = b.valid_moves('d5')
        self.assertEqual(moves, {'b5', 'c5', 'd3', 'd4', 'd6', 'd7', 'e5', 'f5'})
    
    def test_black_rook(self):
        b = Board(".nbqkbnr", #8
                  ".ppppppp", #7
                  "r.......", #6
                  "........", #5
                  "p.......", #4
                  "........", #3
                  "PPPPPPPP", #2
                  "RNBQKBNR", #1
                  #abcdefgh
                  )
        moves = b.valid_moves('a6')
        self.assertEqual(moves, {'a5', 'a7', 'a8', 'b6', 'c6',
                                 'd6', 'e6', 'f6', 'g6', 'h6'})
    
    
    def test_black_rook_start(self):
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
        moves = b.valid_moves('a8')
        self.assertEqual(moves, set())
    
    def test_black_rook_attack(self):
        b = Board(".nbqkbnr", #8
                  ".ppppppp", #7
                  "........", #6
                  "pP.r.P..", #5
                  "........", #4
                  "........", #3
                  "PPPPPPPP", #2
                  "RNBQKBNR", #1
                  #abcdefgh
                  )
        moves = b.valid_moves('d5')
        self.assertEqual(moves, {'b5', 'c5', 'd2', 'd3',
                                 'd4', 'd6', 'e5', 'f5'})
    def test_white_queen(self):
        b = Board("rnbqkbnr", #8
                  "pppppppp", #7
                  "........", #6
                  "........", #5
                  "....P.Q.", #4
                  "........", #3
                  "PPPP.PPP", #2
                  "RNB.KBNR", #1
                  #abcdefgh
                  )
        moves = b.valid_moves('g4')
        self.assertEqual(moves, {'d1', 'd7', 'e2', 'e6', 'f3',
                                 'f4', 'f5', 'g3', 'g5', 'g6',
                                 'g7', 'h3', 'h4', 'h5'})
            
    def test_white_queen_start(self):
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
        moves = b.valid_moves('d1')
        self.assertEqual(moves, set())
    
    def test_white_queen_attack(self):
        b = Board("r..qk.nr", #8
                  "p.....pp", #7
                  "..npb...", #6
                  ".p.Q.p..", #5
                  "..p.p...", #4
                  "...b....", #3
                  "PPPPPPPP", #2
                  "RNBQKBNR", #1
                  #abcdefgh
                  )
        moves = b.valid_moves('d5')
        self.assertEqual(moves, {'b5', 'c4', 'c5', 'c6', 'd3',
                                 'd4', 'd6', 'e4', 'e5', 'e6',
                                 'f5'})
    
    def test_black_queen(self):
        b = Board("rnb.kbnr", #8
                  "pp.ppppp", #7
                  "........", #6
                  "q.p.....", #5
                  "........", #4
                  "........", #3
                  "PPPPPPPP", #2
                  "RNBQKBNR", #1
                  #abcdefgh
                  )
        moves = b.valid_moves('a5')
        self.assertEqual(moves, {'a2', 'a3', 'a4', 'a6', 'b4',
                                 'b5', 'b6', 'c3', 'c7', 'd2',
                                 'd8'})
    
    
    def test_black_queen_start(self):
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
        moves = b.valid_moves('d8')
        self.assertEqual(moves, set())
    
    def test_black_queen_attack(self):
        b = Board(".nbqkbnr", #8
                  ".ppppppp", #7
                  "..PBP...", #6
                  "pP.q.P..", #5
                  "..P.P...", #4
                  "...P....", #3
                  "PPPPPPPP", #2
                  "RNBQKBNR", #1
                  #abcdefgh
                  )
        moves = b.valid_moves('d5')
        self.assertEqual(moves, {'b5', 'c4', 'c5', 'c6',
                                 'd3', 'd4', 'd6', 'e4',
                                 'e5', 'e6', 'f5'})

#my attempts at check
##################################################################
def make_move(self, board, from_row, from_col, to_row, to_col):
    board[to_row,to_col].ChessPiece = board[from_row, from_col].ChessPiece
    board[from_row, from_col].ChessPiece = None

def check_for_check(self, board, turn):
    king_col, king_row = king_location(board, turn)
    for column in column_names:
        x2 = column_names.index(column)
        for row in row_names:
            y2 = row_names.index(row)
            if board[row, column].ChessPiece.color is not turn:
                piece = board[row, column].ChessPiece
                if piece.is_valid_move(board, row, column, king_row,
                                       king_col, piece.color, 12):
                    return True
    return False

def move_controller(self, board, from_row, from_col, to_row, to_col, turn):
    replaced_piece = board[to_row,to_col].ChessPiece
    make_move(board, from_row, from_col, to_row, to_col)
    if check_for_check:
        make_move(board, to_row, to_col, from_row, from_col)
        board[to_row,to_col].ChessPiece = replaced_piece
    else:
        turn_number += 1
        if turn is White:
            turn = Black
        else:
            turn = White

####################################################################

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
        code = self.rows[y][x]
        color = self.color_at(x, y)
        get_moves = piece_functions[code.lower()]
        return set(get_moves(board, square, color))

    def color_at(self, x, y):
        code = self.rows[y][x]
        return None if code == '.' else White if code.isupper() else Black
    
    #assuming the move is already shown on the board
    def in_check(self, color):
        king_col, king_row = king_location(board, color)
        for column in column_names:
            x2 = column_names.index(column)
            for row in row_names:
                y2 = row_names.index(row)
                if self.rows[column][row].IsUpper():
                    
                    return True
    return False
                

    def king_location(self, board, turn):
        for column in column_names:
            for row in row_names:
                if self.rows[column][row] == 'K' if turn == White else 'k':
                    return "%s" % (column,row)

def return_none(color):
    return None
