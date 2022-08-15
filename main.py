import cv2
import numpy as np

from cv2 import destroyAllWindows

img = cv2.imread("./rubik-cube.jpg", cv2.IMREAD_COLOR)
window_name = 'Image'
start_point = (50,50)
end_point = (90,90)
color = (255,0,0)
thickness = 2

img = cv2.rectangle(img, start_point, end_point, color, thickness)

cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()