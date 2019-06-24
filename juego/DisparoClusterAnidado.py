"""
    @author: Rodrigo Vargas
    modulo encargado del comportamiento de los disparos fragmentables

    MODULO INCOMPLETO Y NO EN USO
    disparos cluster aplicado a disparos cluster, con rotacion a los clusters"""
import math

from Disparo import *


class DCCluster ( Disparo ) :
    # recordar siempre declarar self en una funcion de objeto
    Index = 2

    def __init__ ( self , xy: list , tiempo: int , angulo: int ,
                   desfase: int , angulos: list , indices: list ,
                   velocidad: int , velocidadDisparos: int ,
                   nDisparos: int , nNDisparos: int ,
                   velocidadFinal: int , alianza: str ) :
        self.Tiempo = 0
        self.Constante = tiempo

    def PasarTiempo ( self ) :
        if self.Tiempo != self.Constante :
            self.Tiempo = self.Tiempo + 1
            pass

    def Actualizar ( self ) :
        self.XY = [ round ( self.XY [ 0 ] + self.Velocidad * math.cos (
            math.radians ( self.Angulo ) ) ) , round (
            self.XY [ 1 ] - self.Velocidad * math.sin (
                math.radians ( self.Angulo ) ) ) ]
        self.Accelerar ( )
        print ( "tiempo:" , self.Tiempo , "ob:" , self.Constante )
        if self.Tiempo == self.Constante :
            self.Fin = True
            self.Continuo = True
        self.PasarTiempo ( )
        pass

    def GetSiguiente ( self ) :
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
