# -*- coding: latin-1 -*-
"""plantilla de objeto python"""
from Armas import ArmaEstandarApuntada


class Jefe1 :
    # recordar siempre declarar self en una funcion de objeto
    def __init__ ( self , pSpawn , velocidad , alturaAtaque ,info
                    ) :
        """

        :type info: list
        """
        self.Vida = 500000
        self.XY = pSpawn.copy ( )
        self.AlturaAtaque = alturaAtaque
        self.C1 = ArmaEstandarApuntada ( 80 , "Enemigo" )
        self.C2 = ArmaEstandarApuntada ( 80 + 60 , "Enemigo" )
        self.C3 = ArmaEstandarApuntada ( 80 + 120 , "Enemigo" )
        self.C4 = ArmaEstandarApuntada ( 80 + 180 , "Enemigo" )
        self.C5 = ArmaEstandarApuntada ( 80 + 240 , "Enemigo" )
        self.C6 = ArmaEstandarApuntada ( 80 + 300 , "Enemigo" )
        self.C7 = ArmaEstandarApuntada ( 80 + 360 , "Enemigo" )
        self.C8 = ArmaEstandarApuntada ( 80 + 420 , "Enemigo" )
        self.Velocidad = velocidad
        self.AlturaAtaque = alturaAtaque
        self.Index = 0
        self.Tipo = "JEFE"
        self.Alianza = "Enemigo"
        self.Tamaño = "JEFE"
        self.InfoEntregada=False
        self.Info=info
        print(info)
        print(self.Info)

    def GetAlianza ( self ) -> str :
        return self.Alianza
    def GetTamaño ( self ) :
        return self.Tamaño
        """obtener tamaño"""

    def GetX ( self ) :
        return self.XY[ 0 ]

    def GetCentro ( self ) :
        return (self.XY[ 0 ] + 32 , self.XY[ 1 ] + 37)

    def GetY ( self ) :
        return self.XY[ 1 ]

    def GetTipo ( self ) :
        return self.Tipo

    def Dañar ( self , daño ) :
        self.Vida = self.Vida - daño
        pass

    def Fin ( self ) :
        # print (self.XY[0]==3000 and self.XY[1] == 3000,"destruir")
        return self.Vida < 0 and self.InfoEntregada
    def EntregarInfo( self ):
        if self.Vida < 0:
            self.InfoEntregada=True
            print(self.Info)
            return self.Info
        else:
            return []
        #if

    def GetTodo ( self ) :
        return (self.XY[ 0 ] , self.XY[ 1 ])

    def GetIndex ( self ) :
        return self.Index

    def Actualizar ( self , objetivo ) :
        # print("tiempo=",self.TExistencia,"\n")
        aux = [ ]
        if self.XY[ 1 ] < self.AlturaAtaque :
            self.XY[ 1 ] = self.AlturaAtaque + self.Velocidad
        else :
            self.C1.Apuntar ( [self.XY[0]+157,self.XY[1]+352] ,
                              objetivo )
            self.C1.Actualizar ( )
            self.C2.Apuntar ( [self.XY[0]+292,self.XY[1]+334] ,
                              objetivo )
            self.C2.Actualizar ( )
            self.C3.Apuntar ( [self.XY[0]+354,self.XY[1]+352] ,
                              objetivo )
            self.C3.Actualizar ( )
            self.C4.Apuntar ( [self.XY[0]+218,self.XY[1]+334] ,
                              objetivo )
            self.C4.Actualizar ( )
            self.C5.Apuntar ( [self.XY[0]+337,self.XY[1]+342] ,
                              objetivo )
            self.C5.Actualizar ( )
            self.C6.Apuntar ( [self.XY[0]+196,self.XY[1]+338] ,
                              objetivo )
            self.C6.Actualizar ( )
            self.C7.Apuntar ( [self.XY[0]+313,self.XY[1]+338],
                              objetivo )
            self.C7.Actualizar ( )
            self.C8.Apuntar ( [self.XY[0]+174,self.XY[1]+342] ,
                              objetivo )
            self.C8.Actualizar ( )
            for disparo in self.C1.Disparar ( [self.XY[0]+157,self.XY[1]+352]) :
                aux.append ( disparo )
            for disparo in self.C2.Disparar ( [self.XY[0]+292,self.XY[1]+334] ) :
                aux.append ( disparo )
            for disparo in self.C3.Disparar ( [self.XY[0]+354,self.XY[1]+352] ) :
                aux.append ( disparo )
            for disparo in self.C4.Disparar ( [self.XY[0]+218,self.XY[1]+334] ) :
                aux.append ( disparo )
            for disparo in self.C5.Disparar ( [self.XY[0]+337,self.XY[1]+342] ) :
                aux.append ( disparo )
            for disparo in self.C6.Disparar ( [self.XY[0]+196,self.XY[1]+338] ) :
                aux.append ( disparo )
            for disparo in self.C7.Disparar ( [self.XY[0]+313,self.XY[1]+338] ) :
                aux.append ( disparo )
            for disparo in self.C8.Disparar ( [self.XY[0]+174,self.XY[1]+342] ) :
                aux.append ( disparo )
        return aux
