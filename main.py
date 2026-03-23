import pygame
import sys
import os

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego")

clock = pygame.time.Clock()


class Game:

    def __init__(self):

        self.screen = screen

    
        fondo_path = "game_data/assets/Fondo"
        fondo_file = os.listdir(fondo_path)[0]

        self.background = pygame.image.load(
            os.path.join(fondo_path, fondo_file)
        ).convert()

        self.background = pygame.transform.scale(self.background, (WIDTH, HEIGHT))

        
        player_path = "game_data/assets/Biker"
        player_file = os.listdir(player_path)[0]

        self.player_img = pygame.image.load(
            os.path.join(player_path, player_file)
        ).convert_alpha()

        self.player_img = pygame.transform.scale(self.player_img, (80, 80))

        self.player = pygame.Rect(100, 400, 80, 80)
        self.speed = 5

    
        enemy_path = "game_data/assets/Punk1"
        enemy_file = os.listdir(enemy_path)[0]

        self.enemy_img = pygame.image.load(
            os.path.join(enemy_path, enemy_file)
        ).convert_alpha()

        self.enemy_img = pygame.transform.scale(self.enemy_img, (80, 80))

        self.enemies = [
            [600, 400],
            [750, 400],
            [900, 400]
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