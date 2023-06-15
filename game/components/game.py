import pygame
from game.components.enemies.enemy_manager import EnemyManager
from game.components.bullets.bullet_manager import BulletManager
from game.components.spaceship import Spaceship

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE #lo que no se esta usando se ve de un color mas opaco


class Game:
    def __init__(self):
        pygame.init() #para inicializar todo lo que necesita pygame
        pygame.display.set_caption(TITLE) #display muestra algo en pantalla
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  #aqui se le pasa ancho y alto
        self.clock = pygame.time.Clock() #clock nos ayuda a definir la cantidad de frames por segundo
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0   #bg es el back ground
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager() 
        self.bullet_manager = BulletManager()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.display.quit()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed() #da como un diccionario de todas las teclas y lo que se ha presionado da un valor
        self.player.update(user_input)
        self.enemy_manager.update(self)
        self.bullet_manager.update()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255)) #fill rellena de un color la pantalla
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        pygame.display.update() #estos dos sirven para que el usuario note los cambios
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg)) #blit permite dibujar imagenes en pantalla
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed
