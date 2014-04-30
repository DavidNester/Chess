
import pygame, sys
from pygame import constants as c
from twenty48 import Board_2048

# Shell script for converting images:
# for filename in *.ico; do name=$(basename $filename .ico);
# convert $name.ico -type truecolormatte PNG32:$name.png;
# mv $name-0.png $name.png; rm *-[12345].png; done

def main():
    board = Board_2048()
    print board.rows
    screen = pygame.display.set_mode((400, 400))
    clock = pygame.time.Clock()
    tile_images = {}
    moves = list()
    for number in ('0', '2', '4', '8', '16', '32'):
        filename = 'static/{}.jpg'.format(number)
        nimage = pygame.image.load(filename)
        nimage = nimage.convert_alpha()
        nimage = pygame.transform.smoothscale(nimage, (76, 76))
        tile_images[number] = nimage

    while True:
        for event in pygame.event.get():
            if event.type == c.KEYDOWN:
                if event.key == c.K_ESCAPE:
                    sys.exit(0)

                # NEW:
                elif event.key == c.K_RIGHT:
                    board, moves = board.move_right()
                elif event.key == c.K_LEFT:
                    board, moves = board.move_left() 
                elif event.key == c.K_UP:
                    board, moves = board.move_up()
                elif event.key == c.K_DOWN:
                    board, moves = board.move_down()

        screen.fill((255, 255, 255))
        for a in range(1,4):
            for b in range(1,4):
                e = (80*a)-80
                f = (80*b)-80
                pygame.draw.rect(screen, (0,0,0), (e,f,80,80), 1)

        row =''
        for i in range(0,3):
            row += '%s' % board.rows[0][i]
        for i, letter in enumerate(row):
            x = 80 * i + 2
            y = 2
            screen.blit(tile_images[letter], (x, y))
        row =''
        for i in range(0,3):
            row += '%s' % board.rows[1][i]
        for i, letter in enumerate(row):
            x = 80  * i + 2
            y = 2 +80
            screen.blit(tile_images[letter], (x, y))
        row =''
        for i in range(0,3):
            row += '%s' % board.rows[2][i]
        for i, letter in enumerate(row):
            x = 80 * i + 2
            y = 2 + 160
            screen.blit(tile_images[letter], (x, y))
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()

