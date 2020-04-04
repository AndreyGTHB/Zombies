import pygame
import math
from settings import *


class Player(pygame.sprite.Sprite):
    speed = 5

    def __init__(self, img, position):
        super(Player, self).__init__()

        self.center = position
        self.original_image = pygame.image.load(img)
        self.image = pygame.transform.rotate(pygame.image.load(img), 90)
        self.rect = self.image.get_rect(center=self.center)

        self.x, self.y = self.rect.center

        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and not self.rect.top <= 0:
            self.speed_y -= self.speed
        if keys[pygame.K_s] and not self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y += self.speed
        if keys[pygame.K_d] and not self.rect.right >= SCREEN_WIDTH:
            self.speed_x += self.speed
        if keys[pygame.K_a] and not self.rect.left <= 0:
            self.speed_x -= self.speed

        self.rotate_to_mouse_pointer()
        self.x += self.speed_x
        self.y += self.speed_y
        self.rect.move_ip(self.speed_x, self.speed_y)

        self.speed_x = 0
        self.speed_y = 0

    def rotate_to_mouse_pointer(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
        angle = 180/math.pi * -math.atan2(rel_y, rel_x)
        self.image = pygame.transform.rotate(self.original_image, int(angle))
        self.rect = self.image.get_rect(center=self.rect.center)






