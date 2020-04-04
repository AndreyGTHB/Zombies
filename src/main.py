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


# objects
player = Player(PLAYER_IMG, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

# groups
sprites = pygame.sprite.Group(player)
bullets = pygame.sprite.Group(Bullet(BULLET_IMG, player))


# main loop
over = False
while not over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            over = True
            sys.exit()
    clicks = pygame.mouse.get_pressed()
    if clicks[0]:
        bullets.add(Bullet(BULLET_IMG, player))

    screen.fill(WHITE)

    sprites.update()
    bullets.update()
    sprites.draw(screen)
    bullets.draw(screen)

    pygame.display.update()
    clock.tick(FPS)


