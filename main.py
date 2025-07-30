import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # start pygame
    pygame.init 

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # containers
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)


    # setup    
    running = True
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    dt = 0

    # game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # update
        updatable.update(dt)
        
        # collision check
        for asteroid in asteroids:
            if asteroid.collision(player):
                print('Game over!')
                running = False

        # draw
        screen.fill('black')
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
        
        

if __name__ == "__main__":
    main()
