# Transformacion geometrica
import cv2
import numpy as np

# Carga la imagen
image = cv2.imread('C:/Users/marti/Desktop/bootcamp-de-inteligenciaArtificial/OpenCV/imagen.jpg')

# Se Obtinen dimenciones de la imagen
height, width = image.shape [:2]

# Se Calcula el centro de la imagen
center = (width / 2 , height / 2) 

# Se define la matriz de rotacion
angle = 45 
M = cv2.getRotationMatrix2D(center, angle, 1.0)

# Aplicar rotacion a la imagen
rotated = cv2.warpAffine(image, M, (width, height)) 

#Mostrar la imagen rotada
cv2.imshow ('Rotada', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()



