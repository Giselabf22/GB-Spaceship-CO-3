import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import ENEMY_TYPE, SHIELD_TYPE, SPACESHIP_TYPE


class BulletManager:

    def __init__(self):
        self.bullets: list[Bullet] = []
        self.enemy_bullets: list[Bullet] = []
        
    def update(self, game):
        collision_detected = False
        
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)
            if bullet.rect.colliderect(game.player.rect):
                self.enemy_bullets.remove(bullet)
                if game.player.power_up_type != SHIELD_TYPE:
                    game.playing = False
                    game.death_count += 1
                    pygame.time.delay(1000)
                    collision_detected = True
                    break
                
        if not collision_detected:
            for enemy in game.enemy_manager.enemies:
                if enemy.rect.colliderect(game.player.rect):
                    game.enemy_manager.enemies.remove(enemy)
                    if game.player.power_up_type != SHIELD_TYPE:
                        game.playing = False
                        game.death_count += 1
                        pygame.time.delay(1000)
                        collision_detected = True
                        break

        if not collision_detected:
            for bullet in self.bullets:
                bullet.update(self.bullets)
                for enemy in game.enemy_manager.enemies:
                    if bullet.rect.colliderect(enemy.rect):
                        if bullet in self.bullets:
                            self.bullets.remove(bullet)
                        if enemy in game.enemy_manager.enemies:
                            game.enemy_manager.enemies.remove(enemy)
                        print(len(self.bullets))
                        game.score += 1
                        game.enemy_manager.update(game)
                        collision_detected = True
                        break
                    
                if collision_detected:
                    break

    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        
        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == ENEMY_TYPE and not self.enemy_bullets:
            self.enemy_bullets.append(bullet)
            
        if bullet.owner == SPACESHIP_TYPE and len(self.bullets) < 3 and bullet not in self.bullets:
            self.bullets.append(bullet)

    def reset(self):
        self.bullets.clear()
        self.enemy_bullets.clear()

        