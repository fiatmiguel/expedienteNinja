import pandas as pd
import sklearn.cluster as sk
import numpy
from sklearn.metrics import silhouette_score as shs
from sklearn.metrics.cluster import calinski_harabaz_score as chs


def padre(ruta="../../Data/opData.csv"):
    miFormato=["user","n1","op","n2","t"]
    datos=pd.read_csv(ruta,header=1,names=miFormato)
    datos=datos.round({"t":4})
    return datos

def poda(data):
    cuentaCompleja="/"
    miSample=data.query('op!="/"')
    return miSample

def getGroup(num):
    if num<11:
        return 1
    if num%10==0:
        return 2
    return 3

def getHardness(op):
    if (op=="*"):
         return 3
    if (op=="-"):
        return 2
    return 1

def heuristica(datos):
    i=datos.index
    funcion=pd.Series(index=i,dtype=int)
    tiempo=pd.Series(index=i,dtype=int)
    for index, row in datos.iterrows():
        tiempo[index]=row["t"]*10000
        funcion[index]=getGroup(row["n1"])*getGroup(row["n2"])*getHardness(row["op"])
    res={'heuristica':funcion,'tiempo':tiempo.values.astype(int)}
    resultado=pd.DataFrame(data=res)
    return resultado

def significante(gatxs,titulosNoviliarios):
    for i in range(10):
        nucleos=2+i
        for novillos,militares in titulosNoviliarios,profesores:
            print (nucleos)
            racimo=novillos(n_clusters=nucleos)
            etiquetas=racimo.fit_predict(gatxs)
            puntos=militares(gatxs,etiquetas)
            print("Si uso "+str(novillos)+" con "+str(nucleos)+" nucleos obtengo la puntuación de "+str(puntos))

data=padre()
data=poda(data)
modelo=heuristica(data)
titulos={sk.AgglomerativeClustering,sk.KMeans}
profesores={shs,chs}
realidad={'novillos':titulos,'militares':profesores}
significante(modelo,realidad)
