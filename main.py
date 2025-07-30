import pygame
from constants import *


def main():
    # start pygame
    pygame.init 
    running = True  

    # Welcome message
    print('Starting Asteroids!')
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # create main window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')
        pygame.display.flip()

if __name__ == "__main__":
    main()
