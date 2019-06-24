"""plantilla de objeto python"""

import math

from Disparo import Disparo


class Laser ( Disparo ) :
    # recordar siempre declarar self en una funcion de objeto
    Tipo = "Rotable"
    Continuo = True

    def __init__ ( self , xy: list , angulo: int , iteracion: int ,
                   alianza: str ) :
        self.XY = xy.copy ( )
        self.Angulo = angulo
        self.Iteracion = iteracion
        self.Alianza = alianza
        self.Daño = 0
        self.Index = 6
        self.Len = 14
        print ( "laserN°:" , iteracion )
        # print([round(self.XY[0]+math.cos(math.radians(self.Angulo))),round(self.XY[1]+math.sin(math.radians(self.Angulo)))])

        if iteracion > 0 :
            # print(self.XY)
            # print([round(self.XY[0]+self.Len*math.cos(math.radians(self.Angulo))),round(self.XY[1]+self.Len*math.sin(math.radians(self.Angulo)))])
            self.Continuacion = Laser ( [ round (
                self.XY [ 0 ] + self.Len * math.cos (
                    math.radians ( self.Angulo ) ) ) , round (
                self.XY [ 1 ] - self.Len * math.sin (
                    math.radians ( self.Angulo ) ) ) ] , self.Angulo ,
                                        self.Iteracion - 1 ,
                                        self.Alianza )
        else :
            self.Continuo = False
            self.Continuacion = None

    def GetSiguiente ( self ) :
        return self.Continuacion

    def SetFin ( self , fin ) :
        print ( "fin:" , fin )
        self.Fin = fin
        if type ( self.Continuacion ) != type ( None ) :
            self.Continuacion.SetFin ( fin )
            # print("cambio:",fin)

        pass

    def Recalcular ( self ) :
        print ( "test:" ,
                self.Iteracion > 0 and (type ( self.Continuacion )) == (
                    type ( None )) )
        print ( "test1:" , self.Iteracion > 0 )
        print ( "test2:" ,
                (type ( self.Continuacion )) == (type ( None )) )
        print ( "test3:" , type ( self.Continuacion ) )
        if (type ( self.Continuacion )) != (type ( None )) :
            self.Continuacion.Recalcular ( )
            pass

        if self.Iteracion > 0 and (type ( self.Continuacion )) == (
        type ( None )) :
            # print(self.XY)
            # print([round(self.XY[0]+self.Len*math.cos(math.radians(self.Angulo))),round(self.XY[1]+self.Len*math.sin(math.radians(self.Angulo)))])
            self.Continuacion = Laser ( [ round (
                self.XY [ 0 ] + self.Len * math.cos (
                    math.radians ( self.Angulo ) ) ) , round (
                self.XY [ 1 ] - self.Len * math.sin (
                    math.radians ( self.Angulo ) ) ) ] , self.Angulo ,
                                        self.Iteracion - 1 ,
                                        self.Alianza )
            self.Continuacion.Recalcular ( )
            self.Continuo = True
        pass

    def SetIndex ( self , indice ) :
        self.Index = indice
        pass

    # def SetFin
    def SetDaño ( self , daño ) :
        self.Daño = daño
        pass

    def SetXY ( self , xy ) :
        self.XY = [ round ( xy [ 0 ] + self.Len * math.cos (
            math.radians ( self.Angulo ) ) ) , round (
            xy [ 1 ] - self.Len * math.sin (
                math.radians ( self.Angulo ) ) ) ]
        pass

    def GetDaño ( self ) :
        self.Continuacion.SetFin ( True )
        if type ( self.Continuacion ) != type ( None ) :
            self.Continuacion.SetFin ( True )
        self.Continuacion = None
        return self.Daño

    def SetContinuo ( self , flag ) :
        self.Continuo = flag
        pass

    def Actualizar ( self ) :
        if self.Iteracion > 0 and (type ( self.Continuacion )) == (
        type ( None )) :
            # print(self.XY)
            # print([round(self.XY[0]+self.Len*math.cos(math.radians(self.Angulo))),round(self.XY[1]+self.Len*math.sin(math.radians(self.Angulo)))])
            self.Continuacion = Laser ( [ round (
                self.XY [ 0 ] + self.Len * math.cos (
                    math.radians ( self.Angulo ) ) ) , round (
                self.XY [ 1 ] - self.Len * math.sin (
                    math.radians ( self.Angulo ) ) ) ] , self.Angulo ,
                                        self.Iteracion - 1 ,
                                        self.Alianza )
            # self.Continuacion.Recalcular()
            self.Continuo = True
            self.Continuacion.SetContinuo ( True )
        if type ( self.Continuacion ) != type ( None ) :
            self.Continuacion.SetIndex ( self.Index )
            self.Continuacion.SetDaño ( self.Daño )
            self.Continuacion.SetXY ( self.XY )
            # self.Continuacion.SetFin(self.Fin)
        pass
