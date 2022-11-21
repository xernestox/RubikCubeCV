from string import whitespace
from tracemalloc import start
import cv2
import numpy as np

def detect_colors():
    # Clave de colores: 
    # U = Up = White = W
    # D = Down = Yellow = Y
    # F = Front = Red = R
    # B = Back = Orange = O
    # R = Right = Blue = B
    # L = Left = Green = G

    #Limites de colores en HSV
    color_list = [
        ['R', [150, 140, 70], [180, 255, 255]],
        ['R', [0, 40, 70], [9, 255, 250]],
        ['Y', [17, 0, 0], [50, 255, 255]],
        ['G', [55, 100, 70], [75, 250, 255]],
        ['B', [100, 50, 70], [150, 250, 255]],
        ['W', [0, 0, 70], [360, 40, 255]],
        ['O', [9, 40, 70], [17, 255, 255]],
    ]

    #Captura la imagen de la camara web
    def webcam_capture():
        webcam = cv2.VideoCapture(0)
        s, frame = webcam.read()
        img_filename = "./face-img.jpeg"

        if s:
            cv2.imwrite(filename= img_filename, img=frame)

        del(webcam)
        return img_filename

    #Guarda en variables la imagen original, el color del centro
    #y crea un array con los colores de la cara.
    img_filename = webcam_capture()
    img = cv2.imread(img_filename, cv2.IMREAD_COLOR)
    # cv2.imshow("image", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    center = ''
    face_colors = ""
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
    gap = 30
    start_pointX = 130 + gap
    end_pointX = 270 - gap
    square_width = end_pointX - start_pointX
     

    start_pointY = 40 + gap
    end_pointY = start_pointY + square_width 

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
        face_colors += detect_color(hsv, color_list)

        #cambio de parametros para siguiente cuadro
        
        if square%3 == 0:
            start_pointY += square_width + 2*gap
            end_pointY += square_width + 2*gap
            start_pointX = 130 + gap
            end_pointX = 270 - gap
        else:
            start_pointX += square_width + 2*gap
            end_pointX += square_width + 2*gap
        
        #guarda el color del centro de la cara

        if square == 5:
            center = face_colors[square-1]


    #despliega los resultados
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return(face_colors, center)
