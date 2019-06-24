"""
    @author: Rodrigo Vargas
    modulo encargado del comportamiento la energia
"""


class Nucleo :
    # recordar siempre declarar self en una funcion de objeto
    def __init__ ( self , energiaMaxima , vidaMaxima ) :
        self.VidaMaxima = vidaMaxima
        self.VidaActual = vidaMaxima
        self.EnergiaMaxima = energiaMaxima
        self.EnergiaActual = energiaMaxima

    def Reset ( self ) :
        self.VidaActual = self.VidaMaxima
        self.EnergiaActual = self.EnergiaMaxima

    def GetStatus ( self ) :
        indice = self.VidaActual / self.VidaMaxima
        self.Cargar ( 1 )
        aux = [ dict ( Info = "Vida:" + str (
            round ( self.VidaActual ) ) + "/" + str (
            self.VidaMaxima ) , X = 32 , Y = 25 ) , dict (
            Info = "Energia:" + str ( self.EnergiaActual ) + "/" + str (
                self.EnergiaMaxima ) , X = 32 , Y = 24 ) ]
        if indice > 0.75 :
            aux.append ( 9 )
        elif indice > 0.5 :
            aux.append ( 10 )
        elif indice > 0.25 :
            aux.append ( 11 )
        else :
            aux.append ( 12 )
        # aux.append("Energia:"+str(self.EnergiaActual)+"/"+str(self.EnergiaMaxima))
        return aux

    def Dañar ( self , daño ) :
        self.VidaActual = self.VidaActual - daño
        pass

    def Tiene ( self , energia ) :
        return self.EnergiaActual > energia

    def EsFuncional ( self ) :
        return self.VidaActual > 0

    def Pedir ( self , peticion ) :
        #print ( "peticion:" , peticion )
        if peticion > self.EnergiaActual :
            aux = self.EnergiaActual
            self.EnergiaActual = 0
            return aux
        else :
            self.EnergiaActual = self.EnergiaActual - peticion
            return peticion

    def Cargar ( self , carga ) :
        if self.EnergiaActual + carga > self.EnergiaMaxima :
            self.EnergiaActual = self.EnergiaMaxima
        else :
            self.EnergiaActual = self.EnergiaActual + carga
        pass
