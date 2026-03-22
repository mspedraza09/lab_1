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
        ruta_fuente = os.path.join(directorio_actual, "elementos", "Cyberpunks Italic.otf")
        ruta_fuente02 = os.path.join(directorio_actual, "elementos", "Cyberpunks.otf")

        #self.imagen = pygame.image.load("game/scenes/imagenes/git_menu.gif")
        #self.imagen = pygame.transform.scale(self.imagen, (800, 600)) 
        try:
            self.fuente = pygame.font.Font(ruta_fuente,100)
            self.fuente_02 = pygame.font.Font(ruta_fuente02,80)
        except:
            self.fuente = pygame.font.SysFont("Arial",150)
            self.fuente_02 = pygame.font.SysFont("Arial",100)

        self.boton_play = botones_menu(self.rosado, 400,200,self.fuente_02, self.ventana)
        self.boton_options = botones_menu(self.rosado, 400,300, self.fuente_02, self.ventana)
        self.boton_credits = botones_menu(self.rosado, 400,400, self.fuente_02, self.ventana)
    
    def titulo_menu(self):
        rectangulo = pygame.Rect(0,530,800,600)
        pygame.draw.rect(self.ventana,self.rosado,rectangulo)

        rectangulo_2 = pygame.Rect(5,5,790,510)
        pygame.draw.rect(self.ventana, self.rosado, rectangulo_2, 3)
        
        dibujar_titulo = self.fuente.render("Arcade", True, self.blanco)
        rect_titulo = dibujar_titulo.get_rect(center=(400, 100))
        self.ventana.blit(dibujar_titulo, rect_titulo)

        self.boton_play.dibujar_botones("PLAY")
        self.boton_options.dibujar_botones("VOLUMEN")
        self.boton_credits.dibujar_botones("CREDITS")

    def dibujar_barra_volumen(self, x, y, ancho_total, alto, volumen_actual):
        dibujar_titulo = self.fuente.render("VOLUMEN", True, self.blanco)
        rect_titulo = dibujar_titulo.get_rect(center=(400, 100))
        self.ventana.blit(dibujar_titulo, rect_titulo)
        # 1. Dibujar el fondo de la barra (el contenedor)
        rect_fondo = pygame.Rect(x, y, ancho_total, alto)
        pygame.draw.rect(self.ventana, (50, 50, 50), rect_fondo)
        
        ancho_relleno = ancho_total * volumen_actual
        
        rect_relleno = pygame.Rect(x, y, ancho_relleno, alto)
        pygame.draw.rect(self.ventana, self.rosado, rect_relleno)
        
        pygame.draw.rect(self.ventana, self.blanco, rect_fondo, 2)

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
    


