import pygame
from game.components.bullets.bullet_manager import BulletManager
from game.components.enemies.enemy_manager import EnemyManager
from game.components.final_menu import FinalMenu
from game.components.menu import Menu
from game.components.powerups.manager import Manager
from game.components.spaceship import Spaceship
from game.utils.constants import BG, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, SHIELD_TYPE, TITLE, FPS

class Game:
    def __init__(self):
        # Inicialización de pygame y configuración de la ventana del juego
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.score = 0
        self.death_count = 0
        self.max_score = 0

        # Componentes del juego
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.power_up_manager = Manager()

        # Menús del juego
        self.menu = Menu("Press any key [ ] to start")
        self.final_menu = FinalMenu()

    def run(self):
        # Bucle principal del juego
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu(self)

        pygame.display.quit()
        pygame.quit()

    def play(self):
        # Inicia una nueva partida
        self.playing = True
        self.score = 0
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        # Gestiona los eventos del juego
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Si se cierra la ventana, se detiene el juego
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.type == pygame.MOUSEBUTTONUP:
                    # Si se presiona la barra espaciadora o se hace clic con el ratón, la nave dispara un proyectil
                    self.player.shoot_bullet(self.bullet_manager)

    def update(self):
        # Actualiza los elementos del juego en cada iteración
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        self.power_up_manager.update(self)

    def draw(self):
        # Dibuja los elementos del juego en la pantalla
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_score()
        self.draw_shield_time()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        # Dibuja el fondo del juego
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:            
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def draw_score(self):
        # Dibuja la puntuación en la pantalla
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)

    def draw_shield_time(self):
        # Dibuja el tiempo restante del escudo en la pantalla
        if self.player.power_up_type == SHIELD_TYPE:
            font = pygame.font.Font(FONT_STYLE, 22)
            shield_time_text = font.render(f"Shield: {max(0, (self.player.power_up_time  - pygame.time.get_ticks()) // 1000)}", True, (255, 255, 255))
            shield_time_text_rect = shield_time_text.get_rect()
            shield_time_text_rect.center = (200, 50)
            self.screen.blit(shield_time_text, shield_time_text_rect)

    def show_menu(self, game):
        # Muestra el menú de inicio o el menú final según corresponda
        user_input = pygame.key.get_pressed()
        if self.death_count > 0:
            # Menú final
            self.menu.update_message(f"Final score is: {game.score} points" )
            self.final_menu.update(game)
            self.final_menu.draw(game.screen)
            self.final_menu.event(self.on_close, game.play)
            self.reset()
        else:
            # Menú de inicio
            self.menu.draw(game.screen)
            self.menu.event(self.on_close, game.play, user_input)

    def on_close(self):
        # Acción cuando se cierra la ventana
        self.playing = False
        self.running = False

    def reset(self):
        # Reinicia los componentes del juego para una nueva partida
        self.bullet_manager.reset()
        self.enemy_manager.reset()
        self.player.reset()

