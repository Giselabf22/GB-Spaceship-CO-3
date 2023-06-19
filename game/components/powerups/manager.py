
import random
import pygame
from game.components.powerups.shield import Shield
from game.utils.constants import SPACESHIP, SPACESHIP_SHIELD


class Manager:

    def __init__(self):
        self.power_ups = []  # Lista de power-ups
        self.when_appears = random.randint(10000, 15000)  # Tiempo para la próxima aparición
        self.duration = 5000  # Duración del power-up de escudo
        self.shield_start_time = 0  # Tiempo de inicio del power-up de escudo

    def generate_power_up(self):
        shield = Shield()  # Crear instancia de Shield
        self.when_appears += random.randint(10000, 15000)  # Actualizar tiempo para la próxima aparición
        self.power_ups.append(shield)  # Agregar el power-up a la lista

    def update(self, game):
        current_time = pygame.time.get_ticks()

        # Generar power-up si no hay ninguno y ha pasado el tiempo de aparición
        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()

        # Actualizar power-ups existentes
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)

            # Colisión con el jugador
            if game.player.rect.colliderect(power_up):
                self.shield_start_time = pygame.time.get_ticks()  # Guardar tiempo de inicio
                game.player.power_up_type = power_up.type  # Establecer tipo de power-up
                game.player.has_power_up = True  # Activar bandera de power-up activo
                game.player.power_up_time = self.shield_start_time + self.duration  # Tiempo de duración del power-up
                game.player.set_image((70, 50), SPACESHIP_SHIELD)  # Cambiar imagen del jugador al escudo
                self.power_ups.remove(power_up)  # Eliminar power-up de la lista

            # Desactivar power-up si ha pasado el tiempo de duración
            if game.player.has_power_up and current_time >= game.player.power_up_time:
                game.player.has_power_up = False  # Desactivar bandera de power-up activo
                game.player.power_up_type = None  # Restablecer tipo de power-up
                game.player.set_image((60, 40), SPACESHIP)  # Cambiar imagen del jugador al sprite normal
                game.player.shield_start_time = 0  # Restablecer tiempo de inicio del power-up de escudo

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)  # Dibujar power-ups en la pantalla

    def reset(self):
        now = pygame.time.get_ticks()
        self.power_ups = []  # Reiniciar lista de power-ups
        self.when_appears = random.randint(now + 10000, now + 15000)  # Generar nuevo tiempo de aparición


