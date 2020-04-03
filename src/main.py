import pygame
import sys
from settings import *


# Initialization
pygame.init()
pygame.mixer.init()

pygame.display.set_caption("Zombies!")
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()


# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)


