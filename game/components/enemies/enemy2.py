import pygame
import random
from pygame.sprite import Sprite

from game.utils.constants import ENEMY_2, ENEMY_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH


UP = 'up'  # Definición de constantes
DOWN = 'down'


class Enemy2(Sprite):  # Definición de clase
    MOVEMENTS = [UP, DOWN]  # Lista que contiene los posibles movimientos del enemigo
    X_POS_LIST = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550]  # Posibles posiciones en el eje X donde un enemigo puede aparecer en la pantalla
    Y_POS = 20
    SPEED_X = 5
    SPEED_Y = 0.5


    def __init__(self):
        self.image = pygame.transform.scale(ENEMY_2, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.type = ENEMY_TYPE

        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y

        self.movement = random.choice(self.MOVEMENTS)
        self.move_y = random.randint(30, 100)  # Establece un número de movimientos que se van a hacer.
        self.moving_index = 0  # Esta variable se utiliza para realizar un seguimiento de la cantidad de movimientos que ha realizado el enemigo en una dirección específica. Se incrementará a medida que el enemigo se mueva y se reiniciará cuando alcance el valor de self.move_y.


    def update(self, ships):
        self.rect.y += self.speed_y

        if self.movement == UP:
            self.rect.y -= self.speed_y * 0.5  # Movimiento en medio cuadro hacia arriba
        else:
            self.rect.y += self.speed_y * 0.5  # Movimiento en medio cuadro hacia abajo

        self.update_movement()
        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)

    def update_movement(self):
        self.moving_index += 1
        if self.rect.y >= SCREEN_HEIGHT - 50:
            self.movement = UP
        elif self.rect.y <= 0:
            self.movement = DOWN

        if self.moving_index >= self.move_y:
            self.moving_index = 0
            self.movement = UP if self.movement == DOWN else DOWN

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
