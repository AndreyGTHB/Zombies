import pygame
import math
from settings import *


class Player(pygame.sprite.Sprite):
    speed = PLAYER_SPEED
    shoot_interval = PLAYER_SHOOT_INTERVAL

    def __init__(self, img, position, bullets, clock):
        super(Player, self).__init__()

        self.center = position
        self.original_image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.rotate(pygame.image.load(img), 90).convert_alpha()
        self.rect = self.image.get_rect(center=self.center)

        self.x, self.y = self.rect.center
        self.direction = 90

        self.speed_x = 0
        self.speed_y = 0

        self.bullets = bullets
        self.time_to_shoot = self.shoot_interval
        self.clock = clock

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
        self.shooting()

        self.rotate_to_mouse_pointer()
        self.x += self.speed_x
        self.y += self.speed_y
        self.rect.move_ip(self.speed_x, self.speed_y)

        self.speed_x = 0
        self.speed_y = 0

    def rotate_to_mouse_pointer(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.rotate_to(mouse_x, mouse_y)

    def rotate_to(self, x, y):
        rel_x, rel_y = x - self.x, y - self.y
        angle = 180 / math.pi * -math.atan2(rel_y, rel_x)
        self.direction = angle - 90
        self.image = pygame.transform.rotate(self.original_image, int(angle))
        print(self.direction)
        self.rect = self.image.get_rect(center=self.rect.center)

    def shooting(self):
        clicks = pygame.mouse.get_pressed()
        if self.time_to_shoot > 0:
            self.time_to_shoot -= self.clock.get_time()
        elif clicks[0]:
            Bullet(BULLET_IMG, self).add(self.bullets)
            self.time_to_shoot = self.shoot_interval





class Bullet(pygame.sprite.Sprite):
    speed = BULLET_SPEED

    def __init__(self, img, player):
        super(Bullet, self).__init__()

        self.x, self.y = player.x, player.y

        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect(center=(self.x, self.y))

        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.DX, self.DY = self.mouse_x - self.x, self.mouse_y - self.y
        self.VL = math.sqrt(self.DX**2 + self.DY**2)
        self.VNX, self.VNY = self.DX/self.VL, self.DY/self.VL
        self.speed_x, self.speed_y = self.VNX * self.speed, self.VNY * self.speed

    def update(self):
        self.move()

        if self.x <= 0 or self.x >= SCREEN_WIDTH or self.y <= 0 or self.y >= SCREEN_HEIGHT:
            self.kill()

    def move(self):
        self.rect.move_ip(self.speed_x, self.speed_y)
        self.x += self.speed_x
        self.y += self.speed_y

