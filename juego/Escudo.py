"""
    @author: Rodrigo Vargas
    modulo encargado del comportamiento los escudos
"""


class Escudo:
    #recordar siempre declarar self en una funcion de objeto

    """
    Attributes:
        VidaMaxima (int):vida maxima que tiene el escudo
        VidaActual (int):vida actual que tiene el escudo
        EnergiaMaxima (int):EnegiaMaxima que tiene el escudo
        EnergiaAlmacenada (int) :EnergiaAcutal que tiene el escudo
    """

    def __init__ ( self , vidamaxima: int , energiaMaxima: int ,
                   consumoEnergia: int , recargaEnergia: int ,
                   escudoMaximo: int , recargaEscudo: int ) :
        self.VidaMaxima = vidamaxima
        self.VidaActual = vidamaxima
        self.EnergiaMaxima = energiaMaxima
        self.EnergiaAlmacenada = energiaMaxima
        self.ConsumoDeEnergia = consumoEnergia
        self.RecargaDeEnergia = recargaEnergia
        self.EscudoMaximo = escudoMaximo
        self.EscudoActual = escudoMaximo
        self.RecargaDeEscudo = recargaEscudo
    def Reset(self):
        """
        reinicia atributos
        :rtype: None

        """
        self.VidaActual=self.VidaMaxima
        self.EnergiaAlmacenada=self.EnergiaMaxima
        self.EscudoActual=self.EscudoMaximo
        pass
    def GetStatus(self):
        """
        entrega status para dibujar
        :rtype: lista
        """
        aux= [ dict ( Info = "E Escudo:" + str (
            self.EnergiaAlmacenada ) + "/" + str (
            self.EnergiaMaxima ) , X = 32 , Y = 27 ) ]
        self.Recargar()
        if not self.EsFuncional():
            return [2,5,8]
        else:
            #aux=[]
            indices=self.EscudoActual/self.EscudoMaximo
            if indices>0.75:
                aux.append(0)
                aux.append(3)
                aux.append(6)
            else:
                if indices>0.5:
                    aux.append(1)
                    aux.append(3)
                    aux.append(6)
                elif indices>0.25:
                    aux.append(1)
                    aux.append(4)
                    aux.append(6)
                else :#indices<=0:
                    aux.append(1)
                    aux.append(4)
                    aux.append(7)
                #aux.append("Energia:"+str(self.EnergiaAlmacenada)+"/"+str(self.EnergiaMaxima))
            return aux
    def Resistir ( self , dañoRecivido: int ) -> int :
        """
        calcula la absorcion de daño del escudo
        :rtype: int
        """
        if self.EscudoActual > dañoRecivido :
            self.EscudoActual = self.EscudoActual - dañoRecivido
            self.Recargar()
            return 0
        else :
            aux = abs(self.EscudoActual - dañoRecivido)
            self.EscudoActual = 0
            self.Recargar()
            return aux
    def PedirEnergia(self)->int:
        """
        pide energia para recargar el buffer
        :rtype: int
        """
        if not self.EsFuncional():
            return 0
        if self.EnergiaMaxima-self.EnergiaAlmacenada>self.RecargaDeEnergia:
            return self.RecargaDeEnergia
        else:
            return self.EnergiaMaxima-self.EnergiaAlmacenada
    def RecargarEnergia(self,energia:int)->None:
        """
        recargar el buffer de energia del escudo
        :param energia: energia a recargar
        """
        #print("energiaRecargada:",energia)
        #print(self.EnergiaAlmacenada+energia)
        self.EnergiaAlmacenada=self.EnergiaAlmacenada+energia
        pass
    def Dañar(self,daño):
        """
        daña el escudo
        :rtype: None
        """
        self.VidaActual=self.VidaActual-daño
        pass
    def EsFuncional(self):
        """
        indica si el escudo funciona
        :rtype: bool
        """
        return self.VidaActual>0
    def Recargar(self):
        """
        funcion encargada de recargar el escudo
        :rtype: None
        """
        if self.EnergiaAlmacenada>self.ConsumoDeEnergia:
            if (self.EscudoMaximo-self.EscudoActual)/self.RecargaDeEscudo>self.ConsumoDeEnergia:
                self.EscudoActual=self.EscudoActual+self.ConsumoDeEnergia*self.RecargaDeEscudo
                #print("caso1")
                self.EnergiaAlmacenada=self.EnergiaAlmacenada-self.ConsumoDeEnergia
            else :

                self.EnergiaAlmacenada=self.EnergiaAlmacenada-int((self.EscudoMaximo-self.EscudoActual)/self.RecargaDeEscudo)
                #print(int((
                # self.EscudoMaximo-self.EscudoActual)/self.RecargaDeEscudo))
                self.EscudoActual=self.EscudoMaximo

                #print("caso2")
        else :
            if self.EnergiaAlmacenada>(self.EscudoMaximo-self.EscudoActual)/self.RecargaDeEscudo:
                self.EscudoActual=self.EscudoActual+int((self.EscudoMaximo-self.EscudoActual)/self.RecargaDeEscudo)*self.RecargaDeEscudo
                self.EnergiaAlmacenada=self.EnergiaAlmacenada-int((self.EscudoMaximo-self.EscudoActual)/self.RecargaDeEscudo)
                #print("caso3")
            else :
                self.EscudoActual=self.EscudoActual+self.EnergiaAlmacenada*self.RecargaDeEscudo
                self.EnergiaAlmacenada=0
                #print("caso4")
        pass


