from cv2 import solve
from detect_colors import detect_colors
from solve_cube import solve_cube
from motor_commands import arduino_commands

# face_colors, center = detect_colors()
# print(face_colors, center)

kociemba_array = solve_cube()
arduino_array = arduino_commands(kociemba_array)

print(arduino_array)