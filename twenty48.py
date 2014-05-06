import random

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
        moves = set()
        new_board = self._copy()
        for i in range(0,3):
            combined = False#changed if moved to 4x4
            for j in range(0,3):
                index = j - 1
                real = j
                zeros = True
                moved = False
                change = 0
                if new_board.rows[i][j] != 0:
                    while zeros:
                        if index > -1 and index < 3:
                            if new_board.rows[i][index] == 0:
                                new_board.rows[i][index] = self.rows[i][j]
                                new_board.rows[i][j] = 0
                                index -= 1
                                j -= 1
                                change = 1
                                moved = True
                            elif new_board.rows[i][index] == self.rows[i][j]:
                                if not combined:#changed if 4x4
                                    new_board.rows[i][index] = self.rows[i][index]*2
                                    new_board.rows[i][j] = 0
                                    zeros = False
                                    moved = True
                                    combined = True#changed if 4x4
                                    change = 0
                                else:
                                    zeros = False
                            else:
                                zeros = False
                        else:
                            zeros = False
                if moved:
                    moves.add((i, real, i, index+change))
        #new_board.add_2()
        return new_board, moves
    
    def move_right(self):#needs to be changed
        moves = set()
        new_board = self._copy()
        for i in backwards:
            combined = False#changed if moved to 4x4
            for j in backwards:
                index = j + 1
                real = j
                zeros = True
                moved = False
                change = 0
                if new_board.rows[i][j] != 0:
                    while zeros:
                        if index > -1 and index < 3:
                            if new_board.rows[i][index] == 0:
                                new_board.rows[i][index] = self.rows[i][j]
                                new_board.rows[i][j] = 0
                                index += 1
                                j += 1
                                change = -1
                                moved = True
                            elif new_board.rows[i][index] == self.rows[i][j]:
                                if not combined:
                                    new_board.rows[i][index] = self.rows[i][index]*2
                                    new_board.rows[i][j] = 0
                                    zeros = False
                                    moved = True
                                    combined = True#changed if 4x4
                                    change = 0
                                else:
                                    zeros = False
                            else:
                                zeros = False
                        else:
                            zeros = False
                if moved:
                    moves.add((i, real, i, index+change))
        #new_board.add_2()
        return new_board,moves
    
    def move_up(self):
        moves = set()
        new_board = self._copy()
        for j in range(0,3):
            combined = False
            for i in range(0,3):
                index = i - 1
                real = i
                zeros = True
                moved = False
                change = 0
                if new_board.rows[i][j] != 0:
                    while zeros:
                        if index > -1 and index < 3:
                            if new_board.rows[index][j] == 0:
                                new_board.rows[index][j] = self.rows[i][j]
                                new_board.rows[i][j] = 0
                                index -= 1
                                i -= 1
                                change = 1
                                moved = True
                            elif new_board.rows[index][j] == self.rows[i][j]:
                                if not combined:
                                    new_board.rows[index][j] = self.rows[index][j]*2
                                    new_board.rows[i][j] = 0
                                    zeros = False
                                    moved = True
                                    combined = True#changed if 4x4
                                    change = 0
                                else:
                                    zeros = False
                            else:
                                zeros = False
                        else:
                            zeros = False
                if moved:
                    moves.add((real, j, index + change, j))
        #new_board.add_2()
        return new_board, moves
    
    def move_down(self):#needs to be changed
        moves = set()
        new_board = self._copy()
        for j in backwards:
            combined = False
            for i in backwards:
                index = i + 1
                real = i
                zeros = True
                moved = False
                change = 0
                if new_board.rows[i][j] != 0:
                    while zeros:
                        if index > -1 and index < 3:
                            if new_board.rows[index][j] == 0:
                                new_board.rows[index][j] = self.rows[i][j]
                                new_board.rows[i][j] = 0
                                index += 1
                                i += 1
                                change = -1
                                moved = True
                            elif new_board.rows[index][j] == self.rows[i][j]:
                                if not combined:
                                    new_board.rows[index][j] = self.rows[index][j]*2
                                    new_board.rows[i][j] = 0
                                    zeros = False
                                    combined = True
                                    change = 0
                                    moved = True
                                else:
                                    zeros = False
                            else:
                                zeros = False
                        else:
                            zeros = False
                if moved:
                    moves.add((real, j, index + change, j))
        #new_board.add_2()
        return new_board, moves

    def _copy(self):
    	return Board_2048(self.rows)

    def print_board(self):
        for i in range(0,3):
            print 'row %s' % i
            for j in range(0,3):
                print self.rows[i][j]
    
    def add_2(self):
        open_spaces = self.open_spaces()
        number = random.randint(0,len(open_spaces)-1)
        i,j = open_spaces[number]
        new_value = 0
        r = random.random()
        if r - .9 > 0:
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

