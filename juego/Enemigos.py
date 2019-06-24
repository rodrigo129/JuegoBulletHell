"""
    @author: Rodrigo Vargas
    modulos encargados del comportamiento los enemigos
"""
import math

from Armas import Anillo
from Armas import ArmaAtaqueTriangular
from Armas import ArmaBarrera
from Armas import ArmaEstandarApuntada



class Enemigo :
    """Enemigo simple, sigue un recorrido y dispara siempre que puede hacia el jugados"""
    alianza = "Enemigo"
    estado = None  ###añadir estados
    Modo = "Normal"
    Tipo = "Estatico"
    TExistencia = 0
    Tamaño = "64"

    # recordar siempre declarar self en una funcion de objeto
    def __init__ ( self , path: dict , keys: list ) :
        # print("algo",keys,"cosa")
        # print("path",path)
        self.PATH = path
        self.ListaKeys = keys
        self.XY = [ path.get ( self.ListaKeys [ 0 ] ) [ 0 ] ,
                    path.get ( self.ListaKeys [ 0 ] ) [
                        1 ] ]  ##añadir al constructor
        # self.y=500
        self.alto = None
        self.ancho = None
        self.ArmaPrimaria = ArmaEstandarApuntada ( 60 ,
                                                   "Enemigo" )  # intervalo entre disparo
        self.Index = 0
        self.Tiempo = 0
        self.TExistencia = 0
        self.Vida = 1200

    def GetAlianza ( self ) -> str :
        """
        indica a que bando pertence la entidad
        :rtype: str
        """
        return self.alianza

    def GetX ( self ) :
        return self.XY [ 0 ]
        """obtener x"""


    def GetCentro ( self ) :
        return (self.XY [ 0 ] + 32 , self.XY [ 1 ] + 37)
        """punto de apuntado para los enemigos"""

    def GetY ( self ) :
        return self.XY [ 1 ]
        """obtener y"""

    def GetTipo ( self ) :
        return self.Tipo

    def SetX ( self , X ) :
        self.XY [ 0 ] = X
        pass
        """set x"""

    def SetY ( self , Y ) :
        self.XY [ 1 ] = Y
        pass
        """set y"""

    def GetPosicion ( self ) :
        return (self.XY [ 0 ] , self.XY [ 1 ])
        """obtener posicion"""

    def GetTamaño ( self ) :
        return self.Tamaño
        """obtener tamaño"""

    def SetPosicion ( self , xy: list ) :
        self.XY = xy
        pass
        """mover posicion"""



    def Dañar ( self , daño ) :
        self.Vida = self.Vida - daño
        pass

    def Fin ( self ) :
        # print (self.XY[0]==3000 and self.XY[1] == 3000,"destruir")
        return (self.XY [ 0 ] == 3000 and self.XY [
            1 ] == 3000) or self.Vida < 0

    def GetTodo ( self ) :
        return (self.XY [ 0 ] , self.XY [ 1 ] , self.ancho , self.alto)
        """obtener tupla coordenadas y tamaño"""

    # def DisparoPrimario(self):##?no en uso?
    # return self.ArmaPrimaria.Disparar(self.Modo,self.GetY()+13,self.GetX()+20,23)
    def GetIndex ( self ) :
        return self.Index

    """disparar ametralladora"""

    def PasarTiempo ( self ) :
        self.Tiempo = self.Tiempo + 1
        if self.Tiempo / 2 == 1 :
            self.Tiempo = 0
            if self.Index == 0 :
                self.Index = 1
            else :
                self.Index = 0
        pass

    def Actualizar ( self , objetivo ) :
        # print("tiempo=",self.TExistencia,"\n")

        if self.TExistencia in self.ListaKeys :
            # print("posision X=",self.PATH.get((self.TExistencia))[0])
            self.SetX ( self.PATH.get ( (self.TExistencia) ) [ 0 ] )
            self.SetY ( self.PATH.get ( (self.TExistencia) ) [ 1 ] )
        aux = None
        self.PasarTiempo ( )
        self.ArmaPrimaria.Apuntar ( self.GetPosicion ( ) , objetivo )
        self.ArmaPrimaria.Actualizar ( )
        aux = self.ArmaPrimaria.Disparar ( self.XY.copy ( ) )
        if len ( aux ) == 1 :
            if self.Index == 0 :
                self.Index = 2
            else :
                self.Index = 3
        self.TExistencia = self.TExistencia + 1
        return aux

    # def ToString(self):
    #  pass
    # @classmethod
    # def FromString(cls,string:str,path:dict):
    # pass
    """actualizar estado de la Nave"""


"""enemigo estandar"""


class Enemigo2 :
    """enemigo que sigue la coordenada x del jugador, dispara 6
    disparos por ronda"""
    Tamaño = "64"
    Tipo = "Estatico"
    Index = 4
    Alianza = "Enemigo"

    def __init__ ( self , pInicio: list , velocidad: int ,
                   alturaAtaque: int ) :
        self.XY = pInicio.copy ( )
        self.XYAtaque = [ pInicio [ 0 ] , alturaAtaque ]
        self.Arma1 = ArmaAtaqueTriangular ( 45 , "Enemigo" , 270 , 30 )
        self.Arma2 = ArmaAtaqueTriangular ( 45 , "Enemigo" , 270 , 30 )
        self.Index = 4
        self.Tiempo = 0
        self.Vida = 1800
        self.Vel = velocidad

    def GetAlianza ( self ) -> str :
        return self.Alianza

    def GetIndex ( self ) :
        return self.Index

    def GetTipo ( self ) :
        return self.Tipo

    def GetX ( self ) :
        return self.XY [ 0 ]

    def GetY ( self ) :
        return self.XY [ 1 ]

    def GetPosicion ( self ) :
        return (self.XY [ 0 ] , self.XY [ 1 ])

    def Fin ( self ) :
        return self.Vida < 0

    def Dañar ( self , daño ) :
        self.Vida = self.Vida - daño
        pass

    def GetTodo ( self ) :
        return (self.XY [ 0 ] , self.XY [ 1 ])

    def GetTamaño ( self ) :
        return self.Tamaño

    def Actualizar ( self , objetivo ) :
        aux = [ ]
        self.Arma1.Actualizar ( )
        self.Arma2.Actualizar ( )
        if self.XY [ 1 ] < self.XYAtaque [ 1 ] :
            self.XY [ 1 ] = self.XY [ 1 ] + self.Vel
        else :
            if self.XY [ 0 ] + 5 < objetivo [ 0 ] :
                self.Index = 5
                self.XY [ 0 ] = self.XY [ 0 ] + self.Vel
            elif self.XY [ 0 ] - 5 > objetivo [ 0 ] :
                self.Index = 7
                self.XY [ 0 ] = self.XY [ 0 ] - self.Vel
            else :
                self.Index = 6
            if self.XY [ 0 ] - 20 < objetivo [ 0 ] or self.XY [
                0 ] + 20 > objetivo [ 0 ] :
                disparos1 = self.Arma1.Disparar (
                    [ self.XY [ 0 ] + 22 , self.XY [ 1 ] + 35 ] , 10 )
                disparos2 = self.Arma2.Disparar (
                    [ self.XY [ 0 ] + 39 , self.XY [ 1 ] + 35 ] , 10 )

                for disparo in disparos1 :
                    # print(disparo.GetTodo(),"disparo enemigo 2")
                    aux.append ( disparo )
                for disparo in disparos2 :
                    aux.append ( disparo )
                # print(len(aux))
        return aux


class Enemigo3 :
    """enemigo que va a una posiscion indicada y ataca a ciegas"""
    Tamaño = "128"
    Tipo = "Estatico"
    Index = 0
    Alianza = "Enemigo"

    def __init__ ( self , pInicio: list , velocidad: int ,
                   alturaAtaque: int , velocidadAtaque ) :
        self.XY = pInicio.copy ( )
        self.XYAtaque = [ pInicio [ 0 ] , alturaAtaque ]
        self.Arma1 = Anillo ( 270 , 0.5 , self.Alianza )
        self.Index = 0
        self.Tiempo = 0
        self.Vida = 12500
        self.Vel = velocidad
        self.VelocidadAtaque = velocidadAtaque

    def GetAlianza ( self ) -> str :
        return self.Alianza

    def GetIndex ( self ) :
        return self.Index

    def GetX ( self ) :
        return self.XY [ 0 ]

    def GetTipo ( self ) :
        return self.Tipo

    def GetY ( self ) :
        return self.XY [ 1 ]

    def GetPosicion ( self ) :
        return (self.XY [ 0 ] , self.XY [ 1 ])

    def Fin ( self ) :
        # print("Vida:",self.Vida)
        # print(self.Vida<0)
        return self.Vida < 0

    def Dañar ( self , daño ) :
        print ( "daño:" , daño )
        self.Vida = self.Vida - daño
        print ( "VidaRestante:" , self.Vida )
        pass

    def GetTodo ( self ) :
        return (self.XY [ 0 ] , self.XY [ 1 ])

    def GetTamaño ( self ) :
        return self.Tamaño

    def Actualizar ( self , objetivo ) :
        aux = [ ]
        self.Arma1.Actualizar ( )
        if self.XY [ 1 ] < self.XYAtaque [ 1 ] :
            self.XY [ 1 ] = self.XY [ 1 ] + self.Vel
        else :

            disparos1 = self.Arma1.Disparar (
                [ self.XY [ 0 ] + 22 , self.XY [ 1 ] + 35 ] , 5 )

            for disparo in disparos1 :
                # print(disparo.GetTodo(),"disparo enemigo 2")
                aux.append ( disparo )

        return aux


class Enemigo4 :
    """NO EN USO,INCOMPLETO, REQUIERE DisparoClusterAnidado"""
    pass


class Enemigo5 :
    """enemigo que busca al jugador, giera al rededor de el dejando
    disparos estaticos en el proceso """
    def __init__ ( self , xy , vida , velocidad , radio , constante ,
                   duracion ) :
        self.XY = xy.copy ( )
        self.Radio = radio
        self.Constante = constante
        self.Alianza = "Enemigo"
        self.Velocidad = velocidad
        self.Index = 0
        self.Angulo = 0
        self.I = 0
        handle = [ ]
        self.Tipo = "Rotable"
        self.Tamaño = "64"
        self.Vida = vida
        self.Modo = "Posicionar"
        self.Droper = ArmaBarrera ( constante , duracion , 500 , 7 ,
                                    self.Alianza )
        i = 0
        while i < 360 :
            handle.append (
                [ round ( radio * math.cos ( math.radians ( i ) ) ) ,
                  round ( -radio * math.sin ( math.radians ( i ) ) ) ] )
            i = i + 1
        self.Handle = handle

    pass

    def GetAlianza ( self ) -> str :
        return self.Alianza

    def GetIndex ( self ) :
        return self.Index

    def GetX ( self ) :
        return self.XY [ 0 ]

    def GetY ( self ) :
        return self.XY [ 1 ]

    def GetPosicion ( self ) :
        return (self.XY [ 0 ] , self.XY [ 1 ])

    def Fin ( self ) :
        return self.Vida < 0

    def Dañar ( self , daño ) :
        self.Vida = self.Vida - daño
        pass

    def GetTodo ( self ) :
        return (self.XY [ 0 ] , self.XY [ 1 ])

    def GetTamaño ( self ) :
        return self.Tamaño

    def GetTipo ( self ) :
        return self.Tipo

    def GetAngulo ( self ) :
        if self.Modo == "Posicionar" :

            return 180
        elif self.Modo == "Posicionar2" :
            return self.Angulo + 90
        else :
            return (self.Angulo + 270) % 360

    def Actualizar ( self , objetivo ) :
        aux = [ ]

        if self.Modo == "Posicionar" :
            if self.XY [ 1 ] + self.Velocidad < objetivo [ 1 ] :
                self.XY [ 1 ] = self.XY [ 1 ] + self.Velocidad
            else :
                self.XY [ 1 ] = objetivo [ 1 ]

                self.Modo = "Posicionar2"
                pass
        if self.Modo == "Posicionar2" :
            self.XY [ 1 ] = objetivo [ 1 ]
            if self.XY [ 0 ] > objetivo [ 0 ] :
                # entrada derecha
                self.Angulo = 180
                if self.XY [ 0 ] - objetivo [ 0 ] > self.Radio :
                    self.XY [ 0 ] = self.XY [ 0 ] - self.Velocidad

                    pass
                else :

                    self.XY [ 0 ] = objetivo [ 0 ] + self.Velocidad
                    self.Modo = "Girar"
                    self.Angulo = 0
                    pass

            else :
                # entrada izquierda
                self.Angulo = 0
                if objetivo [ 0 ] - self.XY [ 0 ] > self.Radio :
                    self.XY [ 0 ] = self.XY [ 0 ] + self.Velocidad

                    pass
                else :

                    self.XY [ 0 ] = objetivo [ 0 ] - self.Velocidad
                    self.Modo = "Girar"
                    self.Angulo = 180
                    pass

        if self.Modo == "Girar" :
            indice = round ( self.Angulo + (math.degrees ( (
                                                                       math.radians (
                                                                           360 ) * self.Radio - self.Velocidad) / self.Radio )) ) % 360
            if objetivo [ 0 ] > self.XY [ 0 ] :
                self.Angulo = indice = (indice) % 360

                # print(self.XY,[objetivo[0]+self.Handle[indice][0],objetivo[1]+self.Handle[indice][1]])

                self.XY = [
                    objetivo [ 0 ] + self.Handle [ indice ] [ 0 ] ,
                    objetivo [ 1 ] + self.Handle [ indice ] [ 1 ] ]
                self.Droper.Actualizar ( )
                disparos = self.Droper.Disparar ( self.XY )
                for disparo in disparos :
                    aux.append ( disparo )
            else :
                self.Angulo = indice = (indice) % 360
                self.XY = [
                    objetivo [ 0 ] + self.Handle [ indice ] [ 0 ] ,
                    objetivo [ 1 ] + self.Handle [ indice ] [ 1 ] ]
                self.Droper.Actualizar ( )
                disparos = self.Droper.Disparar ( self.XY )
                for disparo in disparos :
                    aux.append ( disparo )
                # print(len(aux))
        return aux
