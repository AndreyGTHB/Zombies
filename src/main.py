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
evt = EvacuationText(None, 46, clock, 35000)
evt.add(all_sprites)
evsh = None

evacuation = False


num_of_zombies = 0
zombie_spawning_time = 2.5
zombie_timer = None
decrement_spawning_timer = None


def check_collision(group1, group2):
    for sprite1 in group1:
        for sprite2 in group2:
            grouped = pygame.sprite.Group(sprite2)
            if pygame.sprite.spritecollideany(sprite1, grouped):
                sprite1.kill()
                sprite2.kill()
                break


def decrement_spawning_time():
    global zombie_spawning_time
    global decrement_spawning_timer

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
while not over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            zombie_timer.cancel()
            decrement_spawning_timer.cancel()
            sys.exit()

    screen.fill(WHITE)

    if evt.time <= 0 and not evacuation:
        evsh = EvacuationShip(SHIP_IMG, player, all_sprites)
        evacuation = True
    elif evacuation:
        collided = evsh.check_collision()
        if collided:
            player.kill()
            for sprite in all_sprites:
                sprite.kill()
            win = TextObject("You escaped!!", None, 100, 1, GREEN)
            win.draw(screen, (SCREEN_WIDTH/2 - 60, SCREEN_HEIGHT/2 + 50))

    check_collision(bullets, zombies)

    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.update()
    clock.tick(FPS)
