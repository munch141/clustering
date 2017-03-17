"""
Proyecto 2 de Inteligencia Artificial 2.
Enero-Marzo 2017.
Hecho por:
    Ricardo Munch.       Carnet: 11-10684.
    Valentina Hernandez. Carnet: 10-10352.

Este archivo contiene funciones para cargar los datos de los ejercicios.
"""

import numpy as np

SETOSA = 0
VERSICOLOR = 1
VIRGINICA = 2

def load_iris(filename):
    x = []
    y = []
    with open(filename) as fp:
        for line in fp:
            s = line.split(",")
            rasgos = np.array(map(float, s[:-1])).reshape(1, 4)[0]
            x.append(rasgos)

            if s[-1] == "Iris-setosa\n":
                y.append(SETOSA)
            elif s[-1] == "Iris-versicolor\n":
                y.append(VERSICOLOR)
            elif s[-1] == "Iris-virginica\n":
                y.append(VIRGINICA)

    return zip(x, y)
