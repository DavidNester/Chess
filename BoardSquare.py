#enum ChessColors (white, black)
White = 'W'
Black = 'B'
Colors = ['White','Black']

class BoardSquare(object):
  
  
    def __init__(self, row, col):
        self.row = row
        self.col = col