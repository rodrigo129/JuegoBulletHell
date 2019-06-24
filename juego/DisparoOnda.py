"""
    @author: Rodrigo Vargas
    modulo encargado del comportamiento de los disparos oscilantes
"""
import math

from Disparo import *


class Dsin ( Disparo ) :
    """
        modulo encargado del comportamiento de los disparos con
        movimiento sinusoidal
    Attributes:
        XY (list):coordenadas (x,y)
        Velocidad (int):velocidad disparo
        Index (int):indice sprite
        Amplitud (int):amplitud de oscilacion
        Tiempo (int): contador de frames desde que se disparo
        Omega (int): constante 2*pi
        XR (int): coordenada x de oscilacion
        Daño(int):daño del disparo
        Alianza(str):bando al que pertenece
    """

    Index = 1
    Amplitud = None
    # amplitud de la ondulacion
    # Xreal

    # Z#por implementar
    Omega = 2 * math.pi
    # angulo
    Velocidad = -5  # añadir al constructor
    # Velocidad

    Tiempo = None

    # "tiempo"
    def __init__ ( self , xy: list , amp: int ,
                   alianza: str ) :  # añadir angulo Omega
        """
        Args:
            xy: lista coordenadas (x,y)
            amp: amplitud de oscilacion
            :rtype: object
        """
        self.Alianza = alianza
        self.XY = xy
        self.XR = xy[ 0 ]
        self.Tiempo = 0
        self.Amplitud = amp
        """crear disparo"""

    def GetXR ( self ) :
        return self.XR
        """obtener el x real"""

    def PasoTiempo ( self )  -> None:
        """
        funcion encargada de avanzar el tiempo de oscilacion
        :rtype: None
        """
        self.Tiempo = self.Tiempo + 1
        pass
        """pasa el tiempo"""

    def GetTiempo ( self )  -> int:
        """
        funcion encargada de retornar el tiempo
        :rtype: int
        """
        return self.Tiempo
        """retorna el tiempo"""



    def GetOmega ( self )  -> int:
        """
        funcion encargada de retornar la constante de oscilacion
        :rtype: int
        """
        return self.Omega



    def GetAmplitud ( self )  -> int:
        """
        funcion encargada de retornar la amplitud
        :rtype: int
        """
        return self.Amplitud
        """obtener amplitud"""

    def Actualizar ( self ) :
        """
                Returns:
                    la funcion esta encargada de calcular las fisicas del
                    disparo
                    :rtype: None
                """
        self.SetY ( self.GetY ( ) + self.GetVel ( ) )  ###adaptar
        self.SetX ( self.GetXR ( ) + int (
            self.GetAmplitud ( ) * math.sin (
                (self.GetOmega ( ) * self.GetTiempo ( )) / 90 ) ) )
        self.PasoTiempo ( )
        pass
        """actualizar datos"""
