"""
Proyecto 2 de Inteligencia Artificial 2.
Enero-Marzo 2017.
Hecho por:
    Ricardo Munch.       Carnet: 11-10684.
    Valentina Hernandez. Carnet: 10-10352.

Este archivo contiene el codigo para generar los resultados del ejercicio 3.
"""
import cv2
import numpy as np

from k_means import k_means


def compress_image(file, k):
    img = cv2.imread(file)
    Z = img.reshape((-1,3))
    Z = np.float32(Z)

    _, labels2, centroids2 = k_means(k, Z)

    centroids2 = np.uint8(centroids2)
    res = [centroids2[l] for l in labels2]
    res2 = np.array(res).reshape((img.shape))

    cv2.imwrite('imagenes/perrito_K{0}.jpg'.format(k), res2)


compress_image('imagenes/perrito.jpg', 2)
compress_image('imagenes/perrito.jpg', 4)
compress_image('imagenes/perrito.jpg', 8)
compress_image('imagenes/perrito.jpg', 16)
compress_image('imagenes/perrito.jpg', 32)
compress_image('imagenes/perrito.jpg', 64)
compress_image('imagenes/perrito.jpg', 128)


# clusters4 = k_means(4, image)
# clusters8 = k_means(8, image)
# clusters16 = k_means(16, image)
# clusters32 = k_means(32, image)
# clusters64 = k_means(64, image)
# clusters128 = k_means(128, image)