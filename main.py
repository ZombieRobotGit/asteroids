# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)


    asteroidField = AsteroidField()
    
    #player initialization must be after changing static filed "containers" value
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT/ 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for item in updatable:
            item.update(dt)
        
        for asteroid in asteroids:
            if asteroid.check_for_collision(player):
                print("Game over!")
                sys.exit()
            
            for shot in shots:
                if asteroid.check_for_collision(shot):
                    shot.kill()
                    asteroid.split()
                    
            


        screen.fill("black")

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        delta_time = game_clock.tick(60)
        dt = delta_time / 1000


if __name__ == "__main__":
    main()
