from ChessPieces import ChessPiece, ROOK
from BoardSquare import Colors, White, Black

n = ( 0, +1)
s = ( 0, -1)
w = (+1,  0)
e = (-1,  0)

class Rook(ChessPiece):

    directions = [n, s, e, w]

    def __init__(self,color):
        super(Rook,self).__init__(Rook,color)


if __name__ == '__main__':

    def g():
        for i in range(8):
            yield i * i

    for item in g():
        print item

    from test_pieces import Board

    b = Board("rnbqkbnr", #8
              "p.pppppp", #7
              "........", #6
              ".P......", #5
              "R.......", #4
              "........", #3
              ".PPPPPPP", #2
              ".NBQKBNR", #1
              #abcdefgh
              )
    r = Rook(White)
    print list(r.valid_moves(b, 'a4', White, 3))