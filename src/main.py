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
player = Player(PLAYER_IMG, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

# groups
all_sprites = pygame.sprite.Group(player)


# main loop
over = False
while not over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            over = True
            sys.exit()

    screen.fill(WHITE)

    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.update()
    clock.tick(FPS)


