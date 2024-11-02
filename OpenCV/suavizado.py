# Transformacion geometrica
import cv2

# Carga la imagen
image = cv2.imread('C:/Users/marti/Desktop/bootcamp-de-inteligenciaArtificial/OpenCV/imagen.jpg')
image2 = cv2.imread('C:/Users/marti/Desktop/bootcamp-de-inteligenciaArtificial/OpenCV/thundercats.jpg')

# Aplicar el filtro Gaussiano para suavizar la imagen
smoothed = cv2.GaussianBlur(image, (5, 5), 0)
smoothed2 = cv2.GaussianBlur(image2, (5, 5), 0) 

# Mostrar la imagen recortada
cv2.imshow('Suavizado', smoothed)
cv2.imshow('Suavizado2', smoothed2)
cv2.waitKey(0)
cv2.destroyAllWindows()

