import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    speed = 5

    def __init__(self, img, position):
        super(Player, self).__init__()

        self.center = position
        self.start_image = pygame.transform.rotate(pygame.image.load(img), -90)
        self.image = pygame.image.load(PLAYER_IMG)
        self.rect = self.image.get_rect(center=self.center)

        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and not self.rect.top <= 0:
            self.rotate(180)
            self.speed_y -= self.speed
        if keys[pygame.K_DOWN] and not self.rect.bottom >= SCREEN_HEIGHT:
            self.rotate(0)
            self.speed_y += self.speed
        if keys[pygame.K_RIGHT] and not self.rect.right >= SCREEN_WIDTH:
            self.rotate(90)
            self.speed_x += self.speed
        if keys[pygame.K_LEFT] and not self.rect.left <= 0:
            self.rotate(-90)
            self.speed_x -= self.speed

        self.rect.move_ip(self.speed_x, self.speed_y)

        self.speed_x = 0
        self.speed_y = 0

    def rotate(self, degrees):
        self.image = pygame.transform.rotate(self.start_image, degrees)
        self.rect = self.image.get_rect(center=self.rect.center)





