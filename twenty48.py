from random import randint

class Board_2048(object):

    def __init__(self, rows=None):
        if not rows:
            rows = [[0,0,0],
                    [0,0,0],
                    [0,0,0]]
            self.rows = list(rows)
            self.add_2()
            self.add_2()
        else:
            self.rows = list(rows)
    
    def move_left(self):
		moves = list()
		new_board = self._copy()
        for i in range(0,3):
            for j in range(0,3):
                index = j - 1
                zeros = True
                while zeros:
                    if index > -1 and index < 3:
                        if new_board.rows[i][index] == 0:
                            new_board.rows[i][index] = self.rows[i][j]
                            new_board.rows[i][j] = 0
                            index -= 1
                            j -= 1
                        elif new_board.rows[i][index] == self.rows[i][j]:
                            new_board.rows[i][index] = self.rows[i][index]*2
                            new_board.rows[i][j] = 0
                            zeros = False
                        else:
                            zeros = False
                    else:
                        zeros = False
				moves.append((i,j,i,index))
        new_board.add_2()
		return new_board, moves
        print new_board.rows
    
    def move_right(self):#needs to be changed
        for i in backwards:
            for j in backwards:
                index = j + 1
                zeros = True
                while zeros:
                    if index > -1 and index < 3:
                        if new_board.rows[i][index] == 0:
                            new_board.rows[i][index] = self.rows[i][j]
                            new_board.rows[i][j] = 0
                            index += 1
                            j += 1
                        elif new_board.rows[i][index] == self.rows[i][j]:
                            new_board.rows[i][index] = self.rows[i][index]*2
                            new_board.rows[i][j] = 0
                            zeros = False
                        else:
                            zeros = False
                    else:
                        zeros = False
        new_board.add_2()
        print new_board.rows
    
    def move_up(self):
        for j in range(0,3):
            for i in range(0,3):
                index = i - 1
                zeros = True
                while zeros:
                    if index > -1 and index < 3:
                        if new_board.rows[index][j] == 0:
                            new_board.rows[index][j] = self.rows[i][j]
                            new_board.rows[i][j] = 0
                            index -= 1
                            i -= 1
                        elif new_board.rows[index][j] == self.rows[i][j]:
                            new_board.rows[index][j] = self.rows[index][j]*2
                            new_board.rows[i][j] = 0
                            zeros = False
                        else:
                            zeros = False
                    else:
                        zeros = False
        new_board.add_2()
        print new_board.rows
    
    def move_down(self):#needs to be changed
        for j in backwards:
            for i in backwards:
                index = i + 1
                zeros = True
                while zeros:
                    if index > -1 and index < 3:
                        if new_board.rows[index][j] == 0:
                            new_board.rows[index][j] = self.rows[i][j]
                            new_board.rows[i][j] = 0
                            index += 1
                            i += 1
                        elif new_board.rows[index][j] == self.rows[i][j]:
                            new_board.rows[index][j] = self.rows[index][j]*2
                            new_board.rows[i][j] = 0
                            zeros = False
                        else:
                            zeros = False
                    else:
                        zeros = False
        new_board.add_2()
        print new_board.rows
		
	def _copy(self):
		return Board(self.rows)
        
    def print_board(self):
        for i in range(0,3):
            print 'row %s' % i
            for j in range(0,3):
                print self.rows[i][j]
    
    def add_2(self):
        open_spaces = self.open_spaces()
        number = randint(0,len(open_spaces)-1)
        i,j = open_spaces[number]
		new_value = 0
		if rand() - .9 > 0:
			new_value = 4
		else:
			new_value = 2
        self.rows[i][j] = new_value
    
    def open_spaces(self):
        open_space = list()
        for i in range(0,3):
            for j in range(0,3):
                if self.rows[i][j] == 0:
                    open_space.append((i,j))
        return open_space

backwards = (2,1,0)

