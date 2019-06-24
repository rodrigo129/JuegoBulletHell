"""
    @author: Rodrigo Vargas
    modulo encargado del comportamiento de los disparos de linea simples
"""

import math

from Disparo import *


class DLine ( Disparo ) :
    """
    disparos que avanzan en la direcion indicada por un angulo
    Attributes:
        XY (list):coordenadas (x,y)
        Velocidad (int):velocidad disparo
        Index (int):indice sprite
        Omega (int):angulo de 0 a 360 grados, direccion de movimiento
        Daño(int):daño del disparo
        VelocidadFinal(int):velocidad maxima del disparo
        Alianza(str):bando al que pertenece
    """
    XY = None
    # Index=9
    # Z#por implementar
    Omega = None
    # angulo
    Velocidad = -25  # añadir al constructor
    Aceleracion = None  # añadir a actualizar/constructor
    # Velocidad
    VelocidadFinal = 30

    def __init__ ( self , xy: list , angulo: int , velocidad: int ,
                   aceleracion: float ,
                   alianza: str , index: int ,
                   daño: int = 300 )  -> object:  # CoordenadaX,
        # CoordenadaY,Angulo,Color
        """
        Args:
            xy: lista coordenadas (x,y)
            angulo: entero indicado el angulo en en grados entre el intervalo [0,360]
            velocidad: velocididad de movimiento
            alianza: bando al que pertenece
            daño:daño que causa el disparo
            index: indice del sprite
        """
        # print(angulo)
        self.Daño = daño
        self.Alianza = alianza
        self.XY = xy.copy()
        self.Omega = angulo
        self.Index = index
        self.Velocidad = velocidad
        self.Aceleracion = aceleracion
        """crear disparo"""





    def GetOmega ( self )  -> int:
        """
        funcion que retorna el angulo de desplazamiento
        :rtype: int
        """
        return self.Omega
        """obtener omega"""






    def SetVel ( self , vel: int )  -> None:
        """
        funcion encargada de modificar la velocidad
        :rtype: None
        """
        self.Velocidad = vel
        pass
        """fijar Velociad"""

    def SetOmega ( self , angulo: int )  -> None:
        """
        funcion encargada de modificar el angulo de movimiento
        :rtype: None
        """
        self.Omega = angulo
        """fijar Omega"""


    def Actualizar ( self ) :
        """
                Returns:
                    la funcion esta encargada de calcular las fisicas del
                    disparo
                    :rtype: None
                """
        self.Accelerar ( )
        if self.GetOmega ( ) >= 360 :  # mas de una rotacion
            self.SetOmega ( self.GetOmega ( ) % 360 )

        if self.GetOmega ( ) == 0 :  ##angulo 0 grados
            self.SetX ( round ( self.GetX ( ) - self.GetVel ( ) ) )
            pass
        elif self.GetOmega ( ) < 90 :  ##angulo menor 90 grados
            self.SetX ( round (
                self.GetX ( ) - self.GetVel ( ) * math.cos (
                    math.radians ( self.GetOmega ( ) ) ) ) )
            self.SetY ( round (
                self.GetY ( ) + self.GetVel ( ) * math.sin (
                    math.radians ( self.GetOmega ( ) ) ) ) )
            pass
        elif self.GetOmega ( ) == 90 :  ##angulo 90 grados
            self.SetY ( round ( self.GetY ( ) + self.GetVel ( ) ) )
            pass
        elif self.GetOmega ( ) < 180 :  ##angulo menor 90 grados
            self.SetX ( round (
                self.GetX ( ) - self.GetVel ( ) * math.cos (
                    math.radians ( self.GetOmega ( ) ) ) ) )
            self.SetY ( round (
                self.GetY ( ) + self.GetVel ( ) * math.sin (
                    math.radians ( self.GetOmega ( ) ) ) ) )
            pass
        elif self.GetOmega ( ) == 180 :  ##angulo menor 90 grados
            self.SetX ( round ( self.GetX ( ) + self.GetVel ( ) ) )
            pass
        elif self.GetOmega ( ) < 270 :  ##angulo menor 90 grados
            self.SetX ( round (
                self.GetX ( ) + -self.GetVel ( ) * math.cos (
                    math.radians ( self.GetOmega ( ) ) ) ) )
            self.SetY ( round (
                self.GetY ( ) + self.GetVel ( ) * math.sin (
                    math.radians ( self.GetOmega ( ) ) ) ) )
            pass
        elif self.GetOmega ( ) == 270 :  ##angulo menor 90 grados
            self.SetY ( round ( self.GetY ( ) - self.GetVel ( ) ) )
            pass
        elif self.GetOmega ( ) < 360 :  ##angulo menor 90 grados
            self.SetX ( round (
                self.GetX ( ) - self.GetVel ( ) * math.cos (
                    math.radians ( self.GetOmega ( ) ) ) ) )
            self.SetY ( round (
                self.GetY ( ) + self.GetVel ( ) * math.sin (
                    math.radians ( self.GetOmega ( ) ) ) ) )
            pass
