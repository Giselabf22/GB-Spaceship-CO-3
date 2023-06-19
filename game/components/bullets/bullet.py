import pygame
from pygame.sprite import Sprite

from game.utils.constants import BULLET, BULLET_ENEMY, SPACESHIP_TYPE, ENEMY_TYPE, SCREEN_HEIGHT

class Bullet(Sprite):

    SPEED = 20  # Velocidad de la bala
    ENEMY_BULLET_IMG = pygame.transform.scale(BULLET_ENEMY, (9, 32))  # Imagen de la bala enemiga escalada
    SPACESHIP_BULLET = pygame.transform.scale(BULLET, (9, 32))  # Imagen de la bala del jugador escalada

    # Diccionario que asigna las imágenes de las balas según el tipo de propietario
    BULLETS = {
        ENEMY_TYPE: ENEMY_BULLET_IMG,
        SPACESHIP_TYPE: SPACESHIP_BULLET,
    }

    def __init__(self, spaceship):
        self.image = self.BULLETS[spaceship.type]  # Obtener la imagen de la bala según el tipo de propietario
        self.rect = self.image.get_rect()
        self.rect.center = spaceship.rect.center  # Posicionar la bala en el centro del propietario
        self.owner = spaceship.type  # Almacenar el tipo de propietario de la bala

    def update(self, bullets):
        if self.owner == ENEMY_TYPE:
            self.rect.y += self.SPEED  # Mover la bala enemiga hacia abajo
            if self.rect.y >= SCREEN_HEIGHT:  # Si la bala sale de la pantalla
                bullets.remove(self)  # Eliminar la bala de la lista de balas
                
        elif self.owner == SPACESHIP_TYPE:
            self.rect.y -= self.SPEED  # Mover la bala del jugador hacia arriba
            if self.rect.y <= 0:  # Si la bala sale de la pantalla
                bullets.remove(self)  # Eliminar la bala de la lista de balas

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))  # Dibujar la imagen de la bala en la pantalla

