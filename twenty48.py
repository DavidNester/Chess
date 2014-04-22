class Board_2048(object):

    def __init__(self, rows=None):
        if not rows:
            a = Tile(0)
            rows = [[a,      a,a],
                    [a,Tile(2),a],
                    [a,Tile(2),a]]
        self.rows = [list(row) for row in reversed(rows)]
    
    def move(self, vertical, horizontal):#only does left at the moment
        if vertical == 0:
            for i in range(0,3):
                for j in range(0,3):
                    index = j + horizontal
                    if index > -1 and index < 3:
                        if self.rows[i][index].number == self.rows[i][j].number:
                            self.rows[i][index] = Tile(self.rows[i][index].number*2)
                            self.rows[i][j] = Tile(0)
                        elif self.rows[i][index].number == 0:
                            self.rows[i][index] = Tile(self.rows[i][j].number)
                            self.rows[i][j] = Tile(0)
        self.print_board()
        
    def print_board(self):
        for i in range(0,3):
            print 'row %s' % i
            for j in range(0,3):
                print self.rows[i][j].number
    
    def add_2(self):
        return None #adds 2 to an empty spot

class Tile(object):
    
    def __init__(self, number):
        if number == 0:
            self.image = None
        else:
            self.image = None#will be changed
        self.number = number
