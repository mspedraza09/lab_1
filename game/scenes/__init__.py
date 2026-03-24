import pygame

def crear_ventana(nombre_ventana):
    pygame.init()
    ventana = pygame.display.set_mode((800, 600))
    pygame.display.set_caption(nombre_ventana)
    return ventana


