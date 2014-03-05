from ChessPieces import ChessPiece, BISHOP
from BoardSquare import Colors, White, Black

nw = ( -1, +1)
sw = ( -1, -1)
se = (+1,  -1)
ne = (+1,  +1)

class Bishop(ChessPiece):

    directions = nw, sw, ne, se

    def __init__(self,color):
        super(Bishop,self).__init__(Bishop,color)