import pygame


SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT) = (840, 680)
FPS = 60

# game time
GAME_TIME = 60

# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# imagines
PLAYER_IMG = pygame.image.load("../resources/player.png")
BULLET_IMG = pygame.image.load("../resources/bullet.png")
ZOMBIE_IMG = pygame.image.load("../resources/zomb.png")
SHIP_IMG = pygame.image.load("../resources/ev_ship.png")

# constants
PLAYER_SHOOT_INTERVAL = 450

PLAYER_SPEED = 4
BULLET_SPEED = 14
ZOMBIE_SPEED = 4
SHIP_SPEED = 8

NEXT_LEVEL = 10

ZOMBIE_EVENT = 8


