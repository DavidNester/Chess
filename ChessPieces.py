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
    
  def is_valid_move(self,Board, from_row, from_col, 
                  to_row, to_col, turn, turn_number):
    if not (in_range(from_row) and in_range(from_col)
                    and in_range(to_row) and in_range(to_col)):
      return False
    elif from_row == to_row and from_col == to_col:
      return False
    else:
      return True

def in_range(value):
    if 0 <= value < 8:
        return True
    else:
        return False
