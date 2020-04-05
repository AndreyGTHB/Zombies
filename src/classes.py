from random import randint

import pygame
import math
from settings import *


class Interacted:
    def rotate_to(self, x, y):
        raise NotImplementedError("Method 'rotate_to' of interface 'Interacted' must be override.")


class Player(pygame.sprite.Sprite, Interacted):
    speed = PLAYER_SPEED
    shoot_interval = PLAYER_SHOOT_INTERVAL

    def __init__(self, img, position, all_sprites,  bullets, clock):
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
        self.all_sprites = all_sprites

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
        self.rect = self.image.get_rect(center=self.rect.center)

    def shooting(self):
        clicks = pygame.mouse.get_pressed()
        if self.time_to_shoot > 0:
            self.time_to_shoot -= self.clock.get_time()
        elif clicks[0]:
            Bullet(BULLET_IMG, self).add(self.all_sprites, self.bullets)
            self.time_to_shoot = self.shoot_interval




class Bullet(pygame.sprite.Sprite):
    speed = BULLET_SPEED

    def __init__(self, img, player):
        super(Bullet, self).__init__()

        self.x, self.y = player.x, player.y

        self.image = pygame.image.load(img).convert_alpha()
        self.image.set_colorkey((255, 255, 255))
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
        self.x += self.speed_x
        self.y += self.speed_y
        self.rect.center = (self.x, self.y)




class Zombie(pygame.sprite.Sprite, Interacted):
    speed = ZOMBIE_SPEED

    def __init__(self, img, player, bullets):
        super(Zombie, self).__init__()

        self.original_image = pygame.image.load(img).convert_alpha()
        self.image = self.original_image.copy()

        chance = randint(1, 4)
        if chance == 1:
            self.rect = self.image.get_rect()
        elif chance == 2:
            self.rect = self.image.get_rect(center=(SCREEN_WIDTH, 0))
        elif chance == 3:
            self.rect = self.image.get_rect(center=(0, SCREEN_HEIGHT))
        else:
            self.rect = self.image.get_rect(center=(SCREEN_WIDTH, SCREEN_HEIGHT))

        self.player = player
        self.bullets = bullets

        self.direction = 90
        self.x, self.y = self.rect.center

        self.DX, self.DY = self.player.x - self.x, self.player.y - self.y
        self.VL = math.sqrt(self.DX ** 2 + self.DY ** 2)
        self.VNX, self.VNY = self.DX / self.VL, self.DY / self.VL
        self.speed_x, self.speed_y = self.VNX * self.speed, self.VNY * self.speed

    def update(self):
        self.rotate_to(self.player.x, self.player.y)
        self.update_speed()
        self.move()

    def rotate_to(self, x, y):
        rel_x, rel_y = x - self.x, y - self.y
        angle = 180 / math.pi * -math.atan2(rel_y, rel_x)
        self.direction = angle - 90
        self.image = pygame.transform.rotate(self.original_image, int(angle))
        self.rect = self.image.get_rect(center=self.rect.center)

    def update_speed(self):
        DX, DY = self.player.x - self.x, self.player.y - self.y
        VL = math.sqrt(DX ** 2 + DY ** 2)
        VNX, VNY = DX / VL, DY / VL
        self.speed_x, self.speed_y = VNX * self.speed, VNY * self.speed

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.rect.center = (self.x, self.y)




class TextObject():
    def __init__(self, text, font=None, size=30, smoothing=0, colour=BLACK):
        self.font = pygame.font.SysFont(font, size)
        self.image = self.font.render(text, smoothing, colour)
        self.rect = self.image.get_rect()

    def draw(self, screen, position):
        self.rect.center = position
        screen.blit(self.image, self.rect)


class EvacuationText(TextObject, pygame.sprite.Sprite):
    def __init__(self, font, size, clock, time):
        pygame.sprite.Sprite.__init__(self)
        TextObject.__init__(self, f"Evacuation through: {time}", font, size, 1, RED)

        self.time = time
        self.clock = clock

    def update(self):
        self.time -= self.clock.get_time()
        self.image = self.font.render(f"Evacuation through: {self.time//1000}", 1, RED)
        self.rect = self.image.get_rect(center=(350, 45))




