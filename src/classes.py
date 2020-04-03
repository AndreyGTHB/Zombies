import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, screen, clock, img):
        super(Player, self).__init__()

        self.screen = screen
        self.clock = clock

        self.__img = pygame.image.load(img)
        self.rect = self.get_img().get_rect()
        self.centerx = SCREEN_HEIGHT / 2
        self.centery = SCREEN_WIDTH / 2

    def get_img(self):
        return self.__img



