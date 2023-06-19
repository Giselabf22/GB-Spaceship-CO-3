import random
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_1, ENEMY_2


class EnemyManager:

    ENEMIES = [ENEMY_1, ENEMY_2]
    OPTIONS = [1, 2]
    def __init__(self):
        self.enemies: list[Enemy] = []

    def update(self, game):
        if not self.enemies: # [] {} "" -> Valores Falsos 
            self.create_enemies()
        
        for enemy in self.enemies:
            enemy.update(self.enemies, game)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
    
    def create_enemies(self):
        self.choise = random.choice(self.OPTIONS)
        if self.choise == 1:
            for enemy_type in self.ENEMIES:
                self.enemies.append(Enemy(enemy_type))
        else:
            self.enemy_type = random.choice(self.ENEMIES)
            self.enemies.append(Enemy(self.enemy_type))
    
    def reset(self):
        self.enemies.clear()