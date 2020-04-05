import pygame
from settings import *
from classes import *

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill(WHITE)

hello = TextObject("Hello", None, 50, 1, GREEN)
hello.draw(screen, (100, 100))

pygame.display.update()
pygame.time.delay(5000)