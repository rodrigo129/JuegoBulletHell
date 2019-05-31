"""plantilla de objeto python"""
import math
from Disparo import *

class DLine(Disparo):
    X=None
    Y=None
    Amplitud=None
    Index=9
    #amplitud de la ondulacion
    #Z#por implementar
    Omega=None
    #angulo
    Velocidad=-25#añadir al constructor
    #Velocidad
    Color=None
    def __init__(self,x,y,angulo,RGB):#CoordenadaX,CoordenadaY,Angulo,Color
        self.X=x
        self.Y=y
        self.Tiempo=0
        self.Omega=angulo
        self.Color=RGB
        """crear disparo"""
    def GetX(self):
        return self.X
        """obtener x"""
    def GetRGB(self):
        return self.Color
        """obtener RGB"""
    def GetY(self):
        return self.Y
        """obtener y"""
    def GetOmega(self):
        return self.Omega
        """obtener omega"""
    def GetVel(self):
        return self.Velocidad
        """obtener velocidad"""
    def SetX(self,x):
        self.X=x
        pass
        """fijar X"""
    def SetY(self,y):
        self.Y=y
        pass
        """fijar Y"""
    def SetVel(self,vel):
        self.Velocidad=vel
        pass
        """fijar Velociad"""
    def SetOmega(self,angulo):
        self.Omega=angulo
        """fijar Omega"""
    def GetTodo(self):##por mientas
        return (self.X,self.Y,8,8)
        """obtener tupla de coordenadas"""
    def Actualizar(self):
        if self.GetOmega() >= 360:#mas de una rotacion
            self.SetOmega(self.GetOmega()%360)
        
        if self.GetOmega() == 0: ##angulo 0 grados
            self.SetX(self.GetX()-self.GetVel())
            pass
        elif self.GetOmega() < 90: ##angulo menor 90 grados
            self.SetX(int(self.GetX()-self.GetVel()*math.cos(math.radians(self.GetOmega()))))
            self.SetY(int(self.GetY()+self.GetVel()*math.sin(math.radians(self.GetOmega()))))
            pass
        elif self.GetOmega() == 90: ##angulo 90 grados
            self.SetY(self.GetY()+self.GetVel())
            pass
        elif self.GetOmega() < 180: ##angulo menor 90 grados
            self.SetX(int(self.GetX()-self.GetVel()*math.cos(math.radians(self.GetOmega()))))
            self.SetY(int(self.GetY()+self.GetVel()*math.sin(math.radians(self.GetOmega()))))
            pass
        elif self.GetOmega() == 180: ##angulo menor 90 grados
            self.SetX(self.GetX()+self.GetVel())
            pass
        elif self.GetOmega() < 270: ##angulo menor 90 grados
            self.SetX(int(self.GetX()+-self.GetVel()*math.cos(math.radians(self.GetOmega()))))
            self.SetY(int(self.GetY()+self.GetVel()*math.sin(math.radians(self.GetOmega())))) 
            pass
        elif self.GetOmega() == 270: ##angulo menor 90 grados
            self.SetY(self.GetY()-self.GetVel())
            pass
        elif self.GetOmega() < 360: ##angulo menor 90 grados
            self.SetX(int(self.GetX()-self.GetVel()*math.cos(math.radians(self.GetOmega()))))
            self.SetY(int(self.GetY()+self.GetVel()*math.sin(math.radians(self.GetOmega()))))
            pass
