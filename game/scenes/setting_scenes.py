import pygame 
import os
from game.scenes.menu_scenes import botones_menu


class Sonido:
    def __init__(self):
        os.environ['SDL_AUDIODRIVER'] = 'dummy'
        pygame.mixer.init()
        directorio_actual = os.path.dirname(__file__)
        ruta_sonido = os.path.join(directorio_actual, "elementos","End-of-Line-_From-TRON_-Legacy_Score_.mp3")
        ruta = "game/scenes/elementos/End-of-Line-_From-TRON_-Legacy_Score_.mp3"
        print(f"Buscando sonido en: {ruta_sonido}")
        if not os.path.exists(ruta):
            print("--- ERROR: ¡El archivo no existe en esa carpeta! ---")
        try:
            pygame.mixer.music.load(str(ruta_sonido))
            self.sonido = True
            print("Cargado con éxito")
        except:
            self.sonido = False
            print("No se cargo nada")

    def musica_play(self):
        if self.sonido:
            pygame.mixer.music.play(-1)
            print("Reproducciendo")



        
    

    