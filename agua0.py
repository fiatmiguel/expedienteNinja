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
#def KMeaning(datxs):


def main():
    data=miLectorDeDatos()
    data=getSimpleAnaliticOp(data)
#    data=engorde(data)
#    dataByOp=modeloOp(data)
    print(data)
