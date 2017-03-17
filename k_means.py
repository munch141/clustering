"""
Proyecto 2 de Inteligencia Artificial 2.
Enero-Marzo 2017.
Hecho por:
    Ricardo Munch.       Carnet: 11-10684.
    Valentina Hernandez. Carnet: 10-10352.

Este archivo contiene la implementacion de k-means.
"""

import numpy as np

def distance(x, centroid):
    return np.linalg.norm(x-centroid)

def min_dist(x, centroids):
    return np.argmin([distance(x, centroid) for centroid in centroids])

def get_clusters(xs, centroids):
    clusters = {}
    for i in range(len(centroids)):
        clusters[i] = []
    for x in xs:
        clusters[min_dist(x, centroids)].append(x)
    return clusters

def converged(cs, old_cs):
    return set([tuple(a) for a in cs]) == set([tuple(a) for a in old_cs])

def k_means(k, xs):
    dim = len(xs[0])
    # elegimos puntos aleatorios en los datos como centroides iniciales
    centroids = [xs[i] for i in
                 np.random.choice(range(len(xs)), k, replace=False)]
    old_centroids = []
    clusters = {}
    while not converged(centroids, old_centroids):
        old_centroids = centroids
        clusters = get_clusters(xs, centroids)
        centroids = []
        for i in range(k):
            centroids.append(np.mean(clusters[i], axis=0))
    return (clusters, centroids)
