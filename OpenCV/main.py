# Ejemplo basico para cargar una imagen y mostrar una imagen utilizando OpenCV

import cv2

# Cargar una imagen desde el archivo
image = cv2.imread('C:/Users/marti/Desktop/bootcamp-de-inteligenciaArtificial/OpenCV/imagen.jpg')
#image = cv2.imread('imagen.jpg')

# Mostrar la imagen en una ventana
cv2.imshow ('Imagen', image)

# Esperar a que el usuario presione una tecla para cerrar la ventana
cv2.waitKey(0)

# Cerrar todas las ventanas abiertas
cv2.destroyAllWindows()
