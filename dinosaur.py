
import pygame, sys
from pygame import constants as c

# Shell script for converting images:
# for filename in *.ico; do name=$(basename $filename .ico);
# convert $name.ico -type truecolormatte PNG32:$name.png;
# mv $name-0.png $name.png; rm *-[12345].png; done

def main():
    screen = pygame.display.set_mode((800, 800))
    clock = pygame.time.Clock()
    dino = pygame.image.load('tyrannosaur.png')
    piece_images = {}
    for color, method in ('White', str.upper), ('Black', str.lower):
        for letter, name in zip('pnbrkq', ['Pawn', 'Knight', 'Bishop', 'Rook',
                                           'King', 'Queen']):
            filename = 'Chess Icons/{}_{}.png'.format(color, name)
            image = pygame.image.load(filename)
            image = image.convert_alpha()
            image = pygame.transform.smoothscale(image, (76, 76))
            piece_images[method(letter)] = image

    glyphs = {
        'K': pygame.image.load('Chess Icons/Black_King.png'),
        }

    x = 200
    y = 200
    dx = 0
    dy = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == c.KEYDOWN:
                if event.key == c.K_ESCAPE:
                    sys.exit(0)

                # NEW:
                elif event.key == c.K_RIGHT:
                    dx = 5
                    dy = 0
                elif event.key == c.K_LEFT:
                    dx = -5
                    dy = 0 
                elif event.key == c.K_UP:
                    dy = -5
                    dx = 0
                elif event.key == c.K_DOWN:
                    dy = 5
                    dx = 0 
        #x += dx
        #y += dy
        
        
        screen.fill((255, 255, 255))
            
        for i in range(1,9):
            for j in range(1,9):
                filled = (i + j) % 2
                pygame.draw.rect(screen, (0,0,0), ((80*i)-80,(80*j)-80,80,80), not filled)
        # pygame.display.update()
    
        #screen.blit(dino, (x, y))
        row = 'rnbqkbnr'
        for i, letter in enumerate(row):
            x = 80 * i + 2
            y = 0 + 2
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

        pygame.display.flip()
        clock.tick(60)
        #dx = dy = 0

if __name__ == "__main__":
    main()

