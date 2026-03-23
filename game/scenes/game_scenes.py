import pygame
import random

class GameScene:
    def __init__(self, screen):
        print("GameScene cargada")

        self.screen = screen

        # Jugador
        self.player = [400, 500]
        self.player_size = 50
        self.speed = 5

        # Enemigos
        self.enemies = []
        self.enemy_size = 50
        self.spawn_timer = 0

        # Estado del juego
        self.running = True
        self.game_over = False

        # Score y vidas
        self.score = 0
        self.lives = 3

        self.font = pygame.font.Font(None, 36)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and self.game_over:
                    self.__init__(self.screen)  # reiniciar juego

    def update(self):
        if self.game_over:
            return

        keys = pygame.key.get_pressed()

        # Movimiento jugador
        if keys[pygame.K_LEFT]:
            self.player[0] -= self.speed
        if keys[pygame.K_RIGHT]:
            self.player[0] += self.speed

        # Limites pantalla
        if self.player[0] < 0:
            self.player[0] = 0
        if self.player[0] > 800 - self.player_size:
            self.player[0] = 800 - self.player_size

        # Generar enemigos
        self.spawn_timer += 1
        if self.spawn_timer > 60:
            x = random.randint(0, 800 - self.enemy_size)
            self.enemies.append([x, 0])
            self.spawn_timer = 0

        # Mover enemigos
        for enemy in self.enemies:
            enemy[1] += 3

        # Colisiones
        player_rect = pygame.Rect(*self.player, self.player_size, self.player_size)

        for enemy in self.enemies[:]:
            enemy_rect = pygame.Rect(*enemy, self.enemy_size, self.enemy_size)

            if player_rect.colliderect(enemy_rect):
                self.lives -= 1
                self.enemies.remove(enemy)

                if self.lives <= 0:
                    self.game_over = True

        # Limpiar enemigos fuera de pantalla
        self.enemies = [enemy for enemy in self.enemies if enemy[1] < 600]

        # Score
        self.score += 0.1

    def draw(self):
        self.screen.fill((0, 0, 0))

        # Jugador
        pygame.draw.rect(
            self.screen,
            (0, 255, 0),
            (*self.player, self.player_size, self.player_size)
        )

        # Enemigos
        for enemy in self.enemies:
            pygame.draw.rect(
                self.screen,
                (255, 0, 0),
                (*enemy, self.enemy_size, self.enemy_size)
            )

        # Score
        score_text = self.font.render(f"Score: {int(self.score)}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

        # Vidas
        lives_text = self.font.render(f"Vidas: {self.lives}", True, (255, 255, 255))
        self.screen.blit(lives_text, (10, 40))

        # Game Over
        if self.game_over:
            game_over_text = self.font.render("GAME OVER - Presiona R", True, (255, 0, 0))
            self.screen.blit(game_over_text, (200, 250))

        pygame.display.flip()