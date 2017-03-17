"""
Proyecto 2 de Inteligencia Artificial 2.
Enero-Marzo 2017.
Hecho por:
    Ricardo Munch.       Carnet: 11-10684.
    Valentina Hernandez. Carnet: 10-10352.

Este archivo contiene el codigo para generar los resultados del ejercicio 2.
"""

from graficas import *
from k_means import k_means
from load_data import *


data = load_iris("iris.data")
ejemplos = zip(*data)[0]
setosa = [tuple(e) for e in ejemplos[:50]]
versicolor = ejemplos[50:100]
virginica = ejemplos[100:]

ks = [2,3,4,5]
for k in range(2, 6):
    clusters, centroids = k_means(k, ejemplos)
    graficar_clusters_iris(clusters,
                           centroids,
                           "plots/iris_clusters_{0}.png".format(k),
                           False)
graficar_iris("plots/iris_plot.png", False)

c2, _ = k_means(2, ejemplos)
c3, _ = k_means(3, ejemplos)

if len(c2.values()[0]) == 53:
    c = [tuple(x) for x in c2.values()[0]]
else:
    c = [tuple(x) for x in c2.values()[1]]

print "Con k = 2 hubo {0} clasificaciones erroneas (ver grafica).".format(len(set(c) - set(setosa)))

if len(c3.values()[0]) == 50:
    c1, c2 = 1, 2
elif len(c3.values()[1]) == 50:
    c1, c2 = 0, 2
else:
    c1, c2 = 0, 1

print "Con k = 3 hubo {0} clasificaciones erroneas."\
      .format(abs(len(c3.values()[c1])-len(c3.values()[c2])))
