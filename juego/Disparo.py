"""
    @author: Rodrigo Vargas
    modulo encargado del comportamiento de los disparos estandar
"""


class Disparo :
    """
        modulo encargado del comportamiento de los disparos estandar
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
        Alianza(str):bando al que pertenece
    """
    # recordar siempre declarar self en una funcion de objeto
    XY: list = None
    #Color = None
    Index: int = 0
    # Z=None#aun no implementado
    Velocidad: int = -5
    Aceleracion: float = 0
    VelocidadFinal: int = 0
    # parametro dueño para comprobar colisiones
    Daño: int = 300  # añadir a constructores
    Tipo: str = "Estatico"
    Continuo: bool = False
    Fin: bool = False

    def __init__ ( self , xy: list , velocidad: int ,
                   velocidadFinal: int ,
                   aceleracion: float , alianza: str ) :
        """
        Args:
            xy: lista coordenadas (x,y)
            velocidad: velocididad de movimiento
            aceleracion: aceleracion por ciclo de velocidad
            velocidadFinal: velocidad final de movimiento
            alianza: bando al que pertenece
            :rtype: cls
            :type alianza: str
            :type aceleracion: float
            :type velocidadFinal: int
            :type xy: list
            :type velocidad: int
        """

        # self.Daño=10
        self.XY = xy
        self.Velocidad = velocidad
        self.Aceleracion = aceleracion
        self.VelocidadFinal = velocidadFinal
        # self.Z=z
        self.Alianza = alianza

    def EsContinuo ( self )  -> bool:
        """
        indica si un disparo puede generar nuevas intancias de disparo
        :rtype: bool
        """
        aux = self.Continuo
        self.Continuo = False
        return aux

    def GetAlianza ( self ) -> str :
        """
        indica a que bando pertence la entidad
        :rtype: str
        """
        return self.Alianza

    def GetX ( self ) -> int :
        """
        Returns:
            valor numerico de XY[0]
            :rtype: int
        """
        return self.XY [ 0 ]
        """obtener X"""

    def GetY ( self ) -> int :
        """
        Returns:
            valor numerico de XY[0]
            :rtype: int
        """
        return self.XY [ 1 ]
        """obtener Y"""

    def SetX ( self , x: int ) -> None :
        """
        Args:
            x: nueva valor XY[0]
        Returns:
            fija un nuevo XY[0]
             no retorna nada
            :rtype: None
        """
        self.XY [ 0 ] = x
        pass
        """fijar X"""

    def SetY ( self , y: int ) -> None :
        """
        Args:
            y: nueva valor XY[1]
        Returns:
            fija un nuevo XY[1]
             no retorna nada
            :rtype: None
        """
        self.XY [ 1 ] = y
        pass
        """fijar Y"""

    def GetTipo ( self )  -> str:
        """
        Returns:
            indica si el sprite del disparo puede tener rotaciones
            :rtype: str
        """
        return self.Tipo

    def GetDaño ( self )  -> int:
        """
        Returns:
            entre la cantidad de daño del disparo
            :rtype: int
        """
        return self.Daño

    def GetVel ( self ) -> int :
        """
        Returns:
            valor numerico de la velocidad
            :rtype: int
        """
        return self.Velocidad
        """fijar obtener velocidad"""

    def EsFin ( self )  -> bool:
        """
        Returns:
            indica si un disparo tiene que ser eliminado
            :rtype: bool
        """
        return self.Fin

    def GetTodo ( self ) -> tuple :
        """
        Returns:

            :rtype: tuple
            :return: retorna coordenadas para localizar el sprite
        """
        return (self.XY [ 0 ] , self.XY [ 1 ] )
        """
        Returns:
            retorna coordenadas para localizar el sprite
        """
        """obtener tupla de coordenadas"""

    def Actualizar ( self ) -> None :
        """
        Returns:
            la funcion esta encargada de calcular las fisicas del
            disparo
            :rtype: None
        """
        self.SetY ( self.GetY ( ) - self.GetVel ( ) )
        pass
        """actualizar datos"""

    def GetIndex ( self ) -> int :
        """
        Returns:
            indice del sprite asignado
            :rtype: int
        """
        return self.Index

    def GetXY ( self ) -> list :
        """

        :rtype: list
        :return: entrega las coordenas en formato de lista
        """
        return self.XY

    def Accelerar ( self )  -> None:
        """
        funcion encargada de calcular las fisicas correspondientes a
        acceleraciones y desaceleraciones
        :rtype: None
        """
        if self.Aceleracion == 0 :
            pass
        elif self.Aceleracion < 0 :
            if self.Velocidad + self.Aceleracion > self.VelocidadFinal :
                self.Velocidad = self.Velocidad + self.Aceleracion
            else :
                self.Velocidad = self.VelocidadFinal
        elif self.Aceleracion > 0 :
            if self.Velocidad + self.Aceleracion < self.VelocidadFinal :
                self.Velocidad = self.Velocidad + self.Aceleracion
            else :
                self.Velocidad = self.VelocidadFinal
        pass
