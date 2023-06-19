import pygame
from game.utils.constants import FONT_STYLE, GAME_OVER, SCREEN_HEIGHT, SCREEN_WIDTH

class FinalMenu:
    # Definición de constantes para la mitad del ancho y alto de la pantalla
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
 
    def __init__(self):
        # Inicialización de la clase FinalMenu
        # Carga de la fuente 'superbrigade.ttf' y establecimiento del tamaño de fuente en 30
        self.font = pygame.font.Font('game/assets/font/superbrigade.ttf', 30)
        
        # Escalado de la imagen del juego terminado (GAME_OVER) a un tamaño de 500x200
        self.game_over = pygame.transform.smoothscale(GAME_OVER, (500, 200))

        # Obtención del rectángulo que define la posición y tamaño de la imagen del juego terminado
        self.game_over_rect = self.game_over.get_rect()
        self.game_over_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT - 100)
        
        # Carga de la fuente definida en FONT_STYLE y establecimiento del tamaño de fuente en 20
        self.decision_font = pygame.font.Font(FONT_STYLE, 20)
        
        # Renderizado del mensaje de decisión con la fuente, texto, color y sombreado
        self.decision = self.decision_font.render("Press  [SPACE]  to Reset Game  |  Press  [ENTER]  to Exit the Game", True, (255, 0, 0))
        
        # Obtención del rectángulo que define la posición y tamaño del mensaje de decisión
        self.decision_rect = self.decision.get_rect()
        self.decision_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 150)
        
        self.max_score_value = 0

    def event(self, on_close, on_start):
        # Manejo de eventos de la interfaz
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN):
                on_close()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                on_start()

    def update(self, game):
        # Actualización de la puntuación máxima
        if game.score > self.max_score_value:
            self.max_score_value = game.score

        # Renderizado del mensaje de puntuación máxima con la fuente, texto y color
        self.max_score_message = self.font.render(f"The highest score is: {self.max_score_value} points", True, (255, 255, 255))
        
        # Obtención del rectángulo que define la posición y tamaño del mensaje de puntuación máxima
        self.max_score_message_rect = self.max_score_message.get_rect()
        self.max_score_message_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 50)

    def draw(self, screen):
        # Dibujado de la interfaz en la pantalla
        screen.fill((0, 0, 0))
        screen.blit(self.max_score_message, self.max_score_message_rect)
        screen.blit(self.game_over, self.game_over_rect)
        screen.blit(self.decision, self.decision_rect)
        pygame.display.update()


        