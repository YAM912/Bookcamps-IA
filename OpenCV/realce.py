# Transformacion geometrica
import cv2
import numpy as np

# Carga la imagen
image = cv2.imread('C:/Users/marti/Desktop/bootcamp-de-inteligenciaArtificial/OpenCV/imagen.jpg') 

# Definir el kernel para el filtro de afilado (Realce)
kernel = np.array([[-1, -1, -1],
                   [-1, 9, -1],
                   [-1, -1, -1]])

# Aplicar el filtro de afilado (Realce) para realzar los detalles
sharpened = cv2.filter2D(image, -1, kernel)  

# Mostrar la imagen realzada
cv2.imshow('Realce', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()

