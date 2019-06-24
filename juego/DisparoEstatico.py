"""
    @author: Rodrigo Vargas
    modulo encargado del comportamiento de los disparos estaticos
"""
from Disparo import *


class DEstatico ( Disparo ) :
    # recordar siempre declarar self en una funcion de objeto
    def __init__ ( self , xy: list , tiempo: int , alianza: str ,
                   daño = 400 , indice = 7 ) :
        """
        Args:
            xy: lista coordenadas (x,y)
            timpo:tiempo para que desaparesca el disparo
            alianza:bando del disparo
            daño:daño del disparo
            indice:indice del sprite del disparo
        :type xy: list
        :type tiempo: int
        :type alianza: str
        :type daño: int
        :type indice: int
        """
        self.XY = xy.copy ( )
        self.Daño = daño
        self.Constante = tiempo
        self.Tiempo = 0
        self.Index = indice
        self.Alianza = alianza

    def PasarTiempo ( self ) :
        """
                funcion encargada de avanzar el tiempo de oscilacion
                :rtype: None
        """
        if self.Tiempo != self.Constante :
            self.Tiempo = self.Tiempo + 1
        else :
            self.Fin = True
        pass

    def Actualizar ( self ) :
        """
                        Returns:
                            la funcion esta encargada de calcular las fisicas del
                            disparo
                            :rtype: None
                        """
        self.PasarTiempo ( )
        pass
