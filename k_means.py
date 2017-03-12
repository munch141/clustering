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
    centroids = [np.random.randn(dim) for _ in range(k)]
    old_centroids = []
    clusters = {}
    while not converged(centroids, old_centroids):
        old_centroids = centroids
        clusters = get_clusters(xs, centroids)
        centroids = []
        for i in range(k):
            # si hay algun cluster vacio no tiene sentido calcular la
            # media, entonces le asignamos un nuevo centroide aleatorio
            if not clusters[i]:
                centroids.append(np.random.randn(dim))
            else:
                centroids.append(np.mean(clusters[i], axis=0))
    return clusters


