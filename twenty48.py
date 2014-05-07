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

    def _moveh(self, loop_list, jstep):
        score = 0
        moves = set()
        new_board = self._copy()
        for i in loop_list:
            combined = False#changed if moved to 4x4
            for j in loop_list:
                index = j + jstep
                real = j
                zeros = True
                moved = False
                change = 0
                if new_board.rows[i][j] != 0:
                    while zeros:
                        if index > -1 and index < 3:
                            if new_board.rows[i][index] == 0:
                                new_board.rows[i][index] = new_board.rows[i][j]
                                new_board.rows[i][j] = 0
                                index += jstep
                                j += jstep
                                change = -jstep
                                moved = True
                            elif new_board.rows[i][index] == new_board.rows[i][j]:
                                if not combined:#changed if 4x4
                                    new_board.rows[i][index] = new_board.rows[i][index]*2
                                    new_board.rows[i][j] = 0
                                    moved = True
                                    combined = True#changed if 4x4
                                    change = 0
                                    score += new_board.rows[i][index] 
                                else:
                                    zeros = False
                            else:
                                zeros = False
                        else:
                            zeros = False
                if moved:
                    moves.add((i, real, i, index+change))
        if moves == set():
            return self, set(),0
        else:
            new_board.add_2()
            return new_board, moves, score

    def move_left(self):
        loop_list = range(0,3)
        jstep = -1
        return self._moveh(loop_list, jstep)

    def move_right(self):#needs to be changed
        loop_list = backwards
        jstep = 1
        return self._moveh(loop_list, jstep)
    
    def _movev(self, loop_list, istep):
        score = 0
        moves = set()
        new_board = self._copy()
        for j in loop_list:
            combined = False
            for i in loop_list:
                index = i + istep 
                real = i
                zeros = True
                moved = False
                change = 0
                if new_board.rows[i][j] != 0:
                    while zeros:
                        if index > -1 and index < 3:
                            if new_board.rows[index][j] == 0:
                                new_board.rows[index][j] = new_board.rows[i][j]
                                new_board.rows[i][j] = 0
                                index += istep
                                i += istep
                                change = -istep
                                moved = True
                            elif new_board.rows[index][j] == new_board.rows[i][j]:
                                if not combined:
                                    new_board.rows[index][j] = new_board.rows[index][j]*2
                                    new_board.rows[i][j] = 0
                                    moved = True
                                    combined = True#changed if 4x4
                                    change = 0
                                    score += new_board.rows[index][j]
                                else:
                                    zeros = False
                            else:
                                zeros = False
                        else:
                            zeros = False
                if moved:
                    moves.add((real, j, index + change, j))
        if moves == set():
            return self, set(),0
        else:
            new_board.add_2()
            return new_board, moves, score
    
    def move_up(self):
        loop_list = range(0,3)
        istep = -1
        return self._movev(loop_list, istep)
        
    def move_down(self):#needs to be changed
        loop_list = backwards
        istep = 1
        return self._movev(loop_list, istep)
        
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

