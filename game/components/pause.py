import pygame

from game.utils.constants import FONT_STYLE, GAME_OVER, SCREEN_HEIGHT, SCREEN_WIDTH

class Pause:

    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
 
    def __init__(self):
        self.font_title = pygame.font.Font(FONT_STYLE , 80)
        self.title = self.font_title.render("PAUSE", True, (0, 0, 0))
        self.font_title_rect = self.title.get_rect()
        self.font_title_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT )
       
        self.font = pygame.font.Font(FONT_STYLE, 15)
        self.options  = self.font.render("Press  [SPACE]  to Continue the Game  |  Press  [RETURN]  to Exit the Game", True, (255, 255, 0))
        self.options_rect = self.options.get_rect()
        self.options_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 150)
    
    def event(self, on_close, on_start):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.key == pygame.K_RETURN:
                on_close()
                pygame.quit()
                quit()
            if event.key == pygame.K_SPACE:
                on_start()
        

    def update(self, game):
        self.score = self.font.render(f"The highest score is: {self.score} points", True, (255, 255, 255))
        self.score_rect = self.score.get_rect()
        self.score_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 50)

    def draw (self, screen):
         screen.fill((0, 0, 0))
         screen.blit(self.max_score_message,  self.max_score_message_rect)
         screen.blit(self.game_over, self.game_over_rect)
         screen.blit(self.decision, self.decision_rect)
         pygame.display.update()

    def restart_game(self, game):
        pass