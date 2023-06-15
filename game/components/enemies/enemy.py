import pygame   #importaciones
import random
from pygame.sprite import Sprite

from game.utils.constants import ENEMY_1, ENEMY_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH 


LEFT = 'left'  #definicion de constantes
RIGHT = 'right'
class Enemy(Sprite):   #definicion de clase La clase Enemy hereda de Sprite, lo que significa que es una entidad visual que se puede dibujar en la pantalla del juego.
    MOVEMENTS = [LEFT, RIGHT]   #lista que contiene posibles movimientos del enemigo
    X_POS_LIST = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550] #posibles posiciones en el eje X donde un enemigo puede aparecer en la pantalla
    Y_POS = 20
    SPEED_X = 5
    SPEED_Y = 1

    def __init__(self):
        self.image = pygame.transform.scale(ENEMY_1, (50,50))
        self.rect = self.image.get_rect() #se utiliza para obtener un objeto Rect que representa el área ocupada por la imagen del enemigo, lo que facilita el posicionamiento y la detección de colisiones en el juego.
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.type = ENEMY_TYPE

        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y

        self.movement = random.choice(self.MOVEMENTS)
        self.move_x = random.randint(30, 100) #establece un numero de movimientos que se van a hacer.
        self.moving_index = 0 #Esta variable se utiliza para realizar un seguimiento de la cantidad de movimientos que ha realizado el enemigo en una dirección específica. Se incrementará a medida que el enemigo se mueva y se reiniciará cuando alcance el valor de self.move_x.
        self.shooting_time =  random.randint()

    def update(self, ships, game): #metodo  se encarga de actualizar la posición y el movimiento del enemigo en cada fotograma del juego.
        self.rect.y += self.speed_y
        self.shoot(game.bullet_manager)

        if self.movement == LEFT:
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x
        
        self.update_movement()
        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)

    def update_movement(self): 
        self.moving_index += 1
        if self.rect.x >= SCREEN_WIDTH - 50:
            self.movement = LEFT
        elif self.rect.x <= 0:
            self.movement_index = RIGHT

        if self.moving_index >= self.move_x:
            self.moving_index = 0
            self.movement = LEFT if self.movement == RIGHT else RIGHT #operador ternario

    def draw(self, screen): #Este método se encarga de dibujar el enemigo en la pantalla del juego.
        screen.blit(self.image, (self.rect.x, self.rect.y))   #screen es un argumento
#blit de pygame para dibujar la imagen del enemigo en la posición definida por self.rect.x y self.rect.y.

        # "argumento" se refiere a los valores que se pasan a un método o función cuando se llama a ese método o función. Los argumentos proporcionan información o datos necesarios para que el método o función realice ciertas operaciones.

    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.shooting_time += random.randint(30, 50)
