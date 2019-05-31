"""plantilla de objeto python"""
from Armas import ArmaEstandarApuntada
from Armas import ArmaEstandarSniper
class Enemigo:
    x=None#coordenadas
    y=None
    ArmaPrimaria=None
    alto=None
    ancho=None
    alianza="Enemigo"
    estado=None###añadir estados 
    Modo="Normal"
    #recordar siempre declarar self en una funcion de objeto
    def __init__(self,Alto,Ancho):
        self.x=500##añadir al constructor
        self.y=500
        self.alto=Alto
        self.ancho=Ancho
        self.ArmaPrimaria=ArmaEstandarApuntada(60)#intervalo entre disparo
    def GetX(self):
        return self.x
        """obtener x"""
    def CambiarModo(self):#añadir restriciones
        if self.Modo == "Normal":
            self.Modo="Sobrecarga"
            pass
        else:
            self.Modo="Normal"
            pass
    def GetCentro(self):
        return (self.x+32,self.y+37)
        """punto de apuntado para los enemigos"""
    def GetY(self):
        return self.y
        """obtener y"""
    def SetX(self,X):
        self.x=X
        pass
        """set x"""
    def SetY(self,Y):
        self.y=Y
        pass
        """set y"""
    def GetPosicion(self):
        return (self.x,self.y)
        """obtener posicion"""
    def GetTamaño(self):
        return (self.ancho,self.alto)
        """obtener tamaño"""
    def SetPosicion(self,X,Y):
        self.x=X
        self.y=Y
        pass
        """mover posicion"""
    def SetTamaño(self,Alto,Ancho):
        self.alto=Alto
        self.ancho=Ancho
        pass
        """fijar tamaño"""
    def GetTodo(self):
        return (self.x,self.y,self.ancho,self.alto)
        """obtener tupla coordenadas y tamaño"""
    #def DisparoPrimario(self):##?no en uso?
        #return self.ArmaPrimaria.Disparar(self.Modo,self.GetY()+13,self.GetX()+20,23)
    """disparar ametralladora"""
    def Actualizar(self,objetivo):
        self.ArmaPrimaria.Apuntar(self.GetPosicion(),objetivo)
        self.ArmaPrimaria.Actualizar()
        return self.ArmaPrimaria.Disparar(self.x,self.y)
    """actualizar estado de la Nave"""
"""enemigo estandar""" 
class EnemigoSniper:
    x=None#coordenadas
    y=None
    ArmaPrimaria=None
    alto=None
    ancho=None
    alianza="Enemigo"
    estado=None###añadir estados 
    Modo="Normal"
    #recordar siempre declarar self en una funcion de objeto
    def __init__(self,Alto,Ancho):
        self.x=500
        self.y=500
        self.alto=Alto
        self.ancho=Ancho
        self.ArmaPrimaria=ArmaEstandarSniper(5)#intervalo entre disparo
    def GetX(self):
        return self.x
        """obtener x"""
    def CambiarModo(self):#añadir restriciones
        if self.Modo == "Normal":
            self.Modo="Sobrecarga"
            pass
        else:
            self.Modo="Normal"
            pass
    def GetCentro(self):
        return (self.x+32,self.y+37)
        """punto de apuntado para los enemigos"""
    def GetY(self):
        return self.y
        """obtener y"""
    def SetX(self,X):
        self.x=X
        pass
        """set x"""
    def SetY(self,Y):
        self.y=Y
        pass
        """set y"""
    def GetPosicion(self):
        return (self.x,self.y)
        """obtener posicion"""
    def GetTamaño(self):
        return (self.ancho,self.alto)
        """obtener tamaño"""
    def SetPosicion(self,X,Y):
        self.x=X
        self.y=Y
        pass
        """mover posicion"""
    def SetTamaño(self,Alto,Ancho):
        self.alto=Alto
        self.ancho=Ancho
        pass
        """fijar tamaño"""
    def GetTodo(self):
        return (self.x,self.y,self.ancho,self.alto)
        """obtener tupla coordenadas y tamaño"""
    def DisparoPrimario(self):
        return self.ArmaPrimaria.Disparar(self.Modo,self.GetY()+13,self.GetX()+20,23)
    """disparar ametralladora"""
    def Actualizar(self,objetivo):
        self.ArmaPrimaria.Apuntar(self.GetPosicion(),objetivo)
        self.ArmaPrimaria.Actualizar()
        return self.ArmaPrimaria.Disparar(self.x,self.y)
    """actualizar estado de la Nave"""
