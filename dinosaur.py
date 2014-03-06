
import pygame, sys
from pygame import constants as c

def main():
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    dino = pygame.image.load('tyrannosaur.png')

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
                elif event.key == c.K_LEFT:
                    dx = -5
                elif event.key == c.K_UP:
                    dy = -5
                elif event.key == c.K_DOWN:
                    dy = 5

        x += dx
        y += dy

        screen.fill((255, 255, 255))
        screen.blit(dino, (x, y))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()

