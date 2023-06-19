import random
from pygame.sprite import Sprite
from game.utils.constants import SCREEN_HEIGHT

class PowerUp(Sprite):
    def __init__(self, image, type):
        # Inicializar el power-up con su imagen y tipo
        self.image = image
        self.type = type

        # Obtener el rectángulo que define la posición y tamaño del power-up
        self.rect = self.image.get_rect()

        # Establecer la posición inicial del power-up de forma aleatoria en el rango entre 120 y la altura de la pantalla menos 120
        self.rect.x = random.randint(120, SCREEN_HEIGHT - 120)
        self.rect.y = 0

        # Tiempo de inicio del power-up
        self.start_time = 0

    def update(self, speed, power_ups):
        # Actualizar la posición del power-up según la velocidad proporcionada
        self.rect.y += speed

        # Verificar si el power-up ha salido de la pantalla
        if self.rect.y < 0 or self.rect.y >= SCREEN_HEIGHT:
            # Remover el power-up de la lista de power-ups
            power_ups.remove(self)

    def draw(self, screen):
        # Dibujar la imagen del power-up en la pantalla en la posición especificada por el rectángulo
        screen.blit(self.image, self.rect)

        
