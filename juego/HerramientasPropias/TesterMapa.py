import pygame
pygame.init()
"""pygame inicializado"""
import ctypes
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
ancho,alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
alto=alto-56
"""tamaño de pantalla obtenido"""
import json
import sys
import os
"""librerias utiles para almacenar datos"""
Clock = pygame.time.Clock()
intervalo=60
"""datos del reloj declarados"""
run=True
Archivo=open("Path","w")
"""archivo para guardar"""
Tiempo=0
Cuadros=0
"""contadores"""
ventana= pygame.display.set_mode((ancho,alto),pygame.FULLSCREEN)
pygame.display.set_caption("PathGenTool")
"""ventana inicializada"""
MouseClic=False
"""flags"""
CoordenadaAnterior=(-100,-100)
diccionario={}
PathList=[]
NewDicct=True
"""buffer"""
intervalo=60
fuente=pygame.font.SysFont(None,25)
AMARILLO=(255,255,0)
NEGRO=(0,0,0)
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
        self.Aux=None
    def obtener(self,indice):
        self.Aux=self.Hoja.subsurface(self.cells[indice])
        return self.Aux
    def rotar(self,angulo):
        self.Aux=pygame.transform.rotate(self.Aux,angulo)
        pass
    def reflejar(self,Mirror):
        self.Aux=pygame.transform.flip(self.Aux,Mirror,False)
        pass
    def dibujar(self,superficie,indice,angulo,mirror,XY):
        print(indice)
        self.obtener(indice)
        self.rotar(angulo)
        self.reflejar(mirror)
        superficie.blit(self.Aux,(XY[0],XY[1]))
        pass
        
        
SubCeldas=HojaSprites("SubCeldas.png",4,4)
class posicion:
    def __init__(self,XY:list,index:int,angulo:int,Mirror:bool):
        
        a=[]
        a.append(int(XY[0]/32)*32)
        a.append(int(XY[1]/32)*32)
        
        self.Coordenadas=a
        self.Index=index
        self.Angulo=Angulo
        self.Reflejo=Mirror
    def GetCoordenadas(self):
        return self.Coordenadas
    def GetIndex(self):
        return self.Index
    def GetAngulo(self):
        return self.Angulo
    def GetMirror(self):
        return self.Reflejo
        
        
        
        
temp=None
        
#def Dibujar(self,ventana,ListaDebug,ListaCells,temp):
    
    
    #pass





Angulo=0
Mirror=False
Index=0
ListaCells=[]











while run:
    
    keys = pygame.key.get_pressed()
    Mx,My=pygame.mouse.get_pos()
    if Cuadros!=intervalo:
        Cuadros=Cuadros+1
    else:
        Tiempo=Tiempo+1
        Cuadros=0
        
    temp=posicion((Mx,My),Index,Angulo,Mirror)
    """cronometro"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_i:
                Index=Index+1
                Index=Index%16
            if event.key==pygame.K_r:
                Angulo=Angulo+90
                Angulo=Angulo%360
            if event.key==pygame.K_m:
                Mirror=not Mirror 
            if event.key==pygame.K_a:
                ListaCells.append(posicion((Mx,My),Index,Angulo,Mirror))
            if event.key==pygame.K_BACKSPACE:
                ListaCells.pop(len(ListaCells)-1)
            if event.key==pygame.K_ESCAPE:
                run=False
                
                
            
    
    
        
    
    #if keys[pygame.K_i]:#########################################Zona control angulo, indice,reflejo,lista cells
        #Index=Index+1                                           #
        #Index=Index%16                                          #
    #if keys[pygame.K_r]:                                        #
        #Angulo=Angulo+90                                        #
        #Angulo=Angulo%360                                       #
    #if keys[pygame.K_m]:                                        #
        #Mirror=not Mirror                                       #
    #if keys[pygame.K_a]:                                        #
        #ListaCells.append(posicion((Mx,My),Index,Angulo,Mirror))#
    #if keys[pygame.K_BACKSPACE]:                                #
        #ListaCells.pop(len(ListaCells)-1)########################
    #if keys[pygame.K_ESCAPE]:##salir
        #run=False
    
        
        
    ListaDebug=[]
    ListaDebug.append(dict(Texto=fuente.render("(Mx,My)="+str((Mx,My)),True,AMARILLO,NEGRO),Y=0))
    ListaDebug.append(dict(Texto=fuente.render("INDEX=:"+str(Index),True,AMARILLO,NEGRO),Y=25))
    ListaDebug.append(dict(Texto=fuente.render("ANGULO=:"+str(Angulo),True,AMARILLO,NEGRO),Y=50))
    ListaDebug.append(dict(Texto=fuente.render("Mirror=:"+str(Mirror),True,AMARILLO,NEGRO),Y=50))
    
    
    
    #Dibujar(ventana,ListaDebug,ListaCells,temp)
    
    
    
    ventana.fill(NEGRO)
    
    for Texto in ListaDebug:
        ventana.blit(Texto.get("Texto"),(0,Texto.get("Y")))
    for cell in ListaCells:
        SubCeldas.dibujar(ventana,cell.GetIndex(),cell.GetAngulo(),cell.GetMirror(),cell.GetCoordenadas())
    SubCeldas.dibujar(ventana,temp.GetIndex(),temp.GetAngulo(),temp.GetMirror(),temp.GetCoordenadas())
    pygame.display.update()
    Clock.tick(intervalo)


pygame.quit() 
    

