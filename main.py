from string import whitespace
import string
from tracemalloc import start
import cv2
import numpy as np

# Clave de colores: 
# blanco-0, azul-1, amarillo-2, 
# naranja-3, rojo-4, verde-5 

#Limites de colores en HSV
color_list = [
    ['red', [160, 160, 70], [180, 250, 250]],
    ['yellow', [20, 40, 70], [40, 250, 250]],
    ['green', [55, 100, 70], [75, 250, 250]],
    ['blue', [100, 50, 70], [130, 250, 250]],
    ['white', [0, 0, 70], [360, 40, 250]],
    ['orange', [10, 100, 20], [20, 250, 250]],
]




#Guarda en variables la imagen original, el color del centro
#y crea un array con los colores de la cara.
img = cv2.imread("./rubik-cube.jpeg", cv2.IMREAD_COLOR)
center = ''
face_colors = []
img_height= img.shape[0]
img_width = img.shape[1]




#Detecta color de las caras y guarda las variables

def detect_color(hsv_image, colors):
    color_found= 'undefined'
    max_count = 0

    for color_name, lower_val, upper_val in colors:
            # threshold the HSV image - any matching color will show up as white
            mask = cv2.inRange(hsv_image, np.array(lower_val), np.array(upper_val))

            # count white pixels on mask
            count = np.sum(mask)
            if count > max_count:
                color_found = color_name
                max_count = count

    return color_found

#parametros iniciales
window_name = 'Image'
start_pointX = 175
start_pointY = 150
end_pointX = 575
end_pointY = 550
color = (255,255,0)
thickness = 2

for square in range(1,10):

    #dibuja rectangulo sobre imagen
    img = cv2.rectangle(img, (start_pointX, start_pointY), (end_pointX, end_pointY), color, thickness)
    box = img[start_pointY:end_pointY, start_pointX:end_pointX]

    # cv2.imshow("image", box)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    #deteccion de color
    hsv = cv2.cvtColor(box, cv2.COLOR_BGR2HSV)
    face_colors.append(detect_color(hsv, color_list))

    #cambio de parametros para siguiente cuadro
    
    if square%3 == 0:
        start_pointY += 400
        end_pointY += 400
        start_pointX = 175
        end_pointX = 575        
    else:
        start_pointX += 400
        end_pointX += 400
    
    #guarda el color del centro de la cara

    if square == 5:
        center = face_colors[square-1]


    
        

#despliega los resultados
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()



print(face_colors)
print(center)