import sys
import os
import pygame

sys.path.append(os.path.dirname(__file__))

from game.scenes.game_scenes import GameScene

def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Mi Juego")

    scene = GameScene(screen)
    clock = pygame.time.Clock()

    while scene.running:
        scene.handle_events()
        scene.update()
        scene.draw()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()