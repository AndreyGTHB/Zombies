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


# groups
sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
zombies = pygame.sprite.Group()

# objects
player = Player(PLAYER_IMG, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2), bullets, clock)
player.add(sprites)
zombies.add(Zombie(ZOMBIE_IMG, player, bullets))


pygame.time.set_timer(pygame.USEREVENT, 2000)


def check_bul_collision(group1, group2):
    for sprite1 in group1:
        for sprite2 in group2:
            grouped = pygame.sprite.Group(sprite2)
            if pygame.sprite.spritecollideany(sprite1, grouped):
                sprite1.kill()
                sprite2.kill()
                break


# main loop
over = False
while not over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            over = True
            sys.exit()
        elif event.type == pygame.USEREVENT:
            zombies.add(Zombie(ZOMBIE_IMG, player, bullets))

    screen.fill(WHITE)

    check_bul_collision(bullets, zombies)

    sprites.update()
    bullets.update()
    zombies.update()

    sprites.draw(screen)
    bullets.draw(screen)
    zombies.draw(screen)

    pygame.display.update()
    clock.tick(FPS)


