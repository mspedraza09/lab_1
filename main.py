import pygame
from game.scenes.menu_scenes import fondoMenu, EscenaLogin, TopScores
from game.scenes.resources import crear_ventana
from game.scenes.setting_scenes import Sonido
from game_data.profile_manager import SaveProfile

negro = (0,0,0)
ventana = crear_ventana("Menu", negro)
menu = fondoMenu(ventana)
running = True
musica = Sonido()
musica.musica_play()
estado = "login"
volumen_actual = 0.5 
pygame.mixer.music.set_volume(volumen_actual)
usuario = SaveProfile()
login_scene = EscenaLogin(ventana)
top_scores_scene = TopScores(ventana)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
        if estado == "login":
            resultado = login_scene.manejar_eventos(event)
            if resultado and resultado["accion"] == "ENTRAR":
                usuario_actual = resultado["usuario"]
                estado = "menu"
        
        
        elif estado == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    if menu.boton_play.rect.collidepoint(event.pos):
                        print("¡Click en PLAY!")
                    
                    elif menu.boton_options.rect.collidepoint(event.pos):
                        estado = "volumen"
                        print("¡Click en VOLUMEN!")

                    elif menu.boton_top_scores.rect.collidepoint(event.pos):
                        estado = "top_scores"
                        print("¡Click en TOP SCORES!")

                    elif menu.boton_credits_esquina.rect.collidepoint(event.pos):
                        estado = "credits"

                    elif menu.boton_exit.rect.collidepoint(event.pos):
                        running = False
        
        
        elif estado == "volumen":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    volumen_actual = min(volumen_actual + 0.05, 1.0)
                    pygame.mixer.music.set_volume(volumen_actual)
                if event.key == pygame.K_LEFT:
                    volumen_actual = max(volumen_actual - 0.05, 0.0)
                    pygame.mixer.music.set_volume(volumen_actual)
                if event.key == pygame.K_ESCAPE: 
                    estado = "menu"

        elif estado == "credits":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: 
                    estado = "menu"

    
    ventana.fill(negro)
    if estado == "login":
        login_scene.dibujar()
    elif estado == "menu":
        menu.titulo_menu()
    elif estado == "volumen":
        menu.dibujar_barra_volumen(200,250,400,80,volumen_actual)
    elif estado == "top_scores":
        top_scores_scene.get_scores()
    
    pygame.display.flip()

pygame.quit()