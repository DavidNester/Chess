#enum(Knight,Pawn,Rook,Bishop,Queen,King)
KING = 'K'
QUEEN = 'Q'
ROOK = 'R'
BISHOP = 'B'
KNIGHT = 'N'
PAWN = 'P'
pieces = [KING, QUEEN, ROOK, BISHOP, KNIGHT, PAWN]

class ChessPiece(object):
  
  
  def __init__(self,type,color): 
    self.type = type
    self.color = color
    self.lastMove = 0
    
  def IsValidMove(self,Board, fromRow, fromCol, 
                  toRow, toCol, turn, turnNumber):
    if not (InRange(fromRow) and InRange(fromCol) 
                    and InRange(toRow) and InRange(toCol)):
      return False
    elif fromRow == toRow and fromCol == toCol:
      return False
    else:
      return True

def InRange(value):
    if 0 <= value < 8:
        return True
    else:
        return False
