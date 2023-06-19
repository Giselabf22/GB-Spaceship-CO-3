import random
import pygame
from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet
from game.components.bullets.bullet_manager import BulletManager

from game.utils.constants import DEFAULT_TYPE, SPACESHIP_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP

class Spaceship(Sprite):

    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP, (60, 40))
        self.rect = self.image.get_rect()
        self.rect.x = 520
        self.rect.y = 500
        self.type = SPACESHIP_TYPE
        self.power_up_type = DEFAULT_TYPE
        self.has_power_up = False
        self.power_up_time = 0
     
        

    def move_left(self):
        self.rect.x -= 10
        if self.rect.right < 0:
            self.rect.x = SCREEN_WIDTH

    def move_right(self):
        self.rect.x += 10
        if self.rect.left > SCREEN_WIDTH:
            self.rect.x = 0

    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= 10

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 50:
            self.rect.y += 10

    def shoot_bullet(self, bullet_manager):
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)

    def update(self, user_input, game):

        if user_input[pygame.K_LEFT] or user_input[pygame.K_a]:
            self.move_left()

        if user_input[pygame.K_RIGHT] or user_input[pygame.K_d]:
            self.move_right()

        if user_input[pygame.K_UP] or user_input[pygame.K_w]:
            self.move_up()

        if user_input[pygame.K_DOWN] or user_input[pygame.K_s]:
            self.move_down()
        
        if user_input[pygame.K_SPACE]:
            self.shoot_bullet(game.bullet_manager)


    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
    def reset(self):
        self.rect.x = 520
        self.rect.y = 500

    def set_image(self, size= (40, 60), image = SPACESHIP):
        self.image = image
        self.image = pygame.transform.scale(self.image, size)

