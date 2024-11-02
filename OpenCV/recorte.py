# Transformacion geometrica
import cv2

# Carga la imagen
image = cv2.imread('C:/Users/marti/Desktop/bootcamp-de-inteligenciaArtificial/OpenCV/imagen.jpg') 
image2 = cv2.imread('C:/Users/marti/Desktop/bootcamp-de-inteligenciaArtificial/OpenCV/thundercats.jpg')

# Definir las coordenadas del area de interes (ROI)
x, y, w, h = 50, 50, 150, 100
x2, y2, w2, h2 = 20, 150, 350, 280 

# Recortar la region de interes (ROI)
cropped = image[y:y+h, x:x+w]
cropped2 = image2[y2:y2+h2, x2:x2+w2]  

# Mostrar la imagen recortada
cv2.imshow('Recorte', cropped)
cv2.imshow('Recorte2', cropped2)
cv2.waitKey(0)
cv2.destroyAllWindows()

