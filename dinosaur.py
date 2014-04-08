
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

    screen = pygame.display.set_mode((800, 800))
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
                #elif event.key == c.K_RIGHT:
                #    dx = 5
                #    dy = 0
                #elif event.key == c.K_LEFT:
                #    dx = -5
                #    dy = 0 
                #elif event.key == c.K_UP:
                #    dy = -5
                #    dx = 0
                #elif event.key == c.K_DOWN:
                #    dy = 5
                #    dx = 0 
        d = 3
        m += d
        n += d
        
        
        screen.fill((255, 255, 255))
            
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

