import pygame
import sys

pygame.init()

# Ventana
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego")

clock = pygame.time.Clock()


class Game:

    def __init__(self):

        self.screen = screen

        # Jugador
        self.player = pygame.Rect(400, 300, 64, 64)
        self.speed = 5

        # Sprite sheet
        self.sprite_sheet = pygame.image.load("assets/player_walk.png").convert_alpha()

        self.frame_width = 64
        self.frame_height = 64

        self.frames = []

        sheet_width = self.sprite_sheet.get_width()

        for i in range(sheet_width // self.frame_width):
            frame = self.sprite_sheet.subsurface(
                (i * self.frame_width, 0, self.frame_width, self.frame_height)
            )
            self.frames.append(frame)

        self.current_frame = 0
        self.animation_speed = 0.2

        # Enemigos
        self.enemies = [
            [200, 100],
            [500, 200],
            [300, 400]
        ]

        self.enemy_size = 40

    def update(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.player.x -= self.speed

        if keys[pygame.K_RIGHT]:
            self.player.x += self.speed

        if keys[pygame.K_UP]:
            self.player.y -= self.speed

        if keys[pygame.K_DOWN]:
            self.player.y += self.speed

        # Animación
        self.current_frame += self.animation_speed

        if self.current_frame >= len(self.frames):
            self.current_frame = 0

    def draw(self):

        self.screen.fill((30, 30, 30))

        # Jugador animado
        self.screen.blit(self.frames[int(self.current_frame)], self.player)

        # Enemigos
        for enemy in self.enemies:
            pygame.draw.rect(
                self.screen,
                (255, 0, 0),
                (*enemy, self.enemy_size, self.enemy_size)
            )

        pygame.display.flip()


def main():

    game = Game()

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        game.update()
        game.draw()

        clock.tick(60)


if __name__ == "__main__":
    main()