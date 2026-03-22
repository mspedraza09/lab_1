import pygame
from game.scenes.menu_scenes import fondoMenu
from game.scenes.resources import crear_ventana

negro = (0,0,0)
ventana = crear_ventana("Menu", negro)
menu = fondoMenu(ventana)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    ventana.fill(negro)
    menu.titulo_menu()
    pygame.display.flip()

pygame.quit()