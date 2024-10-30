# Transformacion geometrica
import cv2

# Carga la imagen
image = cv2.imread('C:/Users/marti/Desktop/bootcamp-de-inteligenciaArtificial/OpenCV/imagen.jpg') 

# Definir las coordenadas del area de interes (ROI)
x, y, w, h = 50, 50, 150, 100  

# Recortar la region de interes (ROI)
cropped = image[y:y+h, x:x+w]  

# Mostrar la imagen recortada
cv2.imshow('Recorte', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()

