import pygame
import os

def crear_ventana(titulo, color):
    pygame.init()
    ventana = pygame.display.set_mode((800, 600))
    pygame.display.set_caption(titulo)
    ventana.fill(color)
    return ventana



class fondoMenu:
    def __init__(self, ventana):
        self.ventana = ventana
        self.blanco = (255,255,255)
        self.rosado = (252, 0, 153)
        directorio_actual = os.path.dirname(__file__)
        ruta_fuente = os.path.join(directorio_actual, "imagenes", "Cyberpunks Italic.otf")
        ruta_fuente02 = os.path.join(directorio_actual, "imagenes", "Cyberpunks.otf")

        #self.imagen = pygame.image.load("game/scenes/imagenes/git_menu.gif")
        #self.imagen = pygame.transform.scale(self.imagen, (800, 600)) 
        try:
            self.fuente = pygame.font.Font(ruta_fuente,100)
            self.fuente_02 = pygame.font.Font(ruta_fuente02,80)
        except:
            self.fuente = pygame.font.SysFont("Arial",150)
            self.fuente_02 = pygame.font.SysFont("Arial",100)
    
    def titulo_menu(self):
        
        dibujar_titulo = self.fuente.render("Arcade", True, self.blanco)
        rect_titulo = dibujar_titulo.get_rect(center=(400, 100))
        self.ventana.blit(dibujar_titulo, rect_titulo)

        #Botones 
        boton_play = botones_menu(self.rosado, 400,200,self.fuente_02, self.ventana)
        boton_options = botones_menu(self.rosado, 400,300, self.fuente_02, self.ventana)
        boton_credits = botones_menu(self.rosado, 400,400, self.fuente_02, self.ventana)

        boton_play.dibujar_botones("PLAY")
        boton_options.dibujar_botones("OPTIONS")
        boton_credits.dibujar_botones("CREDITS")
        

        rectangulo = pygame.Rect(0,530,800,600)
        pygame.draw.rect(self.ventana,self.rosado,rectangulo)

        rectangulo_2 = pygame.Rect(5,5,790,510)
        pygame.draw.rect(self.ventana, self.rosado, rectangulo_2, 3)


class botones_menu:
    def __init__(self, color, corX, corY, fuente, ventana):
        self.color = color
        self.corX = corX
        self.corY = corY
        self.fuente = fuente
        self.ventana = ventana
        self.rect = pygame.Rect(0,0,250,80)
        self.rect.center = (corX, corY)

    def dibujar_botones(self, mensaje):
        pos_mouse = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos_mouse):
            self.color = (255,255,255)
        else:
            self.color = (252,0,153)

        dibujar_boton = self.fuente.render(mensaje, True, self.color)
        rect_boton = dibujar_boton.get_rect(center=(self.corX,self.corY))
        self.ventana.blit(dibujar_boton, rect_boton)
     
          
    
    





    


