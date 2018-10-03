import pandas as pd
import sklearn as sk

def miLectorDeDatos(ruta="../Data/opData.csv"):
    miFormato=["user","n1","op","n2","t"]
    datos=pd.read_csv(ruta,index_col=False,names=miFormato)
    return datos

def modeloOp(data):
    sum=data.loc[data["op"]=="+"]
    sub=data.loc[data["op"]=="-"]
    mul=data.loc[data["op"]=="*"]
    div=data.loc[data["op"]=="/"]
    return [sum,sub,mul,div]
"""
def engorde(datos):
    data["animales"]=data.map

def timeStudy(data):
"""

def main():
    data=miLectorDeDatos()

    dataByOp=modeloOp(data)
    print(data["op"])
