from ChessPieces import ChessPiece, QUEEN
from BoardSquare import Colors, White, Black

column_names = 'abcdefgh'
row_names = '12345678'

nw = ( -1, +1)
sw = ( -1, -1)
se = (+1,  -1)
ne = (+1,  +1)
n = ( 0, +1)
s = ( 0, -1)
w = (+1,  0)
e = (-1,  0)

def go(direction, x, y):
    dx, dy = direction
    while True:
        x += dx
        y += dy
        if not (0 <= x < 8 and 0 <= y < 8):
            break
        if board[x,y].ChessPiece.color is self.color:
           break
        if board[x,y].ChessPiece.color is not self.color:
           yield x, y
           break
        yield x, y

class Queen(ChessPiece):
    
    
    def __init__(self,color):
        super(Queen,self).__init__(Queen,color)
		
	def valid_moves(self, board, position, turn, turn_number):
        """Position looks like 'a5'."""
        column, row = position
        x = column_names.index(column)
        y = row_names.index(row)
        directions = n, s, e, w, ne, nw, se, sw
        for direction in directions:
            for x2, y2 in go(direction, x, y):
                yield (x2, y2)
				
	def new_is_valid_move(self,board,from_row,from_col,
						  to_row,to_col,turn,turn_number):
        moves = []
        #could probably change so the method receives position
        position = "%s%s" % (row_names[from_row], column_names[from_col])
        while True:
            moves.append(valid_moves(board, position, turn, turn_number))
			to_position = (to_row, to_col)
		for item in moves:
			if item == to_position:
                return True
        return False
    
    def is_valid_move(self,board,from_row,from_col,
                             to_row,to_col,turn,turn_number):
        if not (super(Queen,self).is_valid_move(board,from_row,from_col,
                                               to_row,to_col,turn,turn_number)):
            return False
        if from_row != to_row and from_col != to_col and abs(from_row -         to_row) != abs(from_col - to_col):
            return False 
        if from_row == to_row:
            if abs(from_col - to_col) == 1:
                if board[to_row, to_col].ChessPiece == None:
                    return True
                if board[to_row, to_col].ChessPiece.color != turn:
                    return True
                else:
                    return False
            if abs(from_col - to_col) == 2:
                if from_col > to_col:
                    if board[from_row, from_col-1].ChessPiece != None:
                        return False
                if from_col < to_col:
                    if board[from_row, from_col+1].ChessPiece != None:
                        return False
            # C#: for (int i = 1; i <= Math.Abs(to_col - from_col) - 1; i++)
            else:
                for i in range(1,abs(to_col - from_col)):
                    if from_col > to_col:
                        if board[from_row, from_col - i].ChessPiece != None:
                            return False
                    if from_col < to_col:
                        if board[from_row, from_col + i].ChessPiece != None:
                            return False
        if from_col == to_col:
            if abs(from_row - to_row) == 1:
                if board[to_row, to_col].ChessPiece == None:
                    return True
                elif board[to_row, to_col].ChessPiece.color != turn:
                    return True
                else:
                    return False
                # C#: for (int i = 1; i <= Math.Abs(to_row - from_row) - 1; i++)
            for i in range(1,abs(to_row - from_row)):
                if from_row > to_row:
                    if board[from_row - i, from_col].ChessPiece != None:
                        return False
                if from_row < to_row:
                    if board[from_row + i, from_col].ChessPiece != None:
                        return False
            
            if board[to_row, to_col].ChessPiece == None:
                return True
            elif board[to_row, to_col].ChessPiece.color != turn:
                return True
            
        if abs(from_row - to_row) == abs(from_col - to_col):
            # C#: for (int i = 1; i < Math.Abs(from_row - to_row); i++)
            for i in range(1,abs(from_row - to_row)):
                if from_row > to_row and from_col > to_col:
                    if board[from_row - i, from_col - i].ChessPiece != None:
                        return False
                if from_row > to_row and from_col < to_col:
                    if board[from_row - i, from_col + i].ChessPiece != None:
                        return False
                if from_row < to_row and from_col < to_col:
                    if board[from_row + i, from_col + i].ChessPiece != None:
                        return False
                if from_row < to_row and from_col > to_col:
                    if board[from_row + i, from_col - i].ChessPiece != None:
                        return False

        if board[to_row, to_col].ChessPiece == None:
            return True
        elif board[to_row, to_col].ChessPiece.color != turn:
            return True
        else:
            return False