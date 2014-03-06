from ChessPieces import ChessPiece, QUEEN
from BoardSquare import Colors, White, Black

nw = ( -1, +1)
sw = ( -1, -1)
se = (+1,  -1)
ne = (+1,  +1)
n = ( 0, +1)
s = ( 0, -1)
w = (+1,  0)
e = (-1,  0)

class Queen(ChessPiece):

    directions = n, s, e, w, nw, sw, ne, se

    def __init__(self,color):
        super(Queen,self).__init__(Queen,color)

    