"""
Proyecto 2 de Inteligencia Artificial 2.
Enero-Marzo 2017.
Hecho por:
    Ricardo Munch.       Carnet: 11-10684.
    Valentina Hernandez. Carnet: 10-10352.

Este archivo contiene algunas funciones para graficar los resultados.
"""

import matplotlib.pyplot as plt


def graficar_clusters_iris(cs, centroids):
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
    plt.show()
