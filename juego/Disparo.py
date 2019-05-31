"""plantilla de objeto python"""


class Disparo:
    #recordar siempre declarar self en una funcion de objeto
    X=None
    Y=None
    Color=None
    Index=0
    #Z=None#aun no implementado
    Vel=-5
    #parametro dueño para comprobar colisiones
    def __init__(self,x,y,RGB):
        self.X=x
        self.Y=y
        #self.Z=z
        self.Color=RGB
    def GetX(self):
        return self.X
        """obtener X"""
    def GetRGB(self):
        return self.Color
        """obtener color formato RGB"""
    def GetY(self):
        return self.Y
        """obtener Y"""
    def SetX(self,x):
        self.X=x
        pass
        """fijar X"""
    def SetY(self,y):
        self.Y=y
        pass
        """fijar Y"""
    def GetVel(self):
        return self.Vel
        """fijar obtener velocidad"""
    def GetTodo(self):##por mientas
        return (self.X,self.Y,10,5)
        """obtener tupla de coordenadas"""
    def Actualizar(self):
        self.SetY(self.GetY()+self.GetVel())
        pass
        """actualizar datos"""
    def GetIndex(self):
        return self.Index
