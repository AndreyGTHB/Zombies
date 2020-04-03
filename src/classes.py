import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    speed = 9

    def __init__(self, img):
        super(Player, self).__init__()

        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.center = (0, 0)

        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and not self.rect.bottom - self.rect.height <= 0:
            self.speed_y -= self.speed
        if keys[pygame.K_DOWN]:
            self.speed_y += self.speed
        if keys[pygame.K_RIGHT]:
            self.speed_x += self.speed
        if keys[pygame.K_LEFT]:
            self.speed_x -= self.speed

        self.rect.move_ip(self.speed_x, self.speed_y)

        self.speed_x = 0
        self.speed_y = 0





