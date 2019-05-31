"""plantilla de objeto python"""
from Armas import ArmaNormal

class Nave:
    x=None#coordenadas
    y=None
    ArmaPrimaria=None
    alto=None
    ancho=None
    alianza="jugador"
    estado=None###añadir estados 
    Modo="Normal"
    #recordar siempre declarar self en una funcion de objeto
    def __init__(self,Alto,Ancho):
        self.x=0
        self.y=0
        self.alto=Alto
        self.ancho=Ancho
        self.ArmaPrimaria=ArmaNormal(2)#intervalo entre disparo
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
    def Actualizar(self):
        self.ArmaPrimaria.Actualizar()
        pass
    """actualizar estado de la Nave"""
