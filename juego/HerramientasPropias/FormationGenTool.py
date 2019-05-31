import json
F=open("Path","r")
Fo=open("Formation","w")
TiempoInicial=int(input("ingrese el tiempo en el que inicia la formacio, en cuadros, 60 cuadros=1seg\n"))
OffsetTime=int(input("ingrese intervalo Cuadros entre enemigo en formacion,considerado 60=1 seg\n"))
Tamaño=int(input("ingrese el tamaño de la formacion\n"))
Modo=input("ingrese el modo de la formacion\n")

DiccionarioOriginal=json.loads(F.read())[0]
NuevoDiccionario={}
ListaKeysOriginales=list(DiccionarioOriginal.keys())
ListaKeysTiempoInicial=[]
ListaAux=[]
Contador=0
NuevoKeyAnterior=0
TiempoAnterior=0
for key in ListaKeysOriginales:
    if Contador==0:
        TiempoAnterior=int(key)
        NuevoDiccionario[0]=DiccionarioOriginal.get(str(key))
        Contador=1
    if Contador==1:
        NuevoDiccionario[NuevoKeyAnterior+int(key)-TiempoAnterior]=DiccionarioOriginal.get(str(key))
        NuevoKeyAnterior=NuevoKeyAnterior+int(key)-TiempoAnterior
        TiempoAnterior=int(key)
NuevoDiccionario[NuevoKeyAnterior+1]=[3000,3000]#enviar enemigo al "sumidero"
DiccionarioAux={}
DiccionarioAux["Path"]=NuevoDiccionario
DiccionarioAux["CantidadEnimigos"]=Tamaño
DiccionarioAux["Modo"]=Modo
DiccionarioAux["Offset"]=OffsetTime
Fo.write(json.dumps(DiccionarioAux,indent=4))

    
