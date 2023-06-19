import random
import pygame
from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet
from game.components.bullets.bullet_manager import BulletManager

from game.utils.constants import DEFAULT_TYPE, SPACESHIP_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP

class Spaceship(Sprite):
    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP, (60, 40))  # Carga y ajusta la imagen de la nave
        self.rect = self.image.get_rect()  # Obtiene el rectángulo delimitador de la nave
        self.rect.x = 520  # Posición inicial en el eje x
        self.rect.y = 500  # Posición inicial en el eje y
        self.type = SPACESHIP_TYPE  # Tipo de la nave
        self.power_up_type = DEFAULT_TYPE  # Tipo de power-up actual de la nave
        self.has_power_up = False  # Indicador de si la nave tiene un power-up activo
        self.power_up_time = 0  # Tiempo restante del power-up

    def move_left(self):
        self.rect.x -= 10  # Mueve la nave hacia la izquierda
        if self.rect.right < 0:
            self.rect.x = SCREEN_WIDTH  # Si la nave se sale por la izquierda, reaparece en la derecha

    def move_right(self):
        self.rect.x += 10  # Mueve la nave hacia la derecha
        if self.rect.left > SCREEN_WIDTH:
            self.rect.x = 0  # Si la nave se sale por la derecha, reaparece en la izquierda

    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= 10  # Mueve la nave hacia arriba

    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 50:
            self.rect.y += 10  # Mueve la nave hacia abajo

    def shoot_bullet(self, bullet_manager):
        bullet = Bullet(self)  # Crea una instancia de la clase Bullet asociada a la nave
        bullet_manager.add_bullet(bullet)  # Agrega la bala al administrador de balas del juego

    def update(self, user_input, game):
        if user_input[pygame.K_LEFT] or user_input[pygame.K_a]:
            self.move_left()  # Se mueve hacia la izquierda cuando se presiona la tecla "izquierda" o "a"

        if user_input[pygame.K_RIGHT] or user_input[pygame.K_d]:
            self.move_right()  # Se mueve hacia la derecha cuando se presiona la tecla "derecha" o "d"

        if user_input[pygame.K_UP] or user_input[pygame.K_w]:
            self.move_up()  # Se mueve hacia arriba cuando se presiona la tecla "arriba" o "w"

        if user_input[pygame.K_DOWN] or user_input[pygame.K_s]:
            self.move_down()  # Se mueve hacia abajo cuando se presiona la tecla "abajo" o "s"

        if user_input[pygame.K_SPACE]:
            self.shoot_bullet(game.bullet_manager)  # Dispara una bala cuando se presiona la tecla "espacio"

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))  # Dibuja la imagen de la nave en la posición actual

    def reset(self):
        self.rect.x = 520  # Restablece la posición inicial en el eje x
        self.rect.y = 500  # Restablece la posición inicial en el eje y

    def set_image(self, size=(40, 60), image=SPACESHIP):
        self.image = image
        self.image = pygame.transform.scale(self.image, size)  # Ajusta el tamaño de la imagen de la nave

