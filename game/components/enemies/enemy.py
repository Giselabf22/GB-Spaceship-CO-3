import math
import pygame
import random
from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet

from game.utils.constants import ENEMY_1, ENEMY_2, ENEMY_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH

LEFT = 'left'
RIGHT = 'right'

class Enemy(Sprite):
    X_POS_LIST = [20, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900]
    Y_POS = -5
    SPEED_X = 5
    SPEED_Y = 1
    MOVEMENTS = [LEFT, RIGHT]

    def __init__(self,enemy):

        self.image = pygame.transform.scale(enemy,(50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.type = ENEMY_TYPE

        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y
        self.enemy = enemy
        self.movement = random.choice(self.MOVEMENTS)
        self.move_x = random.randint(30, 100)
        self.moving_index = 0
        self.shooting_time = random.randint(30,50)
        self.amplitude = 30  # Amplitud del movimiento
        self.frequency = 0.01

    def update(self, ships, game):

        self.rect.y += self.speed_y
        self.shoot(game.bullet_manager)

        if self.enemy == ENEMY_2:
            
            if self.movement == LEFT:
                self.rect.x -= 10
                self.rect.y = self.amplitude * math.sin(self.frequency * self.rect.x)
            else:
                self.rect.x += 10
                self.rect.y = self.amplitude * math.sin(self.frequency * self.rect.x)
        
        else:
            if self.movement == LEFT:
                self.rect.x -= self.speed_x
            else:
                self.rect.x += self.speed_x
        
        self.update_movement()

        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)

    def update_movement(self):

        self.moving_index += 1
        if self.rect.x > SCREEN_WIDTH - 50:
            self.movement = LEFT
        elif self.rect.x <= 0:
            self.movement = RIGHT
            
        if self.moving_index >= self.move_x:
            self.moving_index = 0
            self.movement = LEFT if self.movement == RIGHT else RIGHT
            # if self.movement == RIGHT:
            #     self.movement = LEFT
            # else:
            #     self.movement = RIGHT
            

    def draw (self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.shooting_time += random.randint(30, 50)

