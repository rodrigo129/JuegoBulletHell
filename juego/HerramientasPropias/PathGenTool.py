import pygame
pygame.init()
"""pygame inicializado"""
import ctypes
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
ancho,alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
alto=alto-40
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
ventana= pygame.display.set_mode((700,700))
pygame.display.set_caption("PathGenTool")
"""ventana inicializada"""
MouseClic=False
"""flags"""
CoordenadaAnterior=(-100,-100)
diccionario={}
PathList=[]
NewDicct=True
"""buffer"""
while run:
    if Cuadros!=intervalo:
        Cuadros=Cuadros+1
    else:
        Tiempo=Tiempo+1
        Cuadros=0
    """cronometro"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        #if event.type == pygame.MOUSEBUTTONDOWN:
            
        #if event.type == pygame.MOUSEBUTTONUP:
           # MouseClic=False
    
    EstadoMouse=pygame.mouse.get_pressed()        
    
    Mx,My=pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    mouse = pygame.MOUSEBUTTONDOWN
    #print (mouse)
    #print(Mx,My)
    #print (EstadoMouse)
    if EstadoMouse[0]:
        MouseClic=True
        
        NewDicct=True
    else :
        print("si")
        MouseClic=False
        if len(diccionario)>0:
            PathList.append(diccionario)
        #if NewDicct:
           # PathList.append(diccionario)
          #  Tiempo=0
          #  Cuadros=0
          #  NewDicct=False
        diccionario={}
    if MouseClic and( CoordenadaAnterior != (Mx,My)):
        #print(Mx,My)
        a=(Mx,My)
        diccionario[Tiempo*60+Cuadros]=a
        CoordenadaAnterior=(Mx,My)
    """obtener posision del mouse"""
    """eventos"""
    if keys[pygame.K_ESCAPE]:##salir
        run=False
    Clock.tick(intervalo)
Archivo.write(json.dumps(PathList,indent=4))
Archivo.close()
pygame.quit() 
    
