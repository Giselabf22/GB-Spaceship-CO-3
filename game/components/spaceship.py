import pygame
from pygame.sprite import Sprite      #aqui va a estar la clase de la nave

from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP 


class Spaceship(Sprite):#entre los parentesis se pone la clase de la que se quiere heredar
     def __init__(self):
         self.image = pygame.transform.scale(SPACESHIP, (60, 40))#aqui se modifica el ancho y el alto de la nave
         self.rect = self.image.get_rect()
         self.rect.x = 520
         self.rect.y = 500

     def update(self, user_input):
         if user_input[pygame.K_LEFT]:
             self.move_left()
         elif user_input[pygame.K_RIGHT]:
             self.move_right()
         elif user_input[pygame.K_UP]:
             self.move_up()
         elif user_input[pygame.K_DOWN]:
             self.move_down()

     def move_left(self):
         self.rect.x -= 10
         if self.rect.right < 0:  # SI LA NAVE ESTA LOCALIZADA EN 0 SOBRE EL EJE X SU LOCALIZACION SERA IGUAL AL ANCHO DE LA PANTALLA
             self.rect.left = SCREEN_WIDTH
     def move_right(self):
         self.rect.x +=10
         if self.rect.left > SCREEN_WIDTH:  #SI LA NAVE ESTA LOCALIZADA AL TOTAL DEL ANCHO EN EL EJE X SU NUEVA LOCALIZACION SERA IGUAL A 0
             self.rect.right = 0
     def move_up(self):
         if self.rect.y > SCREEN_HEIGHT //2:
             self.rect.y -=10
        
     def move_down(self):
         if self.rect.y < SCREEN_HEIGHT - 50:
             self.rect.y +=10
            
     
     def draw(self, screen):
         screen.blit(self.image, (self.rect.x, self.rect.y)) #blit se usa para dibujar imagenes