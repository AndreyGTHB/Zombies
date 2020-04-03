import pygame
import sys
from settings import *
from classes import *


# initialization
pygame.init()
pygame.mixer.init()

pygame.display.set_caption("Zombies!")
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()


# sprites
player = Player(PLAYER_IMG)

# groups
all_objects = pygame.sprite.Group(player)


# main loop
over = False
frame = 0
while not over:
    frame += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            over = True
            sys.exit(0)

    print(f"ticking {frame}")
    screen.fill(BLUE)

    all_objects.update()
    all_objects.draw(screen)

    pygame.display.update()
    clock.tick(FPS)


