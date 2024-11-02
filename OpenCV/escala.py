# Transformacion geometrica
import cv2

# Carga la imagen
image = cv2.imread('C:/Users/marti/Desktop/bootcamp-de-inteligenciaArtificial/OpenCV/imagen.jpg')
image2 = cv2.imread('C:/Users/marti/Desktop/bootcamp-de-inteligenciaArtificial/OpenCV/thundercats.jpg') 

# Define la nueva anchura y altura
new_width, new_height = 400, 300  

# Aplicar la escala a la imagen
scaled = cv2.resize(image, (new_width, new_height))
scaled2 = cv2.resize(image2, (new_width, new_height))

# Mostrar la imagen a escala
cv2.imshow('Escalada', scaled)
cv2.imshow('Escalada2', scaled2)
cv2.waitKey(0)
cv2.destroyAllWindows()



