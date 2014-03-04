from ChessPieces import ChessPiece, BISHOP
from BoardSquare import Colors, White, Black

column_names = 'abcdefgh'
row_names = '12345678'

nw = ( -1, +1)
sw = ( -1, -1)
se = (+1,  -1)
ne = (+1,  +1)

def go(direction, x, y):
    dx, dy = direction
    while True:
        x += dx
        y += dy
        if not (0 <= x < 8 and 0 <= y < 8):
            break
        # if position is my own piece:
        #   break
        # if position is opponent piece:
        #   yield x, y
        #   break
        yield x, y



class Bishop(ChessPiece):
	
	
    def __init__(self,color):
        super(Bishop,self).__init__(Bishop,color)
    
    def valid_moves(self, board, position, turn, turn_number):
        """Position looks like 'a5'."""
        column, row = position
        x = column_names.index(column)
        y = row_names.index(row)
        directions = nw, sw, ne, se
        for direction in directions:
            for x2, y2 in go(direction, x, y):
                yield (x2, y2)

    def new_is_valid_move(self,board,from_row,
                          from_col,to_row,to_col,turn,turn_number):
        moves = []
        #could probably change so the method receives position
        position = "%s%s" % (row_names(from_row),column_names(from_col))
        while True:
            moves.append(valid_moves(board, position, turn, turn_number))
        to_position = "%s%s" % (row_names(to_row),column_names(to_col))
        for item in moves:
            if item == position:
                return True
        return False

    def is_valid_move(self,board,from_row,
                             from_col,to_row,to_col,turn,turn_number):
        if not (super(Bishop,self).is_valid_move(board,from_row,from_col,
                                               to_row,to_col,turn,turn_number)):
            return False
        if to_col == from_col or to_row == from_row:
            return False
        if abs(from_row - to_row) != abs(from_col - to_col):
            return False
        if abs(from_row - to_row) == abs(from_col - to_col):
            # C#: for (int i = 1; i < Math.Abs(from_row-to_row); i++)
            for i in range(1, abs(from_row-to_row)):
                if from_row > to_row and from_col > to_col:
                    if board[from_row-i,from_col-i].ChessPiece != None:
                        return False
                elif from_row > to_row and from_col < to_col:
                    if board[from_row-i,from_col+i].ChessPiece != None:
                        return False
                elif from_row < to_row and from_col < to_col:
                    if board[from_row+i,from_col+i].ChessPiece != None:
                        return False
                elif from_row < to_row and from_col > to_col:
                    if board[from_row+i,from_col-i].ChessPiece != None:
                        return False
        if board[to_row, to_col].ChessPiece == None:
            return True
        elif board[to_row, to_col].ChessPiece.color != turn:
            return True
        else:
            return False
	
