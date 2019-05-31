import pygame
pygame.init()
from Nave import *
from Disparo import *
from DisparoOnda import *
from DisparoLinia import *
from Enemigos import *
import ctypes
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
import gc
#user32.GetSystemMetrics(0)= ancho
#user32.GetSystemMetrics(1)=alto    
Estado=[]
"""lista estado juego"""
Clock = pygame.time.Clock()
ancho,alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
#ancho=int(ancho/3)
#alto=alto-40    
#lista de disparos
"""inicio"""
ventana= pygame.display.set_mode((ancho,alto),pygame.FULLSCREEN)
#print (ventana.
pygame.display.set_caption("Bullet hell")

ListaDebug=[]#####lista para reservada para mostrar datos de debug
clock=True  #juego corriendo
jugador=Nave(64,64)
vel=10

#enemigo de prueba

debug=False
Estado.append("Nivel 1")#temp

Tiempo=0
#variable para contar segundo, no avanza si hay un jefe en pantalla
FPS=60
#varible 
Cuadros=0
listaDisparos=[]
#variable para contar cuadors, cada 60 se reinicia y Tiempo avanza



class HojaSprites:
    def __init__(self,NombreArchivo,columnas,filas):
        self.Hoja=pygame.image.load(NombreArchivo).convert_alpha()
        self.Columnas=columnas
        self.Filas=filas
        self.TotalDeCeldas=columnas*filas
        
        self.Rect=self.Hoja.get_rect()
        Ancho=self.cellWidth=self.Rect.width/columnas
        print("ancho:",self.Rect.width)
        print("ancho celda",self.Rect.width/columnas)
        Alto=self.cellHeight=self.Rect.height/filas
        print("alto:",self.Rect.height)
        print("alto celda",self.Rect.height/filas)
        self.cells=list([(index%columnas*Ancho,int(index/columnas)*Alto,Ancho,Alto)for index in range (self.TotalDeCeldas)])
        print("lista celdas:",self.cells)
        
    def dibujar(self,superficie,indice,XY):
        superficie.blit(self.Hoja,(XY[0],XY[1]),self.cells[indice])


HojaDisparos=HojaSprites("sprites/Disparos2.png",3,4)






def Dibujar(self,SuperficiePrincipal,ListaEntidades,ListaEsenarios=[]):
    #def __init__(self,SuperficiePrincipal,ListaDisparos=[],ListaEntidades=[],ListaEsenarios=[]): #cambiar a diccionarios
    ventana.fill((0,0,0))
    for Sprite in ListaEsenarios:
        break##esenarios aun no definidos
    
    for Texto in ListaDebug:
        ventana.blit(Texto.get("Texto"),(0,Texto.get("Y")))
        
    
    for Sprite in ListaEntidades:
        pygame.draw.rect(ventana,(0,0,180),Sprite.GetTodo())
    print(len(listaDisparos),"if 0, error al dibujar")
    for Disparo in listaDisparos:
        #ventana.blit(pygame.image.load("sprites/exp.png"), Disparo.GetTodo())
        HojaDisparos.dibujar(ventana,Disparo.GetIndex(),Disparo.GetTodo())
        print(Disparo.GetTodo(),"disparo en pantalla    ")
        #pass###por completar
            
    ventana.blit(pygame.image.load("sprites/nave.png"),jugador.GetTodo())
    pygame.display.update()
    pass




listaEntidades=[]#lista entidades sin contar al jugador
listaEntidadesAuxliar=[]#lista a añadir en el siguiente cuadro entidades sin contar al jugador
listaEntidades.append(Enemigo(32,32))












while clock:
    if Estado[0]=="Nivel 1":
        Cuadros=Cuadros+1
        #reiniciar ventana
        #ventana.fill((0,0,0))
        #pygame.time.delay(100)#reloj
        if Cuadros!=60:
            Cuadros=Cuadros+1
        else:
            Cuadros=0
            Tiempo=Tiempo+1
         #contado de segundos, se utilizara para sincronizar spawn de enemigos con avanze de nivel
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                clock=False
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_LCTRL:
                    jugador.CambiarModo()
                    """cambio de modo solo se tiene que activar una vez para activar o desactivar"""
                if event.key==pygame.K_F12:#debug
                    if debug:
                        debug=False
                        
                    else:
                        debug=True
                        pygame.font.init()
                if event.key==pygame.K_F10:
                    if FPS==60:
                        FPS=1
                    else :
                        FPS=60
                            
                
        """revision salir"""
        print("disparos :",len(listaDisparos))
        keys = pygame.key.get_pressed()
        
        
        if keys[pygame.K_LSHIFT]:
            vel=45
        else:
            vel=10
        """velocidad de movimiento"""
      
        #if keys[K_F12]:#debug
           # if debug:
             #   debug=False
           # else:
               # debug=True
        
        if keys[pygame.K_z]:#disparar onda
            listaDisparos.append(Dsin(jugador.GetX()+10,jugador.GetY()+35,64,(12,225,10)))
        if keys[pygame.K_x]:#disparar normal
            for disparo in jugador.DisparoPrimario():
                listaDisparos.append(disparo)
            #listaDisparos.append(Disparo(jugador.GetX()+10,jugador.GetY()+35,(255,17,20)))
        if keys[pygame.K_c]:#disparar linia
            listaDisparos.append(DLine(jugador.GetX()+10,jugador.GetY()+35,Cuadros,(255,17,20)))###copiar mas adelante a un arma estrella
            listaDisparos.append(DLine(jugador.GetX()+10,jugador.GetY()+35,Cuadros+90,(255,17,20)))
            listaDisparos.append(DLine(jugador.GetX()+10,jugador.GetY()+35,Cuadros+180,(255,17,20)))
            listaDisparos.append(DLine(jugador.GetX()+10,jugador.GetY()+35,Cuadros+270,(255,17,20)))
        if keys[pygame.K_LEFT]:
            if jugador.GetX() > 0:
                jugador.SetX(jugador.GetX()-vel)
            else:
                jugador.SetX(0)
        if keys[pygame.K_ESCAPE]:##salir
            clock=False
        if keys[pygame.K_RIGHT]:
            if jugador.GetX() < int(ancho)-64:#64 =ancho sprite
                jugador.SetX(jugador.GetX()+vel)
            else:
                jugador.SetX(int(ancho)-64)#64 =ancho sprite
        if keys[pygame.K_UP]:
            if jugador.GetY()>0:
                jugador.SetY(jugador.GetY()-vel)
            else:
                jugador.SetY(0)
        if keys[pygame.K_DOWN]:
            if jugador.GetY()<int(alto)-64:#64 =ancho sprite
                jugador.SetY(jugador.GetY()+vel)
            else:
                jugador.SetY(int(alto)-64)#64 =ancho sprite
                                                                                                            ###Zona de control enemigos
        for entidad in listaEntidades:                                                                        #
            listaDisparosEnemigos=entidad.Actualizar(jugador.GetCentro())#enemigos disparando y apuntando     #
            #pygame.draw.rect(ventana,(0,0,180),entidad.GetTodo())  #añadir a una funcion de dibujo            #
            for disparo in listaDisparosEnemigos:                                                             #
                print (len(listaDisparos))                                                                    #
                listaDisparos.append(disparo)                                                                 #
        for entidad in listaEntidadesAuxliar:#cosas a añadir el siguiente ciclo                               #
            listaEntidades.append(entidad)                                                                    #
            listaEntidadesAuxliar.pop(listaEntidadesAuxliar.index(entidad))                                   #
                                                                                                            ###
        
        """resetear fondo"""
        jugador.Actualizar()
        for disparo in listaDisparos:
            if disparo.GetY()<0 or disparo.GetY()> alto+50 or disparo.GetX() < -150 or disparo.GetX() > ancho+150:
                listaDisparos.pop(listaDisparos.index(disparo))
            """borrar disparos fuera de pantalla, por arriba"""
            disparo.Actualizar()
            #pygame.draw.rect(ventana,disparo.GetRGB(), disparo.GetTodo())###dibujar disparo
        
        if debug:
            fuente=pygame.font.SysFont(None,25)
            ListaDebug.append(dict(Texto=fuente.render("disparos:"+str(len(listaDisparos)),True,(255,255,0),(0,0,0)),Y=0))
            #ventana.blit(texto,(0,0))
            ListaDebug.append(dict(Texto=fuente.render("FPS:"+str(Clock.get_fps()),True,(255,255,0),(0,0,0)),Y=25))
            #ventana.blit(texto,(0,25))
            print("paso\n\n\n\n\n\n")   
            
        
        
        
        #pygame.display.flip()
        #pygame.draw.rect(ventana,(13,17,237), jugador.GetTodo())
        #ventana.blit(pygame.image.load("sprites/nave.png"),jugador.GetTodo())
        #pygame.display.update()#actualizar ventana
        
        Dibujar(ventana,listaDisparos,listaEntidades)
        
        
        
        print(gc.isenabled())
        Clock.tick(FPS)

    
    
pygame.quit()     





"""clase encargas de manejar hojas de sprites"""
class HojaSprites:
    def __init__(self,NombreArchivo,columnas,filas):
        self.Hoja=pygame.image.load(NombreArchivo).convert_alpha()
        self.Columnas=columnas
        self.Filas=filas
        self.TotalDeCeldas=columnas*filas
        
        self.rect=self.Hoja.get_rect()
        Ancho=self.cellWidth=self.rect.whidth/columnas
        Alto=self.cellHeight=self.rect.height/filas
        
        self.cells=list([(index%cols*Ancho,index/columnas*Alto,Ancho,Alto)for index in range (self.TotalDeCeldas)])
        
    def dibujar(self,superficie,indice,XY):
        superficie.blit(self.Hoja,(XY[0],XY[1]),self.cells[indice])
        
        
        

        
