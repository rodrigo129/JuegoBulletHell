"""plantilla de objeto python"""
import random

from Armas import ArmaLaser
from Armas import ArmaNormal
from Escudo import Escudo
from Nucleo import Nucleo


class Nave :
    x = None  # coordenadas
    y = None
    ArmaPrimaria = None
    alto = None
    ancho = None
    Alianza = "Jugador"
    estado = None  ###añadir estados
    Modo = "Normal"
    Shift = False
    Index = 0
    Vidas = 3
    Daño = 0
    Velocidad = 10
    Core = Nucleo ( 5000 , 5000 )
    Barrera = Escudo ( 2000 , 100 , 20 , 2 , 100 , 5 )

    # recordar siempre declarar self en una funcion de objeto
    def __init__ ( self , Alto , Ancho ) :
        self.x = 850
        self.y = 950
        self.alto = Alto
        self.ancho = Ancho
        self.ArmaPrimaria = ArmaNormal ( 1500 , 2 ,
                                         "Jugador" )  # intervalo entre disparo
        self.ArmaSecundaria = ArmaLaser ( 1500 , 270 , "Jugador" , 0 )
        self.Core = Nucleo ( 5000 , 5000 )
        self.TiempoInmunidad = 60

    def Reset ( self ) :
        #print ( "error" )
        self.Vidas = self.Vidas - 1
        self.x = 850
        self.y = 950
        self.Core.Reset ( )
        self.Barrera.Reset ( )
        self.ArmaPrimaria.Reset ( )
        self.TiempoInmunidad = 60
        pass

    def GetHudInfo ( self ) :
        HudInfo = [ 29 , dict ( Info = "Vidas:" + str ( self.Vidas ) ,
                                X = 32 ,
                                Y = 26 ) ]
        self.TiempoInmunidad = self.TiempoInmunidad - 1
        for info in self.ArmaSecundaria.GetStatus ( ) :
            HudInfo.append ( info )
        for info in self.Core.GetStatus ( ) :
            HudInfo.append ( info )
        for info in self.Barrera.GetStatus ( ) :
            HudInfo.append ( info )
        for info in self.ArmaPrimaria.GetStatus ( ) :
            HudInfo.append ( info )

        if self.Velocidad != 10 :
            self.Core.Pedir ( 30 )
        else :
            self.Velocidad = 10
        self.Barrera.RecargarEnergia (
            self.Core.Pedir ( self.Barrera.PedirEnergia ( ) ) )
        return HudInfo
        # if

    def GetX ( self ) :
        return self.x
        """obtener x"""

    def GetAlianza ( self ) :
        return self.Alianza

    def CambiarModo ( self ) :  # añadir restriciones
        if self.Modo == "Normal" :
            self.Modo = "Sobrecarga"
            pass
        else :
            self.Modo = "Normal"
            pass

    def GetVelocidad ( self ) :
        return self.Velocidad

    def Acelerar ( self ) :
        if self.Core.Tiene ( 30 ) :
            self.Velocidad = 45
        pass

    def Desacerelar ( self ) :
        self.Velocidad = 10
        pass

    def GetDañoRecivido ( self ) :
        return self.Daño

    def GetCentro ( self ) :
        return (self.x + 32 , self.y + 37)
        """punto de apuntado para los enemigos"""

    def GetXY ( self ) :
        return [ self.x , self.y ]

    def GetY ( self ) :
        return self.y
        """obtener y"""

    def GetIndex ( self ) :
        return self.Index

    def SetX ( self , X ) :
        self.x = X
        pass
        """set x"""

    def SetY ( self , Y ) :
        self.y = Y
        pass
        """set y"""

    def GetPosicion ( self ) :
        return (self.x , self.y)
        """obtener posicion"""

    def GetTamaño ( self ) :
        return (self.ancho , self.alto)
        """obtener tamaño"""

    def SetPosicion ( self , X , Y ) :
        self.x = X
        self.y = Y
        pass
        """mover posicion"""

    def SetTamaño ( self , Alto , Ancho ) :
        self.alto = Alto
        self.ancho = Ancho
        pass
        """fijar tamaño"""

    def GetTodo ( self ) :
        return (self.x , self.y , self.ancho , self.alto)
        """obtener tupla coordenadas y tamaño"""

    def TieneVidas ( self ) :
        return self.Vidas >= 0

    def Dañar ( self , daño ) :
        if self.TiempoInmunidad > 0 :
            daño = 0
        resto = self.Barrera.Resistir ( daño )
        componentes = [ self.Barrera , self.ArmaPrimaria , self.Core ]
        proporcionRestante = 100
        for componente in componentes :
            if componente.EsFuncional ( ) :
                proporcion = (random.randint ( 0 ,
                                               proporcionRestante + 1 ) - 1) / 100
                # print("proporcion:",proporcion)
                # print(proporcion*100)
                componente.Dañar ( resto * proporcion )
                proporcionRestante = proporcionRestante - round (
                    proporcion * 100 )

        self.Barrera.Recargar ( )
        #print ( self.Core.Pedir ( self.Barrera.PedirEnergia ( ) ) )
        self.Barrera.RecargarEnergia (
            self.Core.Pedir ( self.Barrera.PedirEnergia ( ) ) )

        if not self.Core.EsFuncional ( ) :
            self.Reset ( )
        # proporcion=(random.randint(0,proporcionRestante+1)-1)/100

        # self.ArmaPrimaria.Dañar(0)
        # self.Core.Dañar(0)
        # print("DañoJugador",self.Daño)
        pass

    def DisparoPrimario ( self ) :
        if self.Modo == "Sobrecarga" and self.Core.Tiene ( 15 ) :
            self.Core.Pedir ( 15 )
            # return self.ArmaPrimaria.Disparar(self.Modo,[self.GetX()+20,self.GetY()+13],23)
        else :
            self.Modo = "Normal"

        return self.ArmaPrimaria.Disparar ( self.Modo ,
                                            [ self.GetX ( ) + 20 ,
                                              self.GetY ( ) + 13 ] ,
                                            23 )

    """disparar ametralladora"""

    def DisparoSecundario ( self ) :
        return self.ArmaSecundaria.Disparar ( [ self.x , self.y ] , 90 ,
                                              95 )

    def Actualizar ( self ) :
        self.ArmaPrimaria.Actualizar ( )
        # self.ArmaSecundaria.Actualizar([self.x,self.y])
        pass

    """actualizar estado de la Nave"""
