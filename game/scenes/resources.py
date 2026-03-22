import pygame 

def crear_ventana(titulo, color):
    pygame.init()
    ventana = pygame.display.set_mode((800, 600))
    pygame.display.set_caption(titulo)
    ventana.fill(color)
    return ventana