from time import sleep

import pygame
import sys
from threading import Timer
from settings import *
from classes import *

# initialization
pygame.init()
pygame.mixer.init()
over = False

pygame.display.set_caption("Zombies!")
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

# groups
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
zombies = pygame.sprite.Group()

# objects
player = Player(PLAYER_IMG, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), bullets, all_sprites, clock)
player.add(all_sprites)
evt = EvacuationText(None, 46, clock, GAME_TIME * 1000)
evt.add(all_sprites)
evsh = None

evacuation = False


num_of_zombies = 0
zombie_spawning_time = 2.5
zombie_timer = None
decrement_spawning_timer = None


def check_collision(group1, group2, dokill=False):
    answer = False
    for sprite1 in group1:
        for sprite2 in group2:
            grouped = pygame.sprite.Group(sprite2)
            if pygame.sprite.spritecollideany(sprite1, grouped):
                if dokill:
                    sprite1.kill()
                    sprite2.kill()
                answer = True
                break
    return answer


def decrement_spawning_time():
    global zombie_spawning_time
    global decrement_spawning_timer

    if over:
        return

    if zombie_spawning_time > 0.5:
        zombie_spawning_time -= 0.5
    elif zombie_spawning_time > 0.4:
        Zombie.speed = 3
        zombie_spawning_time -= 0.1
    else:
        return

    decrement_spawning_timer = Timer(NEXT_LEVEL, decrement_spawning_time)
    decrement_spawning_timer.start()


def spawn_zombie():
    global zombie_timer
    if over:
        return
    Zombie(ZOMBIE_IMG, player, bullets).add(all_sprites, zombies)
    zombie_timer = Timer(zombie_spawning_time, spawn_zombie)
    zombie_timer.start()


# main loop
decrement_spawning_time()
spawn_zombie()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            zombie_timer.cancel()
            decrement_spawning_timer.cancel()
            sys.exit()

    screen.fill(WHITE)

    if evt.time <= 0 and not evacuation and not over:
        evsh = EvacuationShip(SHIP_IMG, player, all_sprites)
        evacuation = True
    elif evacuation:
        collided = evsh.check_collision()
        if collided:
            evsh.evac = True
            player.kill()
            for sprite in all_sprites:
                if type(sprite) is not EvacuationShip:
                    sprite.kill()
            win = TextObject("You escaped!!", None, 100, 1, GREEN)
            win.add(all_sprites)
            win.draw(screen, (SCREEN_WIDTH/2 - 30, SCREEN_HEIGHT/2 + 50))
            over = True

    check_collision(bullets, zombies, True)

    if pygame.sprite.spritecollideany(player, zombies):
        for spr in all_sprites:
            spr.kill()
        lose = TextObject('You lost!!', None, 100, 1, RED)
        lose.add(all_sprites)
        lose.draw(screen, (SCREEN_WIDTH/2 - 30, SCREEN_HEIGHT/2 + 50))
        over = True

    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.update()
    clock.tick(FPS)
