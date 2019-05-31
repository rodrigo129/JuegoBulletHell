"""plantilla de objeto python"""
import math
from Disparo import *
class Dsin(Disparo):
    X=None
    Y=None
    XR=None
    Index=1
    Amplitud=None
    #amplitud de la ondulacion
    #Xreal
    YR=None
    #Yreal
    #Z#por implementar
    Omega=2*math.pi
    #angulo
    Velocidad=-5#añadir al constructor
    #Velocidad
    Color=None
    Tiempo=None
    #"tiempo"
    def __init__(self,x,y,amp,RGB):#añadir angulo Omega
        self.X=x
        self.Y=y
        self.XR=x
        self.YR=y
        self.Tiempo=0
        self.Amplitud=amp
        self.Color=RGB
        """crear disparo"""
    def GetRGB(self):
        return self.Color
        """obtener color formato RGB"""
    def GetX(self):
        return self.X
        """obtener X"""
    def GetXR(self):
        return self.XR
        """obtener el x real"""
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
    def PasoTiempo(self):
        self.Tiempo=self.Tiempo+1
        pass
        """pasa el tiempo"""
    def GetTiempo(self):
        return self.Tiempo
        """retorna el tiempo"""
    def GetVel(self):
        return self.Vel
        """fijar obtener velocidad"""
    def GetOmega(self):
        return self.Omega
    def GetTodo(self):##por mientas
        return (self.X,self.Y,10,5)
        """obtener tupla de coordenadas"""
    def GetAmplitud(self):
        return self.Amplitud
        """obtener amplitud"""
    def Actualizar(self):
        self.SetY(self.GetY()+self.GetVel())###adaptar
        self.SetX(self.GetXR()+int(self.GetAmplitud()*math.sin((self.GetOmega()*self.GetTiempo())/90)))
        self.PasoTiempo()
        pass
        """actualizar datos"""
