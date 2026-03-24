import pygame
import os
import random


class GameScene:

    def __init__(self, screen):
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()

        base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        assets_path = os.path.join(base_path, "game_data", "assets")

        fondo_path = os.path.join(assets_path, "Fondo")
        fondo_files = os.listdir(fondo_path)

        self.background = pygame.image.load(
            os.path.join(fondo_path, fondo_files[0])
        ).convert()

        self.background = pygame.transform.scale(
            self.background, (self.width, self.height)
        )

        player_path = os.path.join(assets_path, "Biker")
        player_files = os.listdir(player_path)

        self.player = pygame.image.load(
            os.path.join(player_path, player_files[0])
        ).convert_alpha()

        self.player = pygame.transform.scale(self.player, (120, 120))

        self.player_rect = self.player.get_rect()
        self.player_rect.x = 100
        self.player_rect.y = self.height - 160

        self.player_speed = 6

        enemy_path = os.path.join(assets_path, "Punk1")
        enemy_files = os.listdir(enemy_path)

        self.enemy_img = pygame.image.load(
            os.path.join(enemy_path, enemy_files[0])
        ).convert_alpha()

        self.enemy_img = pygame.transform.scale(self.enemy_img, (120, 120))

        self.enemies = []

        self.font = pygame.font.SysFont(None, 36)

        self.score = 0
        self.final_score = 0   # ← aquí se guardará el puntaje final
        self.lives = 3
        self.game_over = False

        self.spawn_timer = 0
        self.hit_cooldown = 0

    def spawn_enemy(self):
        rect = self.enemy_img.get_rect()
        rect.x = self.width
        rect.y = random.randint(self.height - 200, self.height - 120)
        self.enemies.append(rect)

    def handle_input(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.player_rect.y -= self.player_speed

        if keys[pygame.K_DOWN]:
            self.player_rect.y += self.player_speed

        if keys[pygame.K_LEFT]:
            self.player_rect.x -= self.player_speed

        if keys[pygame.K_RIGHT]:
            self.player_rect.x += self.player_speed

    def update(self):

        if self.game_over:
            return

        self.spawn_timer += 1

        if self.spawn_timer > 90:
            self.spawn_enemy()
            self.spawn_timer = 0

        for enemy in self.enemies:
            enemy.x -= 5

        self.enemies = [e for e in self.enemies if e.x > -120]

        if self.hit_cooldown > 0:
            self.hit_cooldown -= 1

        for enemy in self.enemies[:]:
            if self.player_rect.colliderect(enemy):

                if self.hit_cooldown == 0:
                    self.lives -= 1
                    self.hit_cooldown = 60

                self.enemies.remove(enemy)

                if self.lives <= 0:
                    self.game_over = True
                    self.final_score = self.score  # ← se guarda el puntaje final

        self.score += 1

    def draw(self):

        self.screen.blit(self.background, (0, 0))

        self.screen.blit(self.player, self.player_rect)

        for enemy in self.enemies:
            self.screen.blit(self.enemy_img, enemy)

        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

        lives_text = self.font.render(f"Vidas: {self.lives}", True, (255, 255, 255))
        self.screen.blit(lives_text, (10, 40))

        if self.game_over:
            text = self.font.render("GAME OVER - Presiona R", True, (255, 0, 0))
            self.screen.blit(text, (200, 250))