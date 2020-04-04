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


def check_collision(group1, group2, dokill=False) -> bool:
    for sprite in group1:
        pygame.sprite.spritecollide(sprite, group2, dokill=dokill)
        return True
    return False


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

    check_collision(bullets, zombies, True)

    sprites.update()
    bullets.update()
    zombies.update()

    sprites.draw(screen)
    bullets.draw(screen)
    zombies.draw(screen)

    pygame.display.update()
    clock.tick(FPS)


