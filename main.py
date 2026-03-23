import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego")

clock = pygame.time.Clock()


class Game:

    def __init__(self):

        self.screen = screen

        # Fondo
        self.background = pygame.image.load(
            "game_data/assets/Fondo/fondo.png"
        ).convert()

        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))

        # Jugador
        self.player_img = pygame.image.load(
            "game_data/assets/Biker/Biker_run.png"
        ).convert_alpha()

        self.player_img = pygame.transform.scale(self.player_img, (80, 80))

        self.player = pygame.Rect(100, 400, 80, 80)
        self.speed = 5

        # Enemigos
        self.enemy_img = pygame.image.load(
            "game_data/assets/Punk1/Punk_run.png"
        ).convert_alpha()

        self.enemy_img = pygame.transform.scale(self.enemy_img, (80, 80))

        self.enemies = [
            [600, 400],
            [700, 400],
            [800, 400]
        ]

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

        # mover enemigos
        for enemy in self.enemies:
            enemy[0] -= 3

    def draw(self):

        # fondo
        self.screen.blit(self.background, (0, 0))

        # jugador
        self.screen.blit(self.player_img, self.player)

        # enemigos
        for enemy in self.enemies:
            self.screen.blit(self.enemy_img, enemy)

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