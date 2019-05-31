"""plantilla de objeto python"""
from Disparo import *
from DisparoLinia import *
from DisparoLinia2 import *
"""arma principal del jugados"""
class ArmaNormal:#apuntado manual
    #Modo="Normal"
    Cañon1=1
    Cañon2=0
    Constante=5 #tiempo entre disparo
    Tiempo=0
    fase=1
    def __init__(self,constante):
        self.Constante=constante
        
    def Disparar(self,Modo,YRelativo,XRelativo,XDesfase):
        ListaDisparos=[]
        if  Modo =="Sobrecarga":
            if  self.Tiempo ==  self.Constante:
                self.Tiempo=0
                ListaDisparos.append(Disparo(XRelativo,YRelativo,(255,17,20)))
                ListaDisparos.append(Disparo(XRelativo+XDesfase,YRelativo,(255,17,20)))
                return ListaDisparos
                """disparar Ambos Cañones"""
            else :
                return ListaDisparos
                """armas en Recarga"""
        elif Modo =="Normal":
            if  self.fase==1 and  self.Cañon1==1:
                self.fase=0
                self.Cañon1=0
                #Cañon2=1
                self.Tiempo=0
                ListaDisparos.append(Disparo(XRelativo,YRelativo,(255,17,20)))
                return ListaDisparos
                """DispararCañon1"""
            elif  self.fase==0 and  self.Cañon2==1:
                self.fase=1
                self.Cañon2=0
                self.Tiempo=0
                ListaDisparos.append(Disparo(XRelativo+XDesfase,YRelativo,(255,17,20)))
                return ListaDisparos
                """DispararCañon2"""
            else:
                return ListaDisparos
                """armas en Recarga"""
            
    def Actualizar(self):
        if  self.Tiempo !=  self.Constante:
            self.Tiempo= self.Tiempo+1
            pass
            """condador de frames de recarga"""
        elif  self.Tiempo== self.Constante and  self.fase==1:
            self.Cañon1=1
            pass
            """Cañon1 Recargado"""
        elif  self.Tiempo== self.Constante and  self.fase==0:
            self.Cañon2=1
            pass
            """Cañon2 Recargado"""
            """arma primaria jugador"""
            
"""arma apuntada simple del enemigo, tiene angulos siegos"""
class ArmaEstandarApuntada:#apuntado simple
    Cañon1=1
    Constante=6000
    Tiempo=0
    fase=1
    Angulo=0
    def __init__(self,constante):
        self.Constante=constante
    def Apuntar(self,XYPropio,XYObjetivo):
        
        print (XYPropio,XYObjetivo)
        if XYPropio[0]==XYObjetivo[0]:#angulo 90 o 270
            if XYPropio[1]>XYObjetivo[1]:
                self.Angulo=90
            else:
                self.Angulo=270
        elif XYPropio[1]==XYObjetivo[1]:#angulo 0 o 180
            if XYPropio[0]>XYObjetivo[0]:
                self.Angulo=180
            else:
                self.Angulo=0
        else:                           #angulo intermedio
            if XYPropio[1]>XYObjetivo[1]:
                if XYPropio[0]<XYObjetivo[0]:
                    print("cuadrante 1","arma")
                    self.Angulo=math.degrees(math.atan(abs(XYPropio[1]-XYObjetivo[1])/abs(XYPropio[0]-XYObjetivo[0])))#+/-
                else:
                    print("cuadrante 2","arma")
                    self.Angulo=math.degrees(math.atan(-abs(XYObjetivo[1]-XYPropio[1])/abs(XYObjetivo[0]-XYPropio[0])))+180
            else:
                if XYPropio[0]<XYObjetivo[0]:
                    print("cuadrante 4","arma")
                    self.Angulo=math.degrees(math.atan(-abs(XYObjetivo[1]-XYPropio[1])/abs(XYObjetivo[0]-XYPropio[0])))
                else:
                    print("cuadrante 3","arma")
                    self.Angulo=math.degrees(math.atan(abs(XYObjetivo[1]-XYPropio[1])/abs(XYObjetivo[0]-XYPropio[0])))+180
    """obtener angulo en grados de la direcion del jugados"""
    def Actualizar(self,):
        if self.Tiempo != self.Constante:
            self.Tiempo=self.Tiempo+1
        pass
    def Disparar(self,X,Y):#self,Posicion cañonX,Posicion cañonY
        print(self.Angulo)
        print("X=",X,"Y=",Y)
        ListaDisparo=[]
        if self.Tiempo == self.Constante:
            self.Tiempo=0
            ListaDisparo.append(DLine(X,Y,self.Angulo,(255,17,20)))
            return ListaDisparo
        else:
            return ListaDisparo
    """si el arma esta cargada, dispara"""
   
"""arma apuntada simple del enemigo, tiene angulos siegos"""        
class ArmaEstandarSniper:#apuntado reactivo
    Cañon1=1
    Constante=60
    Tiempo=0
    fase=1
    Angulo=0
    XYO=[]#lista de objetivo calculado
    def __init__(self,constante):
        self.Constante=constante
    def Apuntar(self,XYPropio,XYObjetivo):
        print (XYPropio,XYObjetivo)#remover
        if XYPropio[0]==XYObjetivo[0]:#angulo 90 o 270
            if XYPropio[1]>XYObjetivo[1]:
                self.Angulo=90
            else:
                self.Angulo=270
        elif XYPropio[1]==XYObjetivo[1]:#angulo 0 o 180
            if XYPropio[0]>XYObjetivo[0]:
                self.Angulo=180
            else:
                self.Angulo=0
        else:                           #angulo intermedio
            if XYPropio[1]>XYObjetivo[1]:
                if XYPropio[0]<XYObjetivo[0]:
                    print("cuadrante 1","arma apuntado")
                    self.Angulo=math.degrees(math.atan(-(XYPropio[1]-XYObjetivo[1])/(XYPropio[0]-XYObjetivo[0])))#+/-
                else:
                    print("cuadrante 2","arma apuntado")
                    self.Angulo=math.degrees(math.atan(-(XYPropio[1]-XYObjetivo[1])/(XYPropio[0]-XYObjetivo[0])))+180
            else:
                if XYPropio[0]<XYObjetivo[0]:
                    print("cuadrante 4","arma apuntado")
                    self.Angulo=math.degrees(math.atan((XYPropio[1]-XYObjetivo[1])/(XYPropio[0]-XYObjetivo[0])))+180
                else:
                    print("cuadrante 3","arma apuntado")
                    self.Omega=abs(math.degrees(math.atan(-(XYPropio[1]-XYObjetivo[1])/(XYPropio[0]-XYObjetivo[0])))+360)
        
        
        
        
        if self.Angulo >= 360:#correcion de angulo
            self.Angulo=(self.Angulo%360)
        
        
        
        
        if self.Angulo <90 or self.Angulo>270:
            self.XYO=[-1000000000,
            round(-1000000000*((XYObjetivo[1]-XYPropio[1])/(XYObjetivo[0]-XYPropio[0]))+XYObjetivo[1]*((XYObjetivo[1]-XYPropio[1])/(XYObjetivo[0]-XYPropio[0]))+XYObjetivo[1])]
        elif self.Angulo >90 or self.Angulo<270:
            self.XYO=[-1000000000,
            round(-1000000000*((XYObjetivo[1]-XYPropio[1])/(XYObjetivo[0]-XYPropio[0]))+XYObjetivo[1]*((XYObjetivo[1]-XYPropio[1])/(XYObjetivo[0]-XYPropio[0]))+XYObjetivo[1])]
        elif self.Angulo ==90:
            self.XYO=[XYPropio[0],-1000000000]
        elif self.Angulo ==270:
            self.XYO=[XYPropio[0],1000000000]
        pass
            
            
            
            
    """obtener angulo en grados de la direcion del jugados y un objetivo en la pendiente del jugador"""
    def Actualizar(self,):
        if self.Tiempo != self.Constante:
            self.Tiempo=self.Tiempo+1
        pass
    def Disparar(self,X,Y):#self,Posicion cañonX,Posicion cañonY
        XYA=[X,Y]
        print(self.Angulo)
        ListaDisparo=[]
        if self.Tiempo == self.Constante:
            self.Tiempo=0
            print(self.Angulo,"arma,disparo")
            ListaDisparo.append(DLine2(XYA,self.XYO,10,(255,17,20)))
            return ListaDisparo
        else:
            return ListaDisparo
    """si el arma esta cargada, dispara"""
        
