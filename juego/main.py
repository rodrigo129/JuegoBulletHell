import os
import sys
import wave

import pygame

# pygame.mixer.init(buffer=int(4096))
# pygame.mixer.pre_init(buffer=int(4096/4))
pygame.init ( )
pygame.mixer.quit ( )

DirectoriSprites = os.path.join ( os.getcwd ( ) , "sprites" )

file_wav = wave.open (
    os.path.join ( DirectoriSprites , "Track_40.wav" ) )
frequency = file_wav.getframerate ( )

pygame.mixer.init ( frequency = frequency )
from Nave import *
from DisparoOnda import *
from Enemigos import *
from DisparoCluster import *
from DisparoEstatico import *
from JEFE import *

import json

sistema = (sys.platform).strip ( "1234567890" )
print ( sistema )

if sistema == "win" :
    print ( sistema == "win" )
    import ctypes

    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware ( )
    ancho , alto = user32.GetSystemMetrics (
        0 ) , user32.GetSystemMetrics ( 1 )
    AnchoMaximo = ancho
    AltoMaximo = alto
if sistema == "linux" :
    import subprocess

    cmd = [ 'xrandr' ]
    cmd2 = [ 'grep' , '*' ]
    p = subprocess.Popen ( cmd , stdout = subprocess.PIPE )
    p2 = subprocess.Popen ( cmd2 , stdin = p.stdout ,
                            stdout = subprocess.PIPE )
    p.stdout.close ( )

    resolution_string , junk = p2.communicate ( )
    resolution = resolution_string.split ( ) [ 0 ]
    resolution = resolution.decode ( "utf-8" )
    ancho , alto = resolution.split ( 'x' )
    AnchoMaximo = ancho
    AltoMaximo = alto

# user32.GetSystemMetrics(0)= ancho
# user32.GetSystemMetrics(1)=alto
flag = True
Estado = [ ]
# """lista estado juego"""
Clock = pygame.time.Clock ( )
# ancho,alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
AlturaNativa = 1024
AnchoNativo = 1920
AltoCeldaNativa = 64
AnchoCeldaNativa = 64
NCeldasAlto = 16
NCeldasAncho = 30
ancho = int ( ancho / AnchoCeldaNativa ) * AnchoCeldaNativa
alto = int ( alto / AltoCeldaNativa ) * AltoCeldaNativa
ModoVentana = True
# ancho=1260
# alto=720
fullScreen = True

AltoCelda = alto / NCeldasAlto
AnchoCelda = ancho / NCeldasAncho
EscaladoAlto = alto / AlturaNativa
EscaladoAncho = ancho / AnchoNativo
ProporcionEscaladoAlto = alto / AlturaNativa
ProporcionEscaladoAncho = ancho / AnchoNativo

VERDE = (0 , 255 , 0)
GRIS = (155 , 155 , 155)
ROJO = (255 , 0 , 0)

# print (alto)
# ancho=int(ancho/3)
# alto=alto-40
# lista de disparos
"""inicio"""
ventana = pygame.display.set_mode ( (ancho , alto) , pygame.FULLSCREEN )
# print (ventana.
pygame.display.set_caption ( "Bullet hell" )

ListaDebug = [ ]  #####lista para reservada para mostrar datos de debug
clock = True  # juego corriendo
jugador = Nave ( 64 , 64 )
vel = 10
# init fuente

AlturaFuente = int ( (25 * AltoCelda) / AltoCeldaNativa )
fuente = pygame.font.SysFont ( None , AlturaFuente )
# enemigo de prueba

debug = False
# Estado.append("Nivel 1")#temp
Estado.append ( "Inicio" )
Tiempo = 0
# variable para contar segundo, no avanza si hay un jefe en pantalla
FPS = 60
# varible
Cuadros = 0
listaDisparos = [ ]
# variable para contar cuadors, cada 60 se reinicia y Tiempo avanza
FramesEnNivel = 0

# sonido
# sonido=pygame.mixer.Sound("sprites/Track_40.wav")

pygame.mixer.music.load ( "sprites/Track_40.mp3" )


class HojaSprites :
    def __init__ ( self , NombreArchivo , columnas , filas ,
                   proporcion = (1.55 , 0.75) ) :
        self.Hoja = pygame.image.load (
            NombreArchivo ).convert_alpha ( )

        # self.Hoja=pygame.transform.scale(self.Hoja,(int(self.Hoja.get_size()[0]*proporcion[0]),int(self.Hoja.get_size()[1]*proporcion[1])))

        self.Hoja.set_alpha ( 0 )
        self.Columnas = columnas
        self.Filas = filas
        self.TotalDeCeldas = columnas * filas
        self.Rect = self.Hoja.get_rect ( )
        Ancho = self.cellWidth = self.Rect.width / columnas
        # print("ancho:",self.Rect.width)
        # print("ancho celda",self.Rect.width/columnas)
        Alto = self.cellHeight = self.Rect.height / filas
        # print("alto:",self.Rect.height)
        # print("alto celda",self.Rect.height/filas)
        self.cells = list ( [ (index % columnas * Ancho ,
                               int ( index / columnas ) * Alto , Ancho ,
                               Alto) for index in
                              range ( self.TotalDeCeldas ) ] )
        self.surfaces = [ ]
        for cell in self.cells :
            if proporcion != (1 , 1) :
                aux = self.Hoja.subsurface (
                    self.cells [ self.cells.index ( cell ) ] )
                aux = pygame.transform.scale ( aux , (
                    int ( aux.get_size ( ) [ 0 ] * proporcion [ 0 ] ) ,
                    int ( aux.get_size ( ) [ 1 ] * proporcion [ 1 ] )) )
                self.surfaces.append ( aux )
            else :
                aux = self.Hoja.subsurface (
                    self.cells [ self.cells.index ( cell ) ] )
                self.surfaces.append ( aux )

        # print("lista celdas:",self.cells)+}

        self.mask = list (
            [ pygame.mask.from_surface ( self.surfaces [ index ] ) for
              index in range ( self.TotalDeCeldas ) ] )
        self.Rect = list (
            [ self.surfaces [ index ].get_rect ( ) for index in
              range ( self.TotalDeCeldas ) ] )
        # for cell in self.cells:
        # cell.set_alpha(0)
        Ancho , Alto = self.surfaces [ 0 ].get_size ( )
        MitadAncho , MitdadAlto = self.cellCenter = (
            int ( Ancho / 2 ) , int ( Alto / 2 ))
        self.handle = list ( [
            (0 , 0) , (-MitadAncho , 0) , (-Ancho , 0) ,
            (0 , -MitdadAlto) , (-MitadAncho , -MitdadAlto) ,
            (-Ancho , -MitdadAlto) ,
            (0 , -Alto) , (-MitadAncho , -Alto) , (-Ancho , -Alto) , ] )

    def dibujar ( self , superficie , indice , XY , handle = 0 ) :
        superficie.blit ( self.surfaces [ indice ] , (
            XY [ 0 ] + self.handle [ handle ] [ 0 ] ,
            XY [ 1 ] + self.handle [ handle ] [ 1 ]) )
        pass

    def MaskSet ( self , indice: int , XY: list ) :
        # self.mask[indice].set_at(XY)
        return self.mask [ indice ]

    def RectSet ( self , indice: int , XY: list ) :
        return self.Rect [ indice ].copy ( ).move ( XY [ 0 ] ,
                                                    XY [ 1 ] )

    def GetHandle ( self , indice ) :
        return self.handle [ indice ]


class HojaSpritesRotables :
    def __init__ ( self , NombreArchivo , columnas , filas ,
                   proporcion = (0.75 , 1.25) ) :
        self.Hoja = pygame.image.load (
            NombreArchivo ).convert_alpha ( )
        self.Hoja.set_alpha ( 150 )
        self.Columnas = columnas
        self.Filas = filas
        self.TotalDeCeldas = columnas * filas
        self.Rect = self.Hoja.get_rect ( )
        Ancho = self.cellWidth = self.Rect.width / columnas
        # print("ancho:",self.Rect.width)
        # print("ancho celda",self.Rect.width/columnas)
        Alto = self.cellHeight = self.Rect.height / filas
        # print("alto:",self.Rect.height)
        # print("alto celda",self.Rect.height/filas)
        self.cells = list ( [ (index % columnas * Ancho ,
                               int ( index / columnas ) * Alto , Ancho ,
                               Alto) for index in
                              range ( self.TotalDeCeldas ) ] )  #
        # print("coso:",type(self.cells[0]))
        self.sprites = [ ]
        # print(len(self.cells))
        for cell in self.cells :
            rotaciones = [ ]

            angulo = 0
            while angulo < 360 :
                objetos = {}
                # print(angulo,"\n")

                aux = pygame.transform.rotate ( self.Hoja.subsurface (
                    self.cells [ self.cells.index ( cell ) ] ) ,
                    angulo )
                aux.set_alpha ( 0 )
                if proporcion != (1 , 1) :
                    aux = pygame.transform.scale ( aux , (
                        int ( aux.get_size ( ) [ 0 ] * proporcion [
                            0 ] ) ,
                        int ( aux.get_size ( ) [ 1 ] * proporcion [
                            1 ] )) )
                objetos [ "surface" ] = aux
                objetos [ "mask" ] = pygame.mask.from_surface (
                    pygame.transform.rotate ( self.Hoja.subsurface (
                        self.cells [ self.cells.index ( cell ) ] ) ,
                        angulo ) )
                objetos [ "rect" ] = pygame.transform.rotate (
                    self.Hoja.subsurface (
                        self.cells [ self.cells.index ( cell ) ] ) ,
                    angulo ).get_rect ( )
                Ancho , Alto = pygame.transform.rotate (
                    self.Hoja.subsurface (
                        self.cells [ self.cells.index ( cell ) ] ) ,
                    angulo ).get_size ( )
                MitadAncho , MitdadAlto = (
                    int ( Ancho / 2 ) , int ( Alto / 2 ))
                objetos [ "handles" ] = list ( [
                    (0 , 0) , (-MitadAncho , 0) , (-Ancho , 0) ,
                    (0 , -MitdadAlto) , (-MitadAncho , -MitdadAlto) ,
                    (-Ancho , -MitdadAlto) ,
                    (0 , -Alto) , (-MitadAncho , -Alto) ,
                    (-Ancho , -Alto) , ] )
                rotaciones.append ( objetos )
                angulo = angulo + 1
            self.sprites.append ( rotaciones )
        # print(len(self.sprites))
        # print(type(self.sprites))
        # print(len(self.sprites[0]))
        # print(type(self.sprites[0]))
        # print(len(self.sprites[0][0]))
        # print(type(self.sprites[0][0]))
        # print(self.sprites[0][0].keys())

        # self.mask=list([pygame.mask.from_surface(self.Hoja.subsurface(self.cells[index]))for index in range (self.TotalDeCeldas)])
        # self.Rect=list([self.Hoja.subsurface(self.cells[index]).get_rect()for index in range (self.TotalDeCeldas)])

    # MitadAncho, MitdadAlto = self.cellCenter = (int(Ancho / 2), int(Alto / 2))
    #  self.handle = list([
    #	(0, 0), (-MitadAncho, 0), (-Ancho, 0),
    #	(0, -MitdadAlto), (-MitadAncho, -MitdadAlto), (-Ancho, -MitdadAlto),
    #	(0, -Alto), (-MitadAncho, -Alto), (-Ancho, -Alto),])

    def dibujar ( self , superficie , indice , XY , angulo ,
                  handle = 4 ) :
        aux = self.sprites [ indice ] [ angulo ]
        superficie.blit ( aux.get ( "surface" ) , (
            XY [ 0 ] + aux.get ( "handles" ) [ handle ] [ 0 ] ,
            XY [ 1 ] + aux.get ( "handles" ) [ handle ] [ 1 ]) )
        pass

    def MaskSet ( self , indice: int , XY: list , angulo ,
                  handle = 4 ) :
        # self.mask[indice].set_at(XY)
        aux = self.sprites [ indice ] [ angulo ].get ( "mask" )

        return aux

    def RectSet ( self , indice: int , XY: list , angulo ,
                  handle = 4 ) :
        aux = self.sprites [ indice ] [ angulo ]
        return aux.get ( "rect" ).copy ( ).move (
            XY [ 0 ] + aux.get ( "handles" ) [ handle ] [ 0 ] ,
            XY [ 1 ] + aux.get ( "handles" ) [ handle ] [ 1 ] )


# exp=HojaSpritesRotables("sprites/nave.png",1,1)


# os.path.join(DirectoriSprites,


HojaDisparos = HojaSprites (
    os.path.join ( DirectoriSprites , "Disparos2.png" ) , 3 , 4 ,
    proporcion = (ProporcionEscaladoAncho , ProporcionEscaladoAlto) )
HojaEnemigos = HojaSprites (
    os.path.join ( DirectoriSprites , "Enemigos2.png" ) , 3 , 3 ,
    proporcion = (ProporcionEscaladoAncho , ProporcionEscaladoAlto) )
HojaEnemigosX128 = HojaSprites (
    os.path.join ( DirectoriSprites , "EnemigoX128.png" ) , 1 , 2 ,
    proporcion = (ProporcionEscaladoAncho , ProporcionEscaladoAlto) )
HojaPantallas = HojaSprites (
    os.path.join ( DirectoriSprites , "PInicio.png" ) , 1 , 3 ,
    proporcion = (ProporcionEscaladoAncho , ProporcionEscaladoAlto) )
HojaEnemigoEnTest = HojaSprites (
    os.path.join ( DirectoriSprites , "Test.png" ) , 2 , 2 ,
    proporcion = (ProporcionEscaladoAncho , ProporcionEscaladoAlto) )
HojaJugador = HojaSprites (
    os.path.join ( DirectoriSprites , "nave.png" ) , 1 , 1 ,
    proporcion = (ProporcionEscaladoAncho , ProporcionEscaladoAlto) )
HojaHUD = HojaSprites ( os.path.join ( DirectoriSprites , "HUD.png" ) ,
                        5 , 6 , proporcion = (
        ProporcionEscaladoAncho , ProporcionEscaladoAlto) )
HojaEnemigosRotablesX64 = HojaSpritesRotables (
    os.path.join ( DirectoriSprites , "EnemigosRotablesX64.png" ) , 1 ,
    1 ,
    proporcion = (ProporcionEscaladoAncho , ProporcionEscaladoAlto) )
HojaJefe1=HojaSprites (
    os.path.join ( DirectoriSprites , "JEFE1.png" ) , 1 , 1 ,
    proporcion = (ProporcionEscaladoAncho , ProporcionEscaladoAlto) )

# AnchoMaximo=30


def Dibujar ( self , SuperficiePrincipal , ListaEntidades ,
              ListaEsenarios = [ ] ) :
    # def __init__(self,SuperficiePrincipal,ListaDisparos=[],ListaEntidades=[],ListaEsenarios=[]): #cambiar a diccionarios
    # ventana.fill((0,0,0))
    ventana.fill ( (150 , 150 , 0) )

    # exp.dibujar(ventana,0,[700,700],90)
    for Sprite in ListaEsenarios :
        break  ##esenarios aun no definidos

    # print(len(ListaEntidades),"entidades\n")
    for Sprite in ListaEntidades :
        if Sprite.GetTamaño() == "JEFE":
            HojaJefe1.dibujar(ventana,Sprite.GetIndex(),
                              [Sprite.GetTodo ( ) [ 0 ] * ProporcionEscaladoAncho ,
                    Sprite.GetTodo ( ) [
                        1 ] * ProporcionEscaladoAlto ])
        if Sprite.GetTamaño ( ) == "64" :
            if Sprite.GetTipo ( ) == "Estatico" :
                HojaEnemigos.dibujar ( ventana , Sprite.GetIndex ( ) , [
                    Sprite.GetTodo ( ) [ 0 ] * ProporcionEscaladoAncho ,
                    Sprite.GetTodo ( ) [
                        1 ] * ProporcionEscaladoAlto ] )
            if Sprite.GetTipo ( ) == "Rotable" :
                HojaEnemigosRotablesX64.dibujar ( ventana ,
                                                  Sprite.GetIndex ( ) ,
                                                  [ Sprite.GetTodo ( ) [
                                                        0 ] * ProporcionEscaladoAncho ,
                                                    Sprite.GetTodo ( ) [
                                                        1 ] * ProporcionEscaladoAlto ] ,
                                                  Sprite.GetAngulo ( ) )
        if Sprite.GetTamaño ( ) == "128" :
            HojaEnemigosX128.dibujar ( ventana , Sprite.GetIndex ( ) , [
                Sprite.GetTodo ( ) [ 0 ] * ProporcionEscaladoAncho ,
                Sprite.GetTodo ( ) [ 1 ] * ProporcionEscaladoAlto ] )
            # print(1)
        # pygame.draw.rect(ventana,(0,0,180),Sprite.GetTodo())
    # print(len(listaDisparos),"if 0, error al dibujar")
    for Disparo in listaDisparos :
        # ventana.blit(pygame.image.load("sprites/exp.png"), Disparo.GetTodo())
        HojaDisparos.dibujar ( ventana , Disparo.GetIndex ( ) , [
            Disparo.GetTodo ( ) [ 0 ] * ProporcionEscaladoAncho ,
            Disparo.GetTodo ( ) [ 1 ] * ProporcionEscaladoAlto ] )
        # print(Disparo.GetTodo(),"disparo en pantalla    ")z
        # pass###por completar
    # a=pygame.image.load("sprites/nave.png")        zz
    # ventana.blit(pygame.image.load("sprites/nave.png"),jugador.GetTodo())
    HojaJugador.dibujar ( ventana , jugador.GetIndex ( ) , [
        jugador.GetTodo ( ) [ 0 ] * ProporcionEscaladoAncho ,
        jugador.GetTodo ( ) [ 1 ] * ProporcionEscaladoAlto ] )
    # pygame.draw.rect(ventana,(0,0,0),pygame.Rect(0,0,9z6,1080))
    pygame.draw.rect ( ventana , (0 , 0 , 0 , 0) ,
                       pygame.Rect ( 0 , 0 , AnchoCelda * 3 ,
                                     AltoCelda * 16 ) )
    pygame.draw.rect ( ventana , (0 , 0 , 0) ,
                       pygame.Rect ( 27 * AnchoCelda , 0 ,
                                     3 * AnchoCelda , AltoCelda * 16 ) )
    for Texto in ListaDebug :
        ventana.blit ( Texto.get ( "Texto" ) ,
                       (0 , Texto.get ( "Y" ) * AlturaFuente) )
    for info in jugador.GetHudInfo ( ) :
        # print(info)
        if type ( info ) == type ( 2 ) :
            HojaHUD.dibujar ( ventana , info ,
                              [ int ( 32 * ProporcionEscaladoAncho ) ,
                                int ( 448 * ProporcionEscaladoAlto ) ] )
        else :
            # print((info.get("X")*ProporcionEscaladoAncho))

            ventana.blit ( fuente.render ( info.get ( "Info" ) , True ,
                                           (0 , 255 , 0) ,
                                           (0 , 0 , 0) ) , (int (
                info.get ( "X" ) * ProporcionEscaladoAncho ) ,
                                                            info.get (
                                                                "Y" ) * AlturaFuente) )
        # print("WIP")
        # fuente.render("FPS:"+str(Clock.get_fps()),True,(255,255,0),(0,0,0))
        # ventana.blit(
    pygame.display.update ( )
    pass


listaEntidades = [ ]  # lista entidades sin contar al jugador
listaEntidadesAuxliar = [ ]  # lista a añadir en el siguiente cuadro entidades sin contar al jugador
# listaEntidades.append(Enemigo(32,32))


seleccion = 0
while clock :
    if Estado [ 0 ] == "Inicio" :
        pygame.mixer.music.fadeout ( 400 )
        for event in pygame.event.get ( ) :
            if event.type == pygame.QUIT :
                clock = False
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_UP :
                    seleccion = seleccion - 1
                if event.key == pygame.K_DOWN :
                    seleccion = seleccion + 1
                if event.key == pygame.K_z :
                    if seleccion == 0 :
                        jugador = Nave ( 64 , 64 )
                        Archivo="Formation"
                        # jugador.Reset()
                        Estado [ 0 ] = "Intermedio"
                        Estado.append ( "Nivel 1" )
                    if seleccion == 1 :
                        seleccion = 0
                        Estado [ 0 ] = "Opciones"
                        Estado.append ( "Inicio" )
                        PrimerCiclo = True
                    if seleccion == 2 :
                        clock = False
        if seleccion > 2 :
            seleccion = 0
        if seleccion < 0 :
            seleccion = 2
        HojaPantallas.dibujar ( ventana , seleccion , [ 0 , 0 ] )
        pygame.display.update ( )
    if Estado [ 0 ] == "Opciones" :
        # Estado.pop(0)
        if PrimerCiclo :
            bufferParntalla = (ancho , alto)
            bufferModo = ModoVentana
            # print(bufferParntalla)
            PrimerCiclo = False
        Texto = [ ]
        for event in pygame.event.get ( ) :

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_UP :
                    seleccion = seleccion - 2
                if event.key == pygame.K_DOWN :
                    seleccion = seleccion + 2
                if event.key == pygame.K_LEFT :
                    seleccion = seleccion - 1
                if event.key == pygame.K_RIGHT :
                    seleccion = seleccion + 1
                if event.key == pygame.K_z :
                    print ( AnchoMaximo >= 1920 )
                    print ( "condicion1:" ,
                            seleccion == 0 and AltoMaximo >= 1024 and AnchoMaximo >= 1920 )
                    print ( "condicion2:" ,
                            seleccion == 2 and AltoMaximo >= 720 and AnchoMaximo >= 1260 )
                    if seleccion == 0 and AltoMaximo >= 1024 and AnchoMaximo >= 1920 :
                        fullScreen = False
                        ancho = 1920
                        alto = 1024
                    if seleccion == 1 and AltoMaximo >= 1024 and AnchoMaximo >= 1920 :
                        fullScreen = True
                        ancho = 1920
                        alto = 1024
                    if seleccion == 2 and AltoMaximo >= 720 and AnchoMaximo >= 1260 :
                        fullScreen = False
                        ancho = 1260
                        alto = 720
                    if seleccion == 3 and AltoMaximo >= 720 and AnchoMaximo >= 1260 :
                        fullScreen = True
                        ancho = 1260
                        alto = 720
                    if seleccion == 4 :
                        fullScreen = False
                        ancho = AnchoMaximo
                        alto = AltoMaximo
                    if seleccion == 5 :
                        fullScreen = True
                        ancho = AnchoMaximo
                        alto = AltoMaximo
                    if seleccion == 6 :
                        Estado [ 0 ] = "Escalar"
                    if seleccion == 7 :
                        ancho , alto = bufferParntalla
                        fullScreen = bufferModo
                        PrimerCiclo = False
                        Estado.pop ( 0 )

        if seleccion > 7 :
            seleccion = 0
        if seleccion < 0 :
            seleccion = 7

        i = 0
        while i <= 7 :
            boton = {}
            if i < 2 :
                boton [ "Y" ] = 6
            elif i < 4 :
                boton [ "Y" ] = 7
            elif i < 6 :
                boton [ "Y" ] = 8
            elif i < 8 :
                boton [ "Y" ] = 9
            if i % 2 == 1 :
                if i != 7 :
                    boton [ "Texto" ] = "FullScreen"
                    boton [ "X" ] = 13
                else :
                    boton [ "Texto" ] = "Cancelar"
                    boton [ "X" ] = 14
                if i == seleccion :
                    if i < 2 :
                        if AltoMaximo >= 1024 and AnchoMaximo >= 1920 :
                            boton [ "Color" ] = VERDE
                        else :
                            boton [ "Color" ] = ROJO
                    elif i < 4 :
                        if AltoMaximo >= 720 and AnchoMaximo >= 1260 :
                            boton [ "Color" ] = VERDE
                        else :
                            boton [ "Color" ] = ROJO
                    else :
                        boton [ "Color" ] = VERDE
                else :
                    boton [ "Color" ] = GRIS

            else :
                if i != 6 :
                    boton [ "X" ] = 9
                else :
                    boton [ "X" ] = 8
                if i == seleccion :
                    if i < 2 :
                        if AltoMaximo >= 1024 and AnchoMaximo >= 1920 :
                            boton [ "Color" ] = VERDE
                        else :
                            boton [ "Color" ] = ROJO
                    elif i < 4 :
                        if AltoMaximo >= 720 and AnchoMaximo >= 1260 :
                            boton [ "Color" ] = VERDE
                        else :
                            boton [ "Color" ] = ROJO
                    else :
                        boton [ "Color" ] = VERDE
                else :
                    boton [ "Color" ] = GRIS
                if i == 0 :
                    boton [ "Texto" ] = "1920X1080"
                if i == 2 :
                    boton [ "Texto" ] = "1260X720"
                if i == 4 :
                    boton [ "Texto" ] = "Auto"
                if i == 6 :
                    boton [ "Texto" ] = "Acceptar"

            Texto.append ( boton )
            i = i + 1
        # print(Texto)
        # print(AnchoCelda,AltoCelda)
        # print(

        pygame.draw.rect ( ventana , (0 , 0 , 0 , 0) ,
                           pygame.Rect ( AnchoCelda * 7 ,
                                         AltoCelda * 2 ,
                                         AnchoCelda * 16 ,
                                         AltoCelda * 12 ) )
        for boton in Texto :
            # print("boton:",Texto.index(boton))
            # print(boton.get("X"),boton.get("Y"))

            ventana.blit (
                fuente.render ( boton.get ( "Texto" ) , True ,
                                boton.get ( "Color" ) , (0 , 0 , 0) ) ,
                (int ( boton.get ( "X" ) * AnchoCelda ) ,
                 boton.get ( "Y" ) * AltoCelda) )

        pygame.display.update ( )
        # print("update")

        Clock.tick ( 60 )

    if Estado [ 0 ] == "Recargar" :
        print ( "wip" )
        Estado [ 0 ] = "Inicio"
    if Estado [ 0 ] == "Intermedio" :
        pygame.mixer.music.play ( loops = -1 )
        # pygame.mixer.Channel(0).play(sonido,loops=-1)
        # sonido.play(loops=-1)
        listaEntidades = [ ]
        #listaEntidades.append(Jefe1([300,-500],10,10))
        listaDisparos = [ ]
        FramesEnNivel = 0
        f = open ( Archivo , "r" )
        EnemiSpawn = [ ]
        EnemiSpawn = json.loads ( f.read ( ) )
        f.close ( )
        # listaEntidades.append(Enemigo3([500,-125],10,300,-15))
        # listaEntidades.append(Enemigo5([200,-125],1000,10,250,3,60,"Enemigo"))
        # listaEntidades.append(Enemigo5([1200,-125],1000,10,250,3,60,"Enemigo"))
        Estado.pop ( 0 )
    if Estado [ 0 ] == "Escalar" :

        AlturaNativa = 1024
        AnchoNativo = 1920
        AltoCeldaNativa = 64
        AnchoCeldaNativa = 64
        NCeldasAlto = 16
        NCeldasAncho = 30
        ancho = int ( ancho / AnchoCeldaNativa ) * AnchoCeldaNativa
        alto = int ( alto / AltoCeldaNativa ) * AltoCeldaNativa

        AltoCelda = alto / NCeldasAlto
        AnchoCelda = ancho / NCeldasAncho
        EscaladoAlto = alto / AlturaNativa
        EscaladoAncho = ancho / AnchoNativo
        ProporcionEscaladoAlto = alto / AlturaNativa
        ProporcionEscaladoAncho = ancho / AnchoNativo
        ModoVentana = fullScreen
        HojaDisparos = HojaSprites ( "sprites/Disparos2.png" , 3 , 4 ,
                                     proporcion = (
                                         ProporcionEscaladoAncho ,
                                         ProporcionEscaladoAlto) )
        HojaEnemigos = HojaSprites ( "sprites/Enemigos2.png" , 3 , 3 ,
                                     proporcion = (
                                         ProporcionEscaladoAncho ,
                                         ProporcionEscaladoAlto) )
        HojaEnemigosX128 = HojaSprites ( "sprites/EnemigoX128.png" , 1 ,
                                         2 , proporcion = (
                ProporcionEscaladoAncho , ProporcionEscaladoAlto) )
        HojaPantallas = HojaSprites ( "sprites/PInicio.png" , 1 , 3 ,
                                      proporcion = (
                                          ProporcionEscaladoAncho ,
                                          ProporcionEscaladoAlto) )
        HojaEnemigoEnTest = HojaSprites ( "sprites/Test.png" , 2 , 2 ,
                                          proporcion = (
                                              ProporcionEscaladoAncho ,
                                              ProporcionEscaladoAlto) )
        HojaJugador = HojaSprites ( "sprites/nave.png" , 1 , 1 ,
                                    proporcion = (
                                        ProporcionEscaladoAncho ,
                                        ProporcionEscaladoAlto) )
        HojaHUD = HojaSprites ( "sprites/HUD.png" , 5 , 6 ,
                                proporcion = (ProporcionEscaladoAncho ,
                                              ProporcionEscaladoAlto) )
        HojaEnemigosRotablesX64 = HojaSpritesRotables (
            "sprites/EnemigosRotablesX64.png" , 1 , 1 , proporcion = (
                ProporcionEscaladoAncho , ProporcionEscaladoAlto) )
        HojaJefe1 = HojaSprites (
            os.path.join ( DirectoriSprites , "JEFE1.png" ) , 1 , 1 ,
            proporcion = (
            ProporcionEscaladoAncho , ProporcionEscaladoAlto) )
        if fullScreen :
            ventana = pygame.display.set_mode ( (ancho , alto) ,
                                                pygame.FULLSCREEN )
        else :
            ventana = pygame.display.set_mode ( (ancho , alto) )
        AlturaFuente = int ( (25 * AltoCelda) / AltoCeldaNativa )
        fuente = pygame.font.SysFont ( None , AlturaFuente )
        Estado.pop ( 0 )

    if Estado [ 0 ] == "Nivel 1" :

        if not jugador.TieneVidas ( ) :
            Estado [ 0 ] = "Inicio"

        for Condicion in EnemiSpawn :
            # print(lista)
            # print("spawn:",EnemiSpawn)
            # print("lista:",lista)
            # Condicion=lista#[0]
            # print("Condicion:",Condicion)
            # print()
            # print(Condicion)
            # print(Condicion.get("Contador"),Condicion.get("Repeticiones"))

            if Condicion.get ( "Contador" ) == Condicion.get (
                    "Repeticiones" ) :
                # print("error")
                #print ( Condicion )
                EnemiSpawn.pop ( EnemiSpawn.index ( Condicion ) )
                #print("quedan:",len(EnemiSpawn)," olas")
                #print ("falta:")
                #print(EnemiSpawn)
            else :

                if (Condicion.get ( "Inicio" ) + FramesEnNivel) % (

                        Condicion.get ( "TiempoRepeticion" )) == 0 :
                    print(Condicion.get ( "Inicio" ))
                    print(FramesEnNivel)
                    print(Condicion.get ( "TiempoRepeticion" ))
                    aux = 0
                    if Condicion.get ( "Tipo" ) == "Enemigo1" :
                        while aux < int (
                                Condicion.get ( "CantidadEnemigos" ) ) :
                            PathCorregido = {}
                            PathBase = list (
                                (Condicion.get ( "Path" )).keys ( ) )
                            cont = 0
                            for Path in PathBase :
                                PathCorregido [
                                    int ( Path ) + aux * Condicion.get (
                                        "Offset" ) ] = Condicion.get (
                                    "Path" ).get ( str ( Path ) )
                            # print(type(PathCorregido))
                            listaEntidades.append (
                                Enemigo ( PathCorregido , list (
                                    PathCorregido.keys ( ) ) ) )  # temporal. colocar monto de if para determiinar el tipo de enemigo
                            aux = aux + 1
                        Condicion [ "Contador" ] = Condicion.get (
                            "Contador" ) + 1
                    # Condicion["Contador"]=Condicion.get("Contador")+1
                    if Condicion.get ( "Tipo" ) == "Enemigo2" :
                        # print("enemigo2")
                        while aux < int (
                                Condicion.get ( "CantidadEnemigos" ) ) :
                            listaEntidades.append (
                                Enemigo2 ( Condicion.get ( "PSpawn" ) ,
                                           Condicion.get (
                                               "Velocidad" ) ,
                                           Condicion.get (
                                               "InicioAtaque" ) ) )
                            aux = aux + 1
                        Condicion [ "Contador" ] = Condicion.get (
                            "Contador" ) + 1
                    # Condicion["Contador"]=Condicion.get("Contador")+1
                    if Condicion.get ( "Tipo" ) == "Enemigo3" :
                        # print("enemigo2")
                        while aux < int (
                                Condicion.get ( "CantidadEnemigos" ) ) :
                            listaEntidades.append (
                                Enemigo3 ( Condicion.get ( "PSpawn" ) ,
                                           Condicion.get (
                                               "Velocidad" ) ,
                                           Condicion.get (
                                               "InicioAtaque" ) ,
                                           Condicion.get (
                                               "VelocidadAtaque" ) ) )
                            aux = aux + 1
                        Condicion [ "Contador" ] = Condicion.get (
                            "Contador" ) + 1
                    # Condicion["Contador"]=Condicion.get("Contador")+1
                    if Condicion.get ( "Tipo" ) == "Enemigo5" :
                        # print("enemigo2")
                        while aux < int (
                                Condicion.get ( "CantidadEnemigos" ) ) :
                            listaEntidades.append (
                                Enemigo5 ( Condicion.get ( "PSpawn" ) ,
                                           Condicion.get ( "Vida" ) ,
                                           Condicion.get (
                                               "Velocidad" ) ,
                                           Condicion.get ( "Radio" ) ,
                                           Condicion.get (
                                               "Constante" ) ,
                                           Condicion.get (
                                               "Duracion" ) ) )
                            aux = aux + 1
                        Condicion [ "Contador" ] = Condicion.get (
                            "Contador" ) + 1
                    if Condicion.get ( "Tipo" ) == "JEFE"        :
                        while aux < int (
                                Condicion.get ( "CantidadEnemigos" ) ) :
                            listaEntidades.append (
                                Jefe1 ( Condicion.get ( "PSpawn" ) ,
                                           Condicion.get (
                                               "Velocidad" ) ,
                                           Condicion.get (
                                               "InicioAtaque" ) ,
                                           Condicion.get (
                                               "Info" ) ) )
                            aux = aux + 1
                        Condicion [ "Contador" ] = Condicion.get (
                            "Contador" ) + 1
        FramesEnNivel = FramesEnNivel + 1
        Cuadros = Cuadros + 1
        # reiniciar ventana
        # ventana.fill((0,0,0))
        # pygame.time.delay(100)#reloj
        if Cuadros != 60 :
            Cuadros = Cuadros + 1
        else :
            Cuadros = 0
            Tiempo = Tiempo + 1
        # contado de segundos, se utilizara para sincronizar spawn de enemigos con avanze de nivel

        for event in pygame.event.get ( ) :
            if event.type == pygame.QUIT :
                clock = False
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_LCTRL :
                    jugador.CambiarModo ( )
                    """cambio de modo solo se tiene que activar una vez para activar o desactivar"""
                if event.key == pygame.K_F12 :  # debug
                    if debug :
                        debug = False

                    else :
                        debug = True
                        pygame.font.init ( )
                if event.key == pygame.K_F10 :
                    if FPS == 60 :
                        FPS = 1
                    else :
                        FPS = 60

        """revision salir"""
        # print("disparos :",len(listaDisparos))
        keys = pygame.key.get_pressed ( )

        if keys [ pygame.K_LSHIFT ] :
            jugador.Acelerar ( )
        else :
            jugador.Desacerelar ( )
        if keys [ pygame.K_q ] :  # and flag:

            # listaDisparos.append(DCluster(jugador.GetXY(),60,90,5,0.1,10,[7,10,11],500,180,0,10,jugador.GetAlianza()))
            listaDisparos.append ( DEstatico ( jugador.GetXY ( ) , 180 ,
                                               jugador.GetAlianza ( ) ) )

            # flag=False
            #
            # for disparo in jugador.DisparoSecundario():
            # listaDisparos.append(disparo)
        """velocidad de movimiento"""

        # if keys[K_F12]:#debug
        # if debug:
        #   debug=False
        # else:
        # debug=True

        if keys [ pygame.K_z ] :  # disparar onda
            listaDisparos.append ( Dsin (
                [ jugador.GetX ( ) + 10 , jugador.GetY ( ) + 35 ] , 64 ,
                "Jugador" ) )
        if keys [ pygame.K_x ] :  # disparar normal
            for disparo in jugador.DisparoPrimario ( ) :
                listaDisparos.append ( disparo )
            # listaDisparos.append(Disparo(jugador.GetX()+10,jugador.GetY()+35,(255,17,20)))

        if keys [ pygame.K_LEFT ] :
            if jugador.GetX ( ) > 0 + 64 * 3 :
                jugador.SetX (
                    jugador.GetX ( ) - jugador.GetVelocidad ( ) )
            else :
                jugador.SetX ( 64 * 3 )
        if keys [ pygame.K_ESCAPE ] :  ##salir
            Estado [ 0 ] = "Inicio"
        if keys [ pygame.K_RIGHT ] :
            if jugador.GetX ( ) < int (
                    1920 ) - 64 * 4 :  # 64 =ancho sprite
                jugador.SetX (
                    jugador.GetX ( ) + jugador.GetVelocidad ( ) )
            else :
                jugador.SetX (
                    int ( 1920 ) - 64 * 4 )  # 64 =ancho sprite
        if keys [ pygame.K_UP ] :
            if jugador.GetY ( ) > 0 :
                jugador.SetY (
                    jugador.GetY ( ) - jugador.GetVelocidad ( ) )
            else :
                jugador.SetY ( 0 )
        if keys [ pygame.K_DOWN ] :
            if jugador.GetY ( ) < int (
                    1024 - 64 ) :  # 64 =ancho sprite
                jugador.SetY (
                    jugador.GetY ( ) + jugador.GetVelocidad ( ) )
            else :
                jugador.SetY ( int ( 1024 - 64 ) )  # 64 =ancho sprite



        for entidad in listaEntidades :
            # print(type(entidad))                                                                        #
            listaDisparosEnemigos = entidad.Actualizar (
                jugador.GetCentro ( ) )  # enemigos disparando y apuntando
            # print(listaDisparosEnemigos)     #
            # pygame.draw.rect(ventana,(0,0,180),entidad.GetTodo())  #añadir a una funcion de dibujo            #
            for disparo in listaDisparosEnemigos :  #
                # print (len(listaDisparos))                                                                    #
                listaDisparos.append ( disparo )  #
        for entidad in listaEntidadesAuxliar :  # cosas a añadir el siguiente ciclo                               #
            listaEntidades.append ( entidad )  #
            listaEntidadesAuxliar.pop (
                listaEntidadesAuxliar.index ( entidad ) )  #
        for entidad in listaEntidades :
            if entidad.Fin ( ) :
                listaEntidades.pop (
                    listaEntidades.index ( entidad ) )  ###

        for entidad in listaEntidades :  ##colicion entidades disparos
            for disparo in listaDisparos :
                # print(disparo.EsFin())
                if disparo.EsFin ( ) :
                    listaDisparos.pop (
                        listaDisparos.index ( disparo ) )
                    break
                if entidad.GetAlianza ( ) != disparo.GetAlianza ( ) :
                    if entidad.GetTamaño ( ) == "64" :
                        if entidad.GetTipo ( ) == "Estatico" :
                            rectEnemigo = HojaEnemigos.RectSet (
                                entidad.GetIndex ( ) ,
                                [ entidad.GetX ( ) ,
                                  entidad.GetY ( ) ] )
                        if entidad.GetTipo ( ) == "Rotable" :
                            rectEnemigo = HojaEnemigosRotablesX64.RectSet (
                                entidad.GetIndex ( ) ,
                                [ entidad.GetX ( ) ,
                                  entidad.GetY ( ) ] ,
                                entidad.GetAngulo ( ) )
                    if entidad.GetTamaño ( ) == "128" :
                        rectEnemigo = HojaEnemigosX128.RectSet (
                            entidad.GetIndex ( ) ,
                            [ entidad.GetX ( ) , entidad.GetY ( ) ] )
                    if entidad.GetTamaño ( ) == "JEFE" :
                        rectEnemigo = HojaJefe1.RectSet (
                            entidad.GetIndex ( ) ,
                            [ entidad.GetX ( ) , entidad.GetY ( ) ] )
                    rectDisparo = HojaDisparos.RectSet (
                        disparo.GetIndex ( ) , disparo.GetXY ( ) )
                    if rectEnemigo.colliderect ( rectDisparo ) :
                        if entidad.GetTamaño ( ) == "64" :
                            if entidad.GetTipo ( ) == "Estatico" :
                                maskEnemigo = HojaEnemigos.MaskSet (
                                    entidad.GetIndex ( ) ,
                                    [ entidad.GetX ( ) ,
                                      entidad.GetY ( ) ] )
                            if entidad.GetTipo ( ) == "Rotable" :
                                maskEnemigo = HojaEnemigosRotablesX64.MaskSet (
                                    entidad.GetIndex ( ) ,
                                    [ entidad.GetX ( ) ,
                                      entidad.GetY ( ) ] ,
                                    entidad.GetAngulo ( ) )
                        if entidad.GetTamaño ( ) == "128" :
                            maskEnemigo = HojaEnemigosX128.MaskSet (
                                entidad.GetIndex ( ) ,
                                [ entidad.GetX ( ) ,
                                  entidad.GetY ( ) ] )
                        if entidad.GetTamaño ( ) == "JEFE" :
                            maskEnemigo = HojaJefe1.MaskSet (
                                entidad.GetIndex ( ) ,
                                [ entidad.GetX ( ) ,
                                  entidad.GetY ( ) ] )
                        maskDisparo = HojaDisparos.MaskSet (
                            disparo.GetIndex ( ) , disparo.GetXY ( ) )

                        # print(disparo.GetXY()[0]-entidad.GetX(),disparo.GetXY()[1]-entidad.GetY())
                        # print(disparo.GetXY()[0])
                        # print(type(disparo))
                        # print(entidad.GetX())
                        # print(disparo.GetXY()[1])
                        # print(entidad.GetY())

                        if maskEnemigo.overlap ( maskDisparo , (
                                disparo.GetXY ( ) [
                                    0 ] - entidad.GetX ( ) ,
                                disparo.GetXY ( ) [
                                    1 ] - entidad.GetY ( )) ) :
                            # print ("colision")
                            entidad.Dañar ( disparo.GetDaño ( ) )
                            if entidad.Fin ( ) :
                                listaEntidades.pop (
                                    listaEntidades.index ( entidad ) )
                                # print("error")
                            listaDisparos.pop (
                                listaDisparos.index ( disparo ) )
                            break
        for disparo in listaDisparos :
            if disparo.GetAlianza ( ) != jugador.GetAlianza ( ) :
                rectDisparo = HojaDisparos.RectSet (
                    disparo.GetIndex ( ) , disparo.GetXY ( ) )
                rectJugador = HojaJugador.RectSet (
                    jugador.GetIndex ( ) , jugador.GetXY ( ) )
                if rectJugador.colliderect ( rectDisparo ) :
                    maskDisparo = HojaDisparos.MaskSet (
                        disparo.GetIndex ( ) , disparo.GetXY ( ) )
                    maskJugador = HojaJugador.MaskSet (
                        jugador.GetIndex ( ) , jugador.GetXY ( ) )
                    if maskJugador.overlap ( maskDisparo , (
                            disparo.GetXY ( ) [ 0 ] - jugador.GetX ( ) ,
                            disparo.GetXY ( ) [
                                1 ] - jugador.GetY ( )) ) :
                        jugador.Dañar ( disparo.GetDaño ( ) )
                        listaDisparos.pop (
                            listaDisparos.index ( disparo ) )

        """resetear fondo"""
        jugador.Actualizar ( )
        for disparo in listaDisparos :
            disparo.Actualizar ( )
            if disparo.EsContinuo ( ) :
                for disp in disparo.GetSiguiente ( ) :
                    listaDisparos.append ( disp )
            if disparo.EsFin ( ) :
                listaDisparos.pop ( listaDisparos.index ( disparo ) )
            else :

                if disparo.GetY ( ) < -500 or disparo.GetY ( ) > 1024 + 50 or disparo.GetX ( ) < -150 or disparo.GetX ( ) > 1920 + 150 :
                    listaDisparos.pop (
                        listaDisparos.index ( disparo ) )
                """borrar disparos fuera de pantalla, por arriba"""

            # pygame.draw.rect(ventana,disparo.GetRGB(), disparo.GetTodo())###dibujar disparo

        if debug :
            # fuente=pygame.font.SysFont(None,25)
            ListaDebug = [ dict ( Texto = fuente.render (
                "disparos:" + str ( len ( listaDisparos ) ) , True ,
                (255 , 255 , 0) , (0 , 0 , 0) ) , Y = 0 ) ,
                dict ( Texto = fuente.render (
                    "FPS:" + str ( Clock.get_fps ( ) ) , True ,
                    (255 , 255 , 0) , (0 , 0 , 0) ) , Y = 1 ) ,
                dict ( Texto = fuente.render (
                    "DañoJugador:" + str (
                        jugador.GetDañoRecivido ( ) ) ,
                    True , (255 , 255 , 0) , (0 , 0 , 0) ) , Y = 2 ) ,
                dict ( Texto = fuente.render (
                    "FramesTotales:" + str ( FramesEnNivel ) , True ,
                    (255 , 255 , 0) , (0 , 0 , 0) ) , Y = 3 ) ]
            # ventana.blit(texto,(0,0))
            # ventana.blit(texto,(0,25))
            #print ( "paso\n\n\n\n\n\n" )

            # pygame.display.flip()
        # pygame.draw.rect(ventana,(13,17,237), jugador.GetTodo())
        # ventana.blit(pygame.image.load("sprites/nave.png"),jugador.GetTodo())
        # pygame.display.update()#actualizar ventana
        for enemigo in listaEntidades:
            if enemigo.GetTamaño() == "JEFE":
                info=enemigo.EntregarInfo()
                if len(info) != 0:
                    print("WIP")
                    if info[0] == "Fin":
                        Estado[0]="Inicio"
                    else:
                        Archivo=info[0]
                        Estado.append(Estado[0])
                        Estado[0]="Intermedio"
                        print("WIP")


        Dibujar ( ventana , listaDisparos , listaEntidades )

        Clock.tick ( FPS )

pygame.quit ( )

"""clase encargas de manejar hojas de sprites"""


class HojaSprites :
    def __init__ ( self , NombreArchivo , columnas , filas ) :
        self.Hoja = pygame.image.load (
            NombreArchivo ).convert_alpha ( )
        self.Columnas = columnas
        self.Filas = filas
        self.TotalDeCeldas = columnas * filas

        self.rect = self.Hoja.get_rect ( )
        Ancho = self.cellWidth = self.rect.whidth / columnas
        Alto = self.cellHeight = self.rect.height / filas

        self.cells = list ( [ (index % cols * Ancho ,
                               index / columnas * Alto , Ancho , Alto)
                              for index in
                              range ( self.TotalDeCeldas ) ] )

    def dibujar ( self , superficie , indice , XY ) :
        superficie.blit ( self.Hoja , (XY [ 0 ] , XY [ 1 ]) ,
                          self.cells [ indice ] )
