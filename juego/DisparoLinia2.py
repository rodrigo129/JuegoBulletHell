"""
    @author: Rodrigo Vargas
    modulo encargado de disparos de linia complejos

    NO EN USO POR COMSUMO EXESIVO DE RECURSOS
"""
import math

from Disparo import *


class DLine2 ( Disparo ) :
    X = None
    Y = None
    Amplitud = None
    Index = 11
    # amplitud de la ondulacion
    # Z#por implementar
    Omega = None
    # angulo
    Velocidad = -10  # añadir al constructor
    # Velocidad
    Color = None
    Velocidad = None
    XVelocidad = None
    YVelocidad = None
    XYOobjetivo = None

    def __init__ ( self , XYA: list , XYO: list , Vel: list ,
                   ) :  # self,CoordenadaX,CoordenadaY,Lista CoordenadaObjetivo,Velicidad,Color##proximamente indice sprite
        """
        Args:
            XYA: lista coordenadas (x,y) actuales
            XYO: lista coordenadas (x,y) del objetivo
            Vel: velocidad de movimiento del disparo
        """
        self.X = XYA [ 0 ]
        self.Y = XYA [ 1 ]
        self.Tiempo = 0
        self.XYObjetivo = XYO
        self.Velocidad = Vel

        """crear disparo"""

    def GetX ( self ) :
        return self.X
        """obtener x"""

    def GetRGB ( self ) :
        return self.Color
        """obtener RGB"""

    def GetY ( self ) :
        return self.Y
        """obtener y"""

    def GetOmega ( self ) :
        return self.Omega
        """obtener omega"""

    def GetVel ( self ) :
        return self.Velocidad
        """obtener velocidad"""

    def SetX ( self , x ) :
        self.X = x
        pass
        """fijar X"""

    def SetY ( self , y ) :
        self.Y = y
        pass
        """fijar Y"""

    def SetVel ( self , vel ) :
        self.Velocidad = vel
        pass
        """fijar Velociad"""

    def SetOmega ( self , angulo ) :
        self.Omega = angulo
        """fijar Omega"""

    def CalcularOmega ( self ) :
        ################################################################################adaptar

        # print("Posicion disparo",self.X,self.Y,"D\n")
        # print("Posicion objetivo",self.XYObjetivo[0],self.XYObjetivo[1],"D\n")
        # print("angulo Disparo despues",self.Omega,"D\n")

        if self.X == self.XYObjetivo [ 0 ] :  # angulo 90 o 270
            if self.Y > self.XYObjetivo [ 1 ] :
                self.Omega = 90
            else :
                self.Omega = 270
        elif self.Y == self.XYObjetivo [ 1 ] :  # angulo 0 o 180
            if self.X > self.XYObjetivo [ 0 ] :
                self.Omega = 180
            else :
                self.Omega = 0
        else :  # angulo intermedio
            if self.Y > self.XYObjetivo [ 1 ] :
                if self.X < self.XYObjetivo [ 0 ] :
                    # print("cuadrante 1","arma")
                    self.Omega = math.degrees ( math.atan (
                        -(self.Y - self.XYObjetivo [ 1 ]) / (
                                    self.X - self.XYObjetivo [
                                0 ]) ) )  # +/-
                else :
                    # print("cuadrante 2","arma")
                    self.Omega = math.degrees ( math.atan (
                        -(self.Y - self.XYObjetivo [ 1 ]) / (
                                    self.X - self.XYObjetivo [
                                0 ]) ) ) + 180
            else :
                if self.X < self.XYObjetivo [ 0 ] :
                    # print("cuadrante 3","arma")
                    self.Omega = math.degrees ( math.atan (
                        (self.Y - self.XYObjetivo [ 1 ]) / (
                                    self.X - self.XYObjetivo [
                                0 ]) ) ) + 180
                else :
                    # print("cuadrante 4","arma")
                    self.Omega = abs ( math.degrees ( math.atan (
                        -(self.Y - self.XYObjetivo [ 1 ]) / (
                                    self.X - self.XYObjetivo [
                                0 ]) ) ) + 360 )

        if self.Omega >= 360 :  # correcion de angulo
            self.Omega = (self.Omega % 360)

        # print("angulo Disparo despues",self.Omega)

        # if self.Angulo <90 or self.Angulo>270:
        #  self.XYO=[1000000000,
        # round(1000000000*((XYPropio[1]-XYObjetivo[1])/XYPropio[0]-XYObjetivo[0]))]
        # elif elf.Angulo >90 or self.Angulo<270:
        # self.XYO=[-1000000000,
        # round(-1000000000*((XYPropio[1]-XYObjetivo[1])/XYPropio[0]-XYObjetivo[0]))]
        # elif elf.Angulo ==90:
        # self.XYO=[XYPropio[0],-1000000000]
        # elif elf.Angulo ==270:
        # self.XYO=[XYPropio[0],1000000000]
        pass
        ################################################################################
        """calcula Omega de manera dinamica"""

    def GetTodo ( self ) :  ##por mientas
        return (self.X , self.Y , 8 , 8)
        """obtener tupla de coordenadas"""

    def Actualizar ( self ) :
        self.CalcularOmega ( )

        if self.GetOmega ( ) == 0 :  ##angulo 0 grados
            self.SetX ( self.GetX ( ) - self.GetVel ( ) )
            pass
        elif self.GetOmega ( ) < 90 :  ##angulo menor 90 grados
            self.SetX ( int (
                self.GetX ( ) + self.GetVel ( ) * math.cos (
                    math.radians ( self.GetOmega ( ) ) ) ) )  #
            self.SetY ( int (
                self.GetY ( ) - self.GetVel ( ) * math.sin (
                    math.radians ( self.GetOmega ( ) ) ) ) )
            pass
        elif self.GetOmega ( ) == 90 :  ##angulo 90 grados
            self.SetY ( self.GetY ( ) + self.GetVel ( ) )
            pass
        elif self.GetOmega ( ) < 180 :  ##angulo menor 90 grados
            self.SetX ( int (
                self.GetX ( ) + self.GetVel ( ) * math.cos (
                    math.radians ( self.GetOmega ( ) ) ) ) )
            self.SetY ( int (
                self.GetY ( ) - self.GetVel ( ) * math.sin (
                    math.radians ( self.GetOmega ( ) ) ) ) )
            pass
        elif self.GetOmega ( ) == 180 :  ##angulo menor 90 grados
            self.SetX ( self.GetX ( ) + self.GetVel ( ) )
            pass
        elif self.GetOmega ( ) < 270 :  ##angulo menor 90 grados
            self.SetX ( int (
                self.GetX ( ) + self.GetVel ( ) * math.cos (
                    math.radians ( self.GetOmega ( ) ) ) ) )
            self.SetY ( int (
                self.GetY ( ) + -self.GetVel ( ) * math.sin (
                    math.radians ( self.GetOmega ( ) ) ) ) )
            pass
        elif self.GetOmega ( ) == 270 :  ##angulo menor 90 grados
            self.SetY ( self.GetY ( ) - self.GetVel ( ) )
            pass
        elif self.GetOmega ( ) < 360 :  ##angulo menor 90 grados
            self.SetX ( int (
                self.GetX ( ) - self.GetVel ( ) * math.cos (
                    math.radians ( self.GetOmega ( ) ) ) ) )
            self.SetY ( int (
                self.GetY ( ) + self.GetVel ( ) * math.sin (
                    math.radians ( self.GetOmega ( ) ) ) ) )
            pass
