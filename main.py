#main.py

from src.game import Game
import pygame
from settings import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game = Game(screen)

    clock = pygame.time.Clock()

    while game.running:
        game.handle_events()
        dt = clock.tick(FPS)
        game.update(dt)
        game.draw()
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
