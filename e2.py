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

ks = [2,3,4,5]
for k in range(2, 6):
    clusters, centroids = k_means(k, zip(*data)[0])
    graficar_clusters_iris(clusters,
                           centroids,
                           "plots/iris_clusters_{0}.png".format(k),
                           False)
graficar_iris("plots/iris_plot.png", False)
