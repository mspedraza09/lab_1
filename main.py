import pygame
from game.scenes.menu_scenes import fondoMenu
from game.scenes.resources import crear_ventana
from game.scenes.setting_scenes import Sonido

negro = (0,0,0)
ventana = crear_ventana("Menu", negro)
menu = fondoMenu(ventana)
running = True
musica = Sonido()
musica.musica_play()
estado = "menu"
volumen_actual = 0.5 
pygame.mixer.music.set_volume(volumen_actual)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                if menu.boton_play.rect.collidepoint(event.pos):
                    print("¡Click en PLAY!")
                
                if menu.boton_options.rect.collidepoint(event.pos):
                    estado = "volumen"
                    print("¡Click en VOLUMEN!")

                if menu.boton_credits.rect.collidepoint(event.pos):
                    print("¡Click en CREDITS!")
        
        if event.type == pygame.KEYDOWN and estado == "volumen":
            if event.key == pygame.K_RIGHT:
                volumen_actual = min(volumen_actual + 0.05, 1.0)
                pygame.mixer.music.set_volume(volumen_actual)
            if event.key == pygame.K_LEFT:
                volumen_actual = max(volumen_actual - 0.05, 0.0)
                pygame.mixer.music.set_volume(volumen_actual)
            if event.key == pygame.K_ESCAPE: # Para poder regresar al menú
                estado = "menu"
        
        

    ventana.fill(negro)
    if estado == "menu":
        menu.titulo_menu()
    elif estado == "volumen":
        menu.dibujar_barra_volumen(200,250,400,80,volumen_actual)
                
    pygame.display.flip()

    

pygame.quit()