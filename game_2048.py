
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
    screen = pygame.display.set_mode((320, 320))
    clock = pygame.time.Clock()
    tile_images = {}
    moves = list()
    for number in ('0', '2', '4', '8', '16', '32', '64', '128', '256'):
        filename = 'static/{}.jpg'.format(number)
        image = pygame.image.load(filename)
        image = image.convert_alpha()
        image = pygame.transform.smoothscale(image, (76, 76))
        tile_images[number] = image

    while True:
        for event in pygame.event.get():
            if event.type == c.KEYDOWN:
                if event.key == c.K_ESCAPE:
                    sys.exit(0)

                # NEW:
                elif event.key == c.K_RIGHT:
                    board, moves = board.move_right()
                    print moves
                elif event.key == c.K_LEFT:
                    board, moves = board.move_left()
                    print moves
                elif event.key == c.K_UP:
                    board, moves = board.move_up()
                    print moves
                elif event.key == c.K_DOWN:
                    board, moves = board.move_down()
                    print moves
        for item in moves:
            fy, fx, dy, dx = item
            print fy,fx,dy,dx
        screen.fill((255, 255, 255))
        for a in range(1,4):
            for b in range(1,4):
                e = (80*a)-80
                f = (80*b)-80
                pygame.draw.rect(screen, (0,0,0), (e,f,80,80), 1)
        
        for i in range(0,3):
            j = 0
            for number in board.rows[i]:
                x = 80 * j + 2
                y = 80 * i + 2
                j += 1
                number = '%s' % number
                screen.blit(tile_images[number], (x, y))
        
        pygame.display.flip()
        clock.tick(60)
        moves = set()#to prevent a crazy loop

if __name__ == "__main__":
    main()

