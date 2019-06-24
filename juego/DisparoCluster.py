"""
    @author: Rodrigo Vargas
    modulo encargado del comportamiento de los disparos fragmentables
"""

from DisparoLinia import *


class DCluster ( Disparo ) :
    """disparo al que se le entrega una cantidad y un tiempo
       al paso del tiempo crea disparos de linia en un circulo
       repartido de manera simetrica
      Attributes:
        XY (list):coordenadas (x,y) del disparo
        Velocidad (int):velocidad del disparo
        Index(int):indice sprite del disparo
        VelocidadFinal(int):velocidad maxima del disparo
        Aceleracion(float):acceleracion del disparo
        Daño(int):daño del disparo
        Tipo(str):tipo de sprite que tiene el disparo
        Continuo(bool):indica si el disparo puede producir otros
        disparos
        Fin(bool):indica si el disparo tiene que eliminarse
        Constante(int):fin del contador del tiempo
        Angulo(int):angulo de 0 a 360 grados, direccion de movimiento
        Tiempo(int):contador
        Desfase(int):desfase en los disparos generados
        VelocidadDisparos(int): velocidad disparos generados
        Alianza(str):bando al que pertenece
        NDisparos(int):numero de disparos a generar
    """
    # recordar siempre declarar self en una funcion de objeto
    #
    Index = 8

    def __init__ ( self , xy , tiempo , angulo , velocidad ,
                   aceleracion , velocidadFinal , indices: list , daño ,
                   nDisparos , desfase , velocidadDisparos , alianza ) :
        self.XY = xy
        self.Constante = tiempo
        self.Angulo = angulo
        self.Tiempo = 0
        self.Velocidad = velocidad
        self.VelocidadFinal = velocidadFinal
        self.Aceleracion = aceleracion
        self.Indices = indices
        self.Daño = daño
        self.NDisparos = nDisparos
        self.Desfase = desfase
        self.VelocidadDisparos = velocidadDisparos
        self.Alianza = alianza

    def PasoTiempo ( self )  -> None:
        """
        funcion encargada de avanzar el tiempo de oscilacion
        :rtype: None
        """
        if self.Tiempo != self.Constante :
            self.Tiempo = self.Tiempo + 1
            pass

    def Actualizar ( self ) :
        """
        Returns:
            la funcion esta encargada de calcular las fisicas del
            disparo
            :rtype: None
        """
        self.XY = [ round ( self.XY [ 0 ] + self.Velocidad * math.cos (
            math.radians ( self.Angulo ) ) ) , round (
            self.XY [ 1 ] - self.Velocidad * math.sin (
                math.radians ( self.Angulo ) ) ) ]
        self.Accelerar ( )
        if self.Tiempo == self.Constante :
            self.Fin = True
            self.Continuo = True
        self.PasarTiempo ( )
        pass

    def GetSiguiente ( self ) :
        """
        retorna disparos si el disparo terminio su tiempo
        :rtype: object
        """
        aux = [ ]
        cont = round ( 360 / self.NDisparos )
        i = 0
        angulo = 0
        while i < self.NDisparos :
            aux.append (
                DLine ( [ self.XY [ 0 ] + 7 , self.XY [ 1 ] + 7 ] ,
                        angulo + self.Desfase , self.VelocidadDisparos ,
                        0 , self.Alianza , self.Indices [
                            int ( i % len ( self.Indices ) ) ] ) )
            i = i + 1
            angulo = angulo + cont

        return aux
