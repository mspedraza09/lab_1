import pygame
import os
from game_data.profile_manager import SaveProfile
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
            self.fuente_pequenia = pygame.font.Font(ruta_fuente02,40)
        except:
            self.fuente = pygame.font.SysFont("Arial",150)
            self.fuente_02 = pygame.font.SysFont("Arial",100)
            self.fuente_pequenia = pygame.font.SysFont("Arial",40)

        self.boton_play = botones_menu(self.rosado, 400,200,self.fuente_02, self.ventana)
        self.boton_options = botones_menu(self.rosado, 400,300, self.fuente_02, self.ventana)
        self.boton_top_scores = botones_menu(self.rosado, 400,400, self.fuente_02, self.ventana)

        self.boton_credits_esquina = botones_menu(self.rosado, 90, 460, self.fuente_pequenia, self.ventana, ancho=150, alto=60)
        self.boton_exit = botones_menu(self.rosado, 710, 460, self.fuente_pequenia, self.ventana, ancho=150, alto=60)
    
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
        self.boton_top_scores.dibujar_botones("TOP SCORES")

        self.boton_credits_esquina.dibujar_con_fondo("CREDITS")
        self.boton_exit.dibujar_con_fondo("EXIT")


    def dibujar_barra_volumen(self, x, y, ancho_total, alto, volumen_actual):
        dibujar_titulo = self.fuente.render("VOLUMEN", True, self.blanco)
        rect_titulo = dibujar_titulo.get_rect(center=(400, 100))
        self.ventana.blit(dibujar_titulo, rect_titulo)
        
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
    def __init__(self, color, corX, corY, fuente, ventana, ancho=250, alto=80):
        self.color = color
        self.corX = corX
        self.corY = corY
        self.fuente = fuente
        self.ventana = ventana
        self.rect = pygame.Rect(0,0,ancho,alto)
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
    
    def dibujar_con_fondo(self, mensaje):
        pygame.draw.rect(self.ventana, self.color, self.rect)

        color_texto = (255, 255, 255) 
        dibujar_letra = self.fuente.render(mensaje, True, color_texto)
        rect_texto = dibujar_letra.get_rect(center=self.rect.center)
        self.ventana.blit(dibujar_letra, rect_texto)
    

class EscenaLogin:
    def __init__(self, ventana):
        self.ventana = ventana
        self.rosado = (252, 0, 153)
        self.blanco = (255, 255, 255)
        self.negro = (0, 0, 0)
        self.gris = (50, 50, 50)
        directorio_actual = os.path.dirname(__file__)
        ruta_fuente = os.path.join(directorio_actual, "elementos", "Cyberpunks Italic.otf")
        ruta_fuente02 = os.path.join(directorio_actual, "elementos", "Cyberpunks.otf")
        
       
        self.gestor_perfiles = SaveProfile()
        
        self.sub_estado = "seleccion"
        self.texto_usuario = ""
        self.input_rect = pygame.Rect(200, 300, 400, 50)
        self.input_activo = False
        
       
        self.rect_btn_login = pygame.Rect(250, 250, 300, 60)
        self.rect_btn_registro = pygame.Rect(250, 350, 300, 60)
        try:
            self.fuente = pygame.font.Font(ruta_fuente, 32)
        except:
            self.fuente = pygame.font.SysFont("Arial",32)
        self.mensaje_error = "" 

    def manejar_eventos(self, event):
        if self.sub_estado == "seleccion":
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.rect_btn_login.collidepoint(event.pos):
                    self.sub_estado = "login_input"
                    self.input_activo = True
                elif self.rect_btn_registro.collidepoint(event.pos):
                    self.sub_estado = "registro_input"
                    self.input_activo = True
                    
        elif self.sub_estado in ["login_input", "registro_input"]:
            if event.type == pygame.KEYDOWN and self.input_activo:
                if event.key == pygame.K_BACKSPACE:
                    self.texto_usuario = self.texto_usuario[:-1]
                elif event.key == pygame.K_RETURN:
                    
                    usuario_ingresado = self.texto_usuario.strip()
                    
                    if usuario_ingresado == "":
                        self.mensaje_error = "Escribe un nombre válido"
                        return None

                    if self.sub_estado == "login_input":
                        
                        datos = self.gestor_perfiles.get_profile(usuario_ingresado)
                        if datos:
                            print(f"Bienvenido de nuevo, {usuario_ingresado}")
                            return {"accion": "ENTRAR", "usuario": usuario_ingresado}
                        else:
                            self.mensaje_error = "Usuario no encontrado"
                    
                    elif self.sub_estado == "registro_input":
                        
                        if self.gestor_perfiles.get_profile(usuario_ingresado):
                            self.mensaje_error = "El usuario ya existe"
                        else:
                            
                            datos_iniciales = {"score": 0, "nivel": 1}
                            self.gestor_perfiles.save_profile(usuario_ingresado, datos_iniciales)
                            print(f"Usuario {usuario_ingresado} registrado con éxito")
                            return {"accion": "ENTRAR", "usuario": usuario_ingresado}
                
                elif event.key == pygame.K_ESCAPE:
                    self.sub_estado = "seleccion"
                    self.mensaje_error = ""
                else:
                    if len(self.texto_usuario) < 15:
                        self.texto_usuario += event.unicode
        return None

    def dibujar(self):
        self.ventana.fill(self.negro) 
        
        
        dibujar_titulo = self.fuente.render("SISTEMA DE ACCESO", True, self.rosado)
        rect_titulo = dibujar_titulo.get_rect(center=(400, 80))
        self.ventana.blit(dibujar_titulo, rect_titulo)

       
        if self.sub_estado == "seleccion":
           
            pygame.draw.rect(self.ventana, self.rosado, self.rect_btn_login)
            txt_login = self.fuente.render("INICIAR SESION", True, self.blanco)
            self.ventana.blit(txt_login, txt_login.get_rect(center=self.rect_btn_login.center))

            
            pygame.draw.rect(self.ventana, self.rosado, self.rect_btn_registro)
            txt_reg = self.fuente.render("REGISTRAR", True, self.blanco)
            self.ventana.blit(txt_reg, txt_reg.get_rect(center=self.rect_btn_registro.center))

        elif self.sub_estado in ["login_input", "registro_input"]:
            
            etiqueta = "MODO: LOGIN" if self.sub_estado == "login_input" else "MODO: REGISTRO"
            txt_modo = self.fuente.render(etiqueta, True, self.blanco)
            self.ventana.blit(txt_modo, (200, 180))

            
            color_borde = self.blanco if self.input_activo else self.gris
            pygame.draw.rect(self.ventana, color_borde, self.input_rect, 2)
            
            
            superficie_texto = self.fuente.render(self.texto_usuario, True, self.rosado)
            self.ventana.blit(superficie_texto, (self.input_rect.x + 10, self.input_rect.y + 10))

            
            if self.mensaje_error:
                txt_err = self.fuente.render(self.mensaje_error, True, (255, 0, 0)) 
                self.ventana.blit(txt_err, (200, 370))

            
            txt_ayuda = self.fuente.render("ENTER para confirmar - ESC para volver", True, self.gris)
            self.ventana.blit(txt_ayuda, (180, 500))

        
        rect_borde = pygame.Rect(5, 5, 790, 590)
        pygame.draw.rect(self.ventana, self.rosado, rect_borde, 3)




    


