# Transformacion geometrica
import cv2

# Carga la imagen
image = cv2.imread('C:/Users/marti/Desktop/bootcamp-de-inteligenciaArtificial/OpenCV/imagen.jpg')

#Aplicar el operador Sobel para detectar bordes
sobelx = cv2.Sobel(image, cv2.CV_64F, 1,  0, ksize=5)
sobely = cv2.Sobel(image, cv2.CV_64F, 0,  1, ksize=5)

# Combinar las respuestas en magnitud
edges = cv2.magnitude(sobelx, sobely)

# Normalizar los valores para mostrar la imagen correctamente
edges = cv2.normalize(edges, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# Mostrar la imagen con bordes detectados
cv2.imshow('Detección de Bordes', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()


