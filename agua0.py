import pandas as pd
import sklearn.cluster as sk
import numpy
from sklearn.metrics import silhouette_score as shs

def miLectorDeDatos(ruta="../../Data/misdatos.txt"):
    miFormato=["user","n1","op","n2","t"]
    datos=pd.read_csv(ruta,names=miFormato)
    datos=datos.round({"t":1})
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
         return 2
    if (op=="-"):
        return 1
    return 0

def heuristica(datos):
    #datos["dificultad"]=getGrupo(datos.n1)+getGroup(datos.n2)
    i=datos.index
    funcion=pd.Series(index=i,dtype=int)
    tiempo=pd.Series(index=i,dtype=int)
    for index, row in datos.iterrows():
        tiempo[index]=row["t"]*10
        print(index)
        funcion[index]=getGrupo(row["n1"])+getGrupo(row["n2"])+getHardness(row["op"])
    resultado={'heuristica':funcion,'t':tiempo.values.asdtype(int)}
    print (tiempo)
    #miModelo={'opera':datos["op"].values,'heuristica':funcion}
    return resultado

def KMeaning(gatxs):
    for i in range(10):
        nucleos=2+i
        racimo=sk.KMeans(n_clusters=nucleos)
        racimo.fit(gatxs)
        etiquetas=racimo.predict()
        puntos=shs(gatxs,etiquetas)
        print("Si uso "++nucleos++" nucleos obtengo la puntuación de "++puntos)

def main():
    data=miLectorDeDatos()
    data=getSimpleAnaliticOp(data)
    modelo=heuristica(data)
    KMeaning(modelo)
#    data=engorde(data)
#    dataByOp=modeloOp(data)
    #print(modelo)
