
import pygame, sys
from boardlib import Board
from pygame import constants as c

# Shell script for converting images:
# for filename in *.ico; do name=$(basename $filename .ico);
# convert $name.ico -type truecolormatte PNG32:$name.png;
# mv $name-0.png $name.png; rm *-[12345].png; done

def main():
    board = Board()
    # print board.piece_at_square('a1')

    screen = pygame.display.set_mode((1200, 800))
    clock = pygame.time.Clock()
    piece_images = {}
   
    for color, method in ('White', str.upper), ('Black', str.lower):
        for letter, name in zip('pnbrkq', ['Pawn', 'Knight', 'Bishop', 'Rook',
                                           'King', 'Queen']):
            filename = 'static/{}_{}.png'.format(color, name)
            image = pygame.image.load(filename)
            image = image.convert_alpha()
            image = pygame.transform.smoothscale(image, (76, 76))
            piece_images[method(letter)] = image

    m = 2
    n = 2

    while True:
        for event in pygame.event.get():
            if event.type == c.KEYDOWN:
                if event.key == c.K_ESCAPE:
                    sys.exit(0)

                # NEW:
                elif event.key == c.K_RIGHT:
                    Board_2048.move(0,1)
                #    dx = 5
                #    dy = 0
                elif event.key == c.K_LEFT:
                    B0ard_2048.move(0,-1)
                #    dx = -5
                #    dy = 0 
                elif event.key == c.K_UP:
                    Board_2048.move(1,0)
                #    dy = -5
                #    dx = 0
                elif event.key == c.K_DOWN:
                    Board_2048.move(-1,0)
                #    dy = 5
                #    dx = 0 
        d = 3
        m += d
        n += d
        
        
        screen.fill((255, 255, 255))
        ###############3x3 2048        
        #new_board = Board_2048()
        
        for a in range(1,4):
            for b in range(1,4):
                e = 80*a + 800
                f = 80*b
                pygame.draw.rect(screen, (0,0,0), (e,f,80,80), 1)
        ###############3x3 2048
        for i in range(1,9):
            for j in range(1,9):
                filled = (i + j) % 2
                x = (80*i)-80
                y = (80*j)-80
                pygame.draw.rect(screen, (0,0,0), (x,y,80,80), not filled)
        # pygame.display.update()
        screen.blit(piece_images['r'] , (m, n))
        row = 'rnbqkbnr'
        for i, letter in enumerate(row):
            x = 80 * i + 2
            y = 2
            screen.blit(piece_images[letter], (x, y))
        row = 'pppppppp'
        for i, letter in enumerate(row):
            x = 80 * i + 2
            y = 80 + 2
            screen.blit(piece_images[letter], (x, y))
        row = 'RNBQKBNR'
        for i, letter in enumerate(row):
            x = 80 * i + 2
            y = 560 + 2
            screen.blit(piece_images[letter], (x, y))
        row = 'PPPPPPPP'
        for i, letter in enumerate(row):
            x = 80 * i + 2
            y = 480 + 2
            screen.blit(piece_images[letter], (x, y))

        pygame.font.init()
        myfont = pygame.font.SysFont("Comic Sans MS", 30)
        label_1 = myfont.render("Chess Game", 1, (0,0,0))
        label_2 = myfont.render("e5 -> d6", 1, (0,0,0))
        pygame.display.set_caption("This is a chess Game")
        screen.blit(label_1, (300,640))
        screen.blit(label_2, (300,665))
        pygame.display.flip()
        clock.tick(60)
        #dx = dy = 0

if __name__ == "__main__":
    main()

class Board_2048(object):

    def __init__(self, *rows):
        if not rows:
            a = Tile(0)
            rows = [[a,      a,a],
                    [a,Tile(2),a],
                    [a,Tile(2),a]]
        self.rows = [list(row) for row in reversed(rows)]
    
    def move(self, vertical, horizontal):
        if vertical == 0:
            for i in range(0,3):
                for j in range(0,3):
                    index = j + horizontal
                    if index > -1 and index < 3:
                        if self.rows[i][index].number == self.rows[i][j].number:
                            self.rows[i][index] = Tile(self.rows[i][index].number*2)
                            self.row[i][j] = Tile(0)
                        elif self.rows[i][index].number == 0:
                            self.rows[i][index] = Tile(self.rows[i][j].number)
                            self.row[i][j] = Tile(0)

class Tile(object):
    
    def __init__(self, number):
        if number == 0:
            self.image = None
        else:
            self.image = None#will be changed
        self.number = number
