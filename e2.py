from graficas import *
from k_means import k_means
from load_data import *


data = load_data("iris.data")

k = 3
clusters = k_means(k, zip(*data)[0])

for i in range(k):
    print "cluster ", i, ": ", len(clusters[i])

graficar_clusters(clusters, k)
