#enum(Knight,Pawn,Rook,Bishop,Queen,King)
King = 'K'
Queen = 'Q'
Rook = 'R'
Bishop = 'B'
Knight = 'N'
Pawn = 'P'
pieces = [King, Queen, Rook, Bishop, Knight, Pawn]
class ChessPiece(object):
  def __init__(self,type,color): 
    self.type = type
    self.color = color
    self.lastMove = 0
    
  def IsValidMove(self,Board, fromRow, fromCol, toRow, toCol, turn, turnNumber)
    if not (InRange(fromRow) and InRange(fromCol) and InRange(toRow) and InRange(toCol)):
      return False
    elif fromRow == toRow and fromCol == toCol:
      return False
    else:
      return True
  
  def InRange(self,value)
    if 0<=value and value<8:
      return True
    else:
      return False
  
    
