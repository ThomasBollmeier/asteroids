# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    fps = 60 # frames per second

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)
    
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)
        for a in asteroids:
            hit = False
            for s in shots:
                if a.collides_with(s):
                    a.split()
                    hit = True
                    s.kill()
                    break
            if hit:
                continue
            if player.collides_with(a):
                print("Game over!")
                return
        pygame.display.flip()
        dt = clock.tick(fps) / 1000

if __name__ == "__main__":
    main()
