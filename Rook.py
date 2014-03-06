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
