"""
    @author: Rodrigo Vargas
    modulos encargados de los comportamientos de las armas
"""
"""
    modulo encargado del comportamiento de las armas
"""
import random

from DisparoEstatico import *
from DisparoLaser import *
from DisparoLinia import *
from DisparoLinia2 import *

"""arma principal del jugados"""


class ArmaNormal :  # apuntado manual
    # Modo="Normal"
    """
    Attributes:
        Cañon1 (int):indicador cañon diponible para disparar
        Cañon2 (int):indicador cañon diponible para disparar
        Constante (int):tiempo de recarga de cañon
        Tiempo (int):contador de recarga de cañon
        fase (int):indicador de turnos de cañon
    """
    # VidaMaximaCañon
    # VidaCañon1
    # VidaCañon2
    Cañon1 = 1
    Cañon2 = 0
    Constante = 5  # tiempo entre disparo
    Tiempo = 0
    fase = 1

    def __init__ ( self , vidaMaxima , constante , alianza ) :
        """

        :rtype: object
        """
        self.VidaMaximaCañon = vidaMaxima
        self.VidaCañon1 = vidaMaxima
        self.VidaCañon2 = vidaMaxima
        self.Constante = constante
        self.Alianza = alianza

    def Reset ( self ) :
        self.VidaCañon1 = self.VidaMaximaCañon
        self.VidaCañon2 = self.VidaMaximaCañon
        Cañon1 = 1
        Cañon2 = 0
        Tiempo = 0
        fase = 1
        pass

    @staticmethod
    def PedirEnergia () :
        return 50

    def EsFuncionalCañon1 ( self ) :
        return self.VidaCañon1 > 0

    def EsFuncionalCañon2 ( self ) :

        return self.VidaCañon2 > 0

    def Dañar ( self , daño ) :
        proporcion = (random.randint ( 0 , 101 ) - 1) / 100
        self.VidaCañon1 = self.VidaCañon1 - daño * proporcion
        self.VidaCañon2 = self.VidaCañon2 - daño * (1 - proporcion)
        pass

    def GetStatus ( self ) :
        aux = [ ]
        indice = self.VidaCañon1 / self.VidaMaximaCañon
        if indice > 0.75 :
            aux.append ( 13 )
        elif indice > 0.5 :
            aux.append ( 14 )
        elif indice > 0.25 :
            aux.append ( 15 )
        else :
            aux.append ( 16 )
        indice = self.VidaCañon2 / self.VidaMaximaCañon
        if indice > 0.75 :
            aux.append ( 17 )
        elif indice > 0.5 :
            aux.append ( 18 )
        elif indice > 0.25 :
            aux.append ( 19 )
        else :
            aux.append ( 20 )
        return aux

    def EsFuncional ( self ) :
        return self.EsFuncionalCañon1 ( ) or self.EsFuncionalCañon2 ( )

    def Disparar ( self , Modo , XYRelativo: list , XDesfase ) :
        ListaDisparos = [ ]
        # print("VidaC1:",self.VidaCañon1,"VidaC2:",self.VidaCañon2,"Test:",self.EsFuncional())
        if Modo == "Sobrecarga" :
            if self.Tiempo == self.Constante :
                self.Tiempo = 0
                if self.EsFuncionalCañon1 ( ) :
                    ListaDisparos.append (
                        Disparo ( XYRelativo , 15 , 0 , 15 ,
                                  self.Alianza ) )
                if self.EsFuncionalCañon2 ( ) :
                    ListaDisparos.append ( Disparo (
                        [ XYRelativo [ 0 ] + XDesfase ,
                          XYRelativo [ 1 ] ] , 15 , 0 , 15 ,
                        self.Alianza ) )
                return ListaDisparos
                """disparar Ambos Cañones"""
            else :
                return ListaDisparos
                """armas en Recarga"""
        elif Modo == "Normal" :
            if self.fase == 1 and self.Cañon1 == 1 :
                self.fase = 0
                self.Cañon1 = 0
                # Cañon2=1
                self.Tiempo = 0
                if self.EsFuncionalCañon1 ( ) :
                    ListaDisparos.append (
                        Disparo ( XYRelativo , 15 , 0 , 15 ,
                                  self.Alianza ) )
                return ListaDisparos
                """DispararCañon1"""
            elif self.fase == 0 and self.Cañon2 == 1 :
                self.fase = 1
                self.Cañon2 = 0
                self.Tiempo = 0
                if self.EsFuncionalCañon2 ( ) :
                    ListaDisparos.append ( Disparo (
                        [ XYRelativo [ 0 ] + XDesfase ,
                          XYRelativo [ 1 ] ] , 15 , 0 , 15 ,
                        self.Alianza ) )
                return ListaDisparos
                """DispararCañon2"""
            else :
                return ListaDisparos
                """armas en Recarga"""

    def Actualizar ( self ) :
        if self.Tiempo != self.Constante :
            self.Tiempo = self.Tiempo + 1
            pass
            """condador de frames de recarga"""
        elif self.Tiempo == self.Constante and self.fase == 1 :
            self.Cañon1 = 1
            pass
            """Cañon1 Recargado"""
        elif self.Tiempo == self.Constante and self.fase == 0 :
            self.Cañon2 = 1
            pass
            """Cañon2 Recargado"""
            """arma primaria jugador"""


"""arma apuntada simple del enemigo, tiene angulos siegos"""


class ArmaEstandarApuntada :  # apuntado simple
    Cañon1 = 1
    Constante = 60
    Tiempo = 0
    fase = 1
    Angulo = 0

    def __init__ ( self , constante: int , alianza: str ,
                   notStandby = False ) :
        self.Alianza = alianza
        self.Constante = constante
        if notStandby :
            self.Tiempo = self.Constante

    def Apuntar ( self , XYPropio: list , XYObjetivo: list ) :

        # print (XYPropio,XYObjetivo)
        if XYPropio [ 0 ] == XYObjetivo [ 0 ] :  # angulo 90 o 270
            if XYPropio [ 1 ] > XYObjetivo [ 1 ] :
                self.Angulo = 90
            else :
                self.Angulo = 270
        elif XYPropio [ 1 ] == XYObjetivo [ 1 ] :  # angulo 0 o 180
            if XYPropio [ 0 ] > XYObjetivo [ 0 ] :
                self.Angulo = 180
            else :
                self.Angulo = 0
        else :  # angulo intermedio
            if XYPropio [ 1 ] > XYObjetivo [ 1 ] :
                if XYPropio [ 0 ] < XYObjetivo [ 0 ] :
                    # print("cuadrante 1","arma")
                    self.Angulo = math.degrees ( math.atan ( abs (
                        XYPropio [ 1 ] - XYObjetivo [ 1 ] ) / abs (
                        XYPropio [ 0 ] - XYObjetivo [ 0 ] ) ) )  # +/-
                else :
                    # print("cuadrante 2","arma")
                    self.Angulo = math.degrees ( math.atan ( -abs (
                        XYObjetivo [ 1 ] - XYPropio [ 1 ] ) / abs (
                        XYObjetivo [ 0 ] - XYPropio [ 0 ] ) ) ) + 180
            else :
                if XYPropio [ 0 ] < XYObjetivo [ 0 ] :
                    # print("cuadrante 4","arma")
                    self.Angulo = math.degrees ( math.atan ( -abs (
                        XYObjetivo [ 1 ] - XYPropio [ 1 ] ) / abs (
                        XYObjetivo [ 0 ] - XYPropio [ 0 ] ) ) )
                else :
                    # print("cuadrante 3","arma")
                    self.Angulo = math.degrees ( math.atan ( abs (
                        XYObjetivo [ 1 ] - XYPropio [ 1 ] ) / abs (
                        XYObjetivo [ 0 ] - XYPropio [ 0 ] ) ) ) + 180

    """obtener angulo en grados de la direcion del jugados"""

    def Actualizar ( self , ) :
        if self.Tiempo != self.Constante :
            self.Tiempo = self.Tiempo + 1
        pass

    def Disparar ( self ,
                   XY: list ) :  # self,Posicion cañonX,Posicion cañonY
        # print(self.Angulo)
        # print("X=",XY[0],"Y=",XY[1])
        ListaDisparo = [ ]
        if self.Tiempo == self.Constante :
            self.Tiempo = 0
            ListaDisparo.append (
                DLine ( XY.copy ( ) , self.Angulo , -15 , 0 ,
                        self.Alianza , 9 ) )
            return ListaDisparo
        else :
            return ListaDisparo

    """si el arma esta cargada, dispara"""


"""arma apuntada simple del enemigo, tiene angulos siegos"""





class ArmaAtaqueTriangular :
    # CañonTiangulo=1
    # Constante=None
    # Tiempo=None
    # Angulo=None
    # DesfaseAngulo=None
    def __init__ ( self , constante , alianza , angulo ,
                   desfaseAngulo ) :
        self.Constante = constante
        self.Alianza = alianza
        self.Angulo = angulo
        self.DesfaseAngulo = desfaseAngulo
        self.Tiempo = 0
        self.CañonTriangulo = 1

    def Disparar ( self , xy , vel ) :
        ListaDisparos = [ ]
        if self.CañonTriangulo :
            self.CañonTriangulo = 0
            self.Tiempo = 0
            # print(self.Alianza)
            # print(self.Angulo,self.Angulo-self.DesfaseAngulo,self.Angulo+self.DesfaseAngulo)
            ListaDisparos.append (
                DLine ( xy.copy ( ) , self.Angulo , -15 , 0 ,
                        self.Alianza , 9 ) )
            ListaDisparos.append (
                DLine ( xy.copy ( ) , self.Angulo - self.DesfaseAngulo ,
                        -15 , 0 , self.Alianza , 9 ) )
            ListaDisparos.append (
                DLine ( xy.copy ( ) , self.Angulo + self.DesfaseAngulo ,
                        -15 , 0 , self.Alianza , 9 ) )
            return ListaDisparos
        else :
            return ListaDisparos

    def Actualizar ( self ) :
        # print("tiempo cañon triangulo=",self.Tiempo)
        if self.Tiempo != self.Constante :
            self.Tiempo = self.Tiempo + 1
            pass
            """condador de frames de recarga"""
        else :
            self.CañonTriangulo = 1
            pass


class Anillo :
    Anillo = 1
    Angulo = 360
    XY = None

    def __init__ ( self , constante , aceleracion , alianza ) :
        """
            Attributes:
            
        """
        self.Anillo = 1
        self.Angulo = 360
        self.Tiempo = 0
        self.Constante = constante
        self.Aceleracion = aceleracion
        self.Alianza = alianza

    def Disparar ( self , xy , vel ) :
        aux = [ ]
        if self.Anillo :
            self.Anillo = 0
            self.Tiempo = 0

            con = 0
            while con < self.Angulo :
                if con % 10 == 5 :
                    aux.append ( DLine ( xy.copy ( ) , con , vel , 0 ,
                                         self.Alianza , 0 ) )
                else :
                    aux.append ( DLine ( xy.copy ( ) , con , vel ,
                                         self.Aceleracion ,
                                         self.Alianza , 1 ) )
                con = con + 5
        return aux

    def Actualizar ( self ) :
        # print("tiempo cañon triangulo=",self.Tiempo)
        if self.Tiempo != self.Constante :
            self.Tiempo = self.Tiempo + 1
            pass
            """condador de frames de recarga"""
        else :
            self.Anillo = 1
            pass


class ArmaLaser :
    def __init__ ( self , vidaMaxima , tiempoCambio , alianza ,
                   angulo ) :
        self.VidaMaxima = vidaMaxima
        self.VidaLaser1 = vidaMaxima
        self.VidaLaser2 = vidaMaxima
        self.ConstanteCambio = tiempoCambio
        self.Alianza = alianza
        self.Angulo = angulo
        self.L1 = None
        self.L2 = None
        self.Tiempo = 0
        self.Delay = [ ]
        self.Flag = True
        self.Dañando = False

    def Reset ( self ) :
        self.VidaLaser1 = self.VidaMaxima
        self.VidaLaser2 = self.VidaMaxima
        self.Tiempo = 0
        pass

    def Dañar ( self , daño ) :
        proporcion = (random.randint ( 0 , 101 ) - 1) / 100
        self.VidaLaser1 = self.VidaLaser1 - daño * proporcion
        self.VidaLaser2 = self.VidaLaser2 - daño * (1 - proporcion)
        pass

    def EsFuncionalLaser1 ( self ) :
        return self.VidaLaser1 > 0

    def EsFuncionalLaser2 ( self ) :
        return self.VidaLaser2 > 0

    def GetStatus ( self ) :
        aux = [ ]
        indice = self.VidaLaser1 / self.VidaMaxima
        # print("Indice1:",indice)
        if indice > 0.75 :
            aux.append ( 21 )
        elif indice > 0.5 :
            aux.append ( 22 )
        elif indice > 0.25 :
            aux.append ( 23 )
        else :
            aux.append ( 24 )
        indice = self.VidaLaser2 / self.VidaMaxima
        # print("Indice2:",indice)
        if indice > 0.75 :
            aux.append ( 25 )
        elif indice > 0.5 :
            aux.append ( 26 )
        elif indice > 0.25 :
            aux.append ( 27 )
        else :
            aux.append ( 28 )
        # print(aux)
        return aux

    def EsFuncional ( self ) :
        return self.EsFuncionalLaser1 ( ) or self.EsFuncionalLaser2 ( )

    def Contador ( self ) :
        self.Delay = [ 1 ] * self.ConstanteCambio

    def Actualizar ( self , xy ) :
        print ( "Delay:" , self.Delay )
        if self.Delay :
            self.L1.SetXY ( [ xy [ 0 ] + 14 , xy [ 1 ] + 42 ] )
            self.L2.SetXY ( [ xy [ 0 ] + 50 , xy [ 1 ] + 42 ] )
            if not self.Flag :
                self.Delay.pop ( )
        else :
            self.Dañando = False
            if type ( self.L1 ) != type ( None ) :
                self.L1.SetFin ( True )
                self.L1 = None
            if type ( self.L2 ) != type ( None ) :
                self.L2.SetFin ( True )
                self.L2 = None
            # self.L1=None
            # self.L2=None
        self.Flag = False
        if type ( self.L1 ) != type ( None ) :
            print ( "algo" )
            self.L1.Recalcular ( )
        if type ( self.L2 ) != type ( None ) :
            self.L2.Recalcular ( )
        pass

    def Disparar ( self , xy , angulo , iteracion ) :
        aux = [ ]
        self.Delay.append ( 1 )
        self.Flag = True
        if self.Delay == [ 1 ] * self.ConstanteCambio :
            self.Dañando = True
        if type ( self.L1 ) != type ( None ) or type (
                self.L2 ) != type ( None ) :
            self.L1.SetXY ( [ xy [ 0 ] + 14 , xy [ 1 ] + 42 ] )
            self.L2.SetXY ( [ xy [ 0 ] + 50 , xy [ 1 ] + 42 ] )
        else :
            self.L1 = Laser ( [ xy [ 0 ] + 14 , xy [ 1 ] + 42 ] ,
                              angulo , iteracion , self.Alianza )
            self.L2 = Laser ( [ xy [ 0 ] + 50 , xy [ 1 ] + 42 ] ,
                              angulo , iteracion , self.Alianza )
        aux.append ( self.L1 )
        aux.append ( self.L2 )
        return aux


class ArmaBarrera :
    Droper = 1

    XY = None

    def __init__ ( self , constante , duracion , daño , indice ,
                   alianza ) :
        """
            Attributes:
            
        """
        self.Droper = 1
        self.Tiempo = 0
        self.Constante = constante
        self.Duracion = duracion
        self.Index = indice
        self.Daño = daño
        self.Alianza = alianza

    def Disparar ( self , xy ) :
        aux = [ ]
        if self.Droper :
            self.Droper = 0
            self.Tiempo = 0
            aux.append ( DEstatico ( xy , self.Duracion , self.Alianza ,
                                     daño = self.Daño ,
                                     indice = self.Index ) )

        return aux

    def Actualizar ( self ) :
        # print("tiempo cañon triangulo=",self.Tiempo)
        if self.Tiempo != self.Constante :
            self.Tiempo = self.Tiempo + 1
            pass
            """condador de frames de recarga"""
        else :
            self.Droper = 1
            pass
