import pygame
import random
import os

class GameScene:
    def __init__(self, screen):
        print("GameScene cargada")

        self.screen = screen

        # RUTA DE ASSETS
        base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        assets_path = os.path.join(base_path, "game_data", "assets")

        # CARGAR SPRITE DEL JUGADOR
        self.player_image = pygame.image.load(
            os.path.join(assets_path, "Biker", "Biker_idle.png")
        ).convert_alpha()

        self.player_image = pygame.transform.scale(self.player_image, (80, 80))

        # JUGADOR
        self.player = [400, 500]
        self.player_size = 80
        self.speed = 5

        # ENEMIGOS
        self.enemies = []
        self.enemy_size = 50
        self.spawn_timer = 0

        # ESTADO DEL JUEGO
        self.running = True
        self.game_over = False

        # SCORE Y VIDAS
        self.score = 0
        self.lives = 3

        self.font = pygame.font.Font(None, 36)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and self.game_over:
                    self.__init__(self.screen)

    def update(self):
        if self.game_over:
            return

        keys = pygame.key.get_pressed()

        # MOVIMIENTO JUGADOR
        if keys[pygame.K_LEFT]:
            self.player[0] -= self.speed
        if keys[pygame.K_RIGHT]:
            self.player[0] += self.speed

        # LIMITES DE PANTALLA
        if self.player[0] < 0:
            self.player[0] = 0
        if self.player[0] > 800 - self.player_size:
            self.player[0] = 800 - self.player_size

        # GENERAR ENEMIGOS
        self.spawn_timer += 1
        if self.spawn_timer > 60:
            x = random.randint(0, 800 - self.enemy_size)
            self.enemies.append([x, 0])
            self.spawn_timer = 0

        # MOVER ENEMIGOS
        for enemy in self.enemies:
            enemy[1] += 3

        # COLISIONES
        player_rect = pygame.Rect(*self.player, self.player_size, self.player_size)

        for enemy in self.enemies[:]:
            enemy_rect = pygame.Rect(*enemy, self.enemy_size, self.enemy_size)

            if player_rect.colliderect(enemy_rect):
                self.lives -= 1
                self.enemies.remove(enemy)

                if self.lives <= 0:
                    self.game_over = True

        # ELIMINAR ENEMIGOS FUERA
        self.enemies = [enemy for enemy in self.enemies if enemy[1] < 600]

        # SCORE
        self.score += 0.1

    def draw(self):
        self.screen.fill((0, 0, 0))

        # JUGADOR (SPRITE)
        self.screen.blit(self.player_image, self.player)

        # ENEMIGOS
        for enemy in self.enemies:
            pygame.draw.rect(
                self.screen,
                (255, 0, 0),
                (*enemy, self.enemy_size, self.enemy_size)
            )

        # SCORE
        score_text = self.font.render(f"Score: {int(self.score)}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

        # VIDAS
        lives_text = self.font.render(f"Vidas: {self.lives}", True, (255, 255, 255))
        self.screen.blit(lives_text, (10, 40))

        # GAME OVER
        if self.game_over:
            game_over_text = self.font.render("GAME OVER - Presiona R", True, (255, 0, 0))
            self.screen.blit(game_over_text, (200, 250))

        pygame.display.flip()