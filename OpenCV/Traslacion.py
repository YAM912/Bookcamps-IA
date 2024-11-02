# Transformacion geometrica
import cv2
import numpy as np

# Carga la imagen
image = cv2.imread('C:/Users/marti/Desktop/bootcamp-de-inteligenciaArtificial/OpenCV/imagen.jpg')
image2 = cv2.imread('C:/Users/marti/Desktop/bootcamp-de-inteligenciaArtificial/OpenCV/thundercats.jpg') 

# Se define la matriz de rotacion
tx, ty = 100, 50
M = np.float32([[1, 0, tx],[0, 1, ty]])

# Aplicar la traslacion de la imagen
translated = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
translated2 = cv2.warpAffine(image2, M, (image2.shape[1], image2.shape[0]))

# Mostrar la imagen rasladada
cv2.imshow('traslacion', translated)
cv2.imshow('traslacion2', translated2)
cv2.waitKey(0)
cv2.destroyAllWindows()


