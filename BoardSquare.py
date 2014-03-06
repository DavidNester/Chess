#enum ChessColors (white, black)
White = 'WHITE'
Black = 'BLACK'
Colors = ['White','Black']

class BoardSquare(object):
  
  
    def __init__(self, row, col):
        self.row = row
        self.col = col
