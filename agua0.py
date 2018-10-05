import pandas as pd
import sklearn as sk

def miLectorDeDatos(ruta="../../Data/opData.csv"):
    miFormato=["user","n1","op","n2","t"]
    datos=pd.read_csv(ruta,header=1,names=miFormato)
    datos=datos.round({"t":2})
    return datos

def modeloOp(datos):
    sum=data.loc[datos["op"]=="+"]
    sub=data.loc[datos["op"]=="-"]
    mul=data.loc[datos["op"]=="*"]
    div=data.loc[datos["op"]=="/"]
    return [sum,sub,mul,div]

def engorde(datos):
    datos["min"]=datos["t"].map(lambda x:(x-1.50))
    datos["max"]=datos["t"].map(lambda x:(x+1.50))
    return datos

def getSimpleAnaliticOp(data):
    cuentaCompleja="/"
    miSample=data.query('op!="/"')
    return miSample

#def timeStudy(data):
def getGrupo(numero):
    if numero<11:
        return 0
    if numero%10==0:
        return 1
    return 2

def getHardness(op):
    if (op=="*"):
         return 4
    if (op=="-"):
        return 1
    return 0

def heuristica(datos):
    #datos["dificultad"]=getGrupo(datos.n1)+getGroup(datos.n2)
    i=datos.index
    funcion=pd.Series(index=i)
    for index, row in datos.iterrows():
        funcion[index]=int(getGrupo(row["n1"])+getGrupo(row["n2"])+getHardness(row["op"]))
    miModelo={'opera':datos["op"].values,'heuristica':funcion}
    return miModelo

#def KMeaning(gatxs):


def main():
    data=miLectorDeDatos()
    data=getSimpleAnaliticOp(data)
    modelo=heuristica(data)
#    data=engorde(data)
#    dataByOp=modeloOp(data)
    print(data)
