"""
Proyecto 2 de Inteligencia Artificial 2.
Enero-Marzo 2017.
Hecho por:
    Ricardo Munch.       Carnet: 11-10684.
    Valentina Hernandez. Carnet: 10-10352.

Este archivo contiene algunas funciones para graficar los resultados.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from load_data import *


def graficar_iris(file, show):
    data = load_iris("iris.data")
    setosa = [x for (x, y) in data if y == SETOSA]
    versicolor = [x for (x, y) in data if y == VERSICOLOR]
    virginica = [x for (x, y) in data if y == VIRGINICA]

    points = [[] for _ in range(6)]
    points[0].append([(x, y) for (x, y, _, _) in setosa])
    points[0].append([(x, y) for (x, y, _, _) in versicolor])
    points[0].append([(x, y) for (x, y, _, _) in virginica])

    points[1].append([(x, y) for (x, _, y, _) in setosa])
    points[1].append([(x, y) for (x, _, y, _) in versicolor])
    points[1].append([(x, y) for (x, _, y, _) in virginica])

    points[2].append([(x, y) for (x, _, _, y) in setosa])
    points[2].append([(x, y) for (x, _, _, y) in versicolor])
    points[2].append([(x, y) for (x, _, _, y) in virginica])

    points[3].append([(x, y) for (_, x, y, _) in setosa])
    points[3].append([(x, y) for (_, x, y, _) in versicolor])
    points[3].append([(x, y) for (_, x, y, _) in virginica])

    points[4].append([(x, y) for (_, x, _, y) in setosa])
    points[4].append([(x, y) for (_, x, _, y) in versicolor])
    points[4].append([(x, y) for (_, x, _, y) in virginica])

    points[5].append([(x, y) for (_, _, x, y) in setosa])
    points[5].append([(x, y) for (_, _, x, y) in versicolor])
    points[5].append([(x, y) for (_, _, x, y) in virginica])

    titles = [
        "Sepal Length vs Sepal Width",
        "Sepal Length vs Petal Length",
        "Sepal Length vs Petal Width",
        "Sepal Width vs Petal Length",
        "Sepal Width vs Petal Width",
        "Petal Length vs Petal Width"
    ]

    labels = [
        ("Sepal Length", "Sepal Width"),
        ("Sepal Length", "Petal Length"),
        ("Sepal Length", "Petal Width"),
        ("Sepal Width", "Petal Length"),
        ("Sepal Width", "Petal Width"),
        ("Petal Length", "Petal Width")
    ]

    colors = ['#3b79c8', '#eb872e', '#85d831']
    patches = [
        mpatches.Patch(color='#3b79c8', label='Setosa'),
        mpatches.Patch(color='#eb872e', label='Versicolor'),
        mpatches.Patch(color='#85d831', label='Virginica')
    ]

    f, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, sharex='col', sharey='row')
    axs = [ax1, ax2, ax3, ax4, ax5, ax6]
    for ax, ps, title, label in zip(axs, points, titles, labels):
        lines = []
        for p, color in zip(ps, colors):
            x, y = zip(*p)
            lines.append(ax.plot(x, y, 'o', c=color, markersize=2)[0])
            ax.set_xlabel(label[0])
            ax.set_ylabel(label[1])
    f.suptitle("Iris Data Set", fontsize = 14, color = '0.5')
    plt.figlegend(lines, ["Setosa", "Versicolor", "Virginica"], loc='upper right')
    if show:
        plt.show()
    plt.savefig(file)


def graficar_clusters_iris(cs, centroids, file, show):
    clusters = [[] for _ in range(6)]
    for c in cs.values():
        clusters[0].append([(x, y) for (x, y, _, _) in c])
        clusters[1].append([(x, y) for (x, _, y, _) in c])
        clusters[2].append([(x, y) for (x, _, _, y) in c])
        clusters[3].append([(x, y) for (_, x, y, _) in c])
        clusters[4].append([(x, y) for (_, x, _, y) in c])
        clusters[5].append([(x, y) for (_, _, x, y) in c])

    titles = [
        "Sepal Length vs Sepal Width",
        "Sepal Length vs Petal Length",
        "Sepal Length vs Petal Width",
        "Sepal Width vs Petal Length",
        "Sepal Width vs Petal Width",
        "Petal Length vs Petal Width"
    ]

    labels = [
        ("Sepal Length", "Sepal Width"),
        ("Sepal Length", "Petal Length"),
        ("Sepal Length", "Petal Width"),
        ("Sepal Width", "Petal Length"),
        ("Sepal Width", "Petal Width"),
        ("Petal Length", "Petal Width")
    ]

    f, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, sharex='col', sharey='row')
    axs = [ax1, ax2, ax3, ax4, ax5, ax6]
    for ax, cluster, title, label in zip(axs, clusters, titles, labels):
        for c in cluster:
            x, y = zip(*c)
            ax.scatter(x, y, s=2)
            ax.set_xlabel(label[0])
            ax.set_ylabel(label[1])
    f.suptitle("{0} clusters".format(len(cs)),
                 fontsize = 14,
                 color = '0.5')
    plt.savefig(file)
    if show:
        plt.show()
