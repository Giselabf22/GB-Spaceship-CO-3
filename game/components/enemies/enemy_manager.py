from game.components.enemies.enemy import Enemy
from game.components.enemies.enemy2 import Enemy2


class EnemyManager:
    def __init__(self):
        self.enemies: list[Enemy] = []
        self.enemies2: list[Enemy2] = []  # Lista para almacenar instancias de Enemy2

    def update(self, game):
        if not self.enemies:
            self.enemies.append(Enemy())

        if not self.enemies2:
            self.enemies2.append(Enemy2())

        for enemy in self.enemies:
            enemy.update(self.enemies, game)

        for enemy2 in self.enemies2:
            enemy2.update(self.enemies2, game)


    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

        for enemy2 in self.enemies2:
            enemy2.draw(screen)
