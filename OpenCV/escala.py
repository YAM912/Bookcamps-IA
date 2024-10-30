# Transformacion geometrica
import cv2

# Carga la imagen
image = cv2.imread('C:/Users/marti/Desktop/bootcamp-de-inteligenciaArtificial/OpenCV/imagen.jpg') 

# Define la nueva anchura y altura
new_width, new_height = 400, 300  

# Aplicar la escala a la imagen
scaled = cv2.resize(image, (new_width, new_height)) 

# Mostrar la imagen a escala
cv2.imshow('Escalada', scaled)
cv2.waitKey(0)
cv2.destroyAllWindows()



