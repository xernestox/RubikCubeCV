from contextlib import nullcontext
from traceback import print_tb
import kociemba


kociemba_array = "B U' B R2 F2 L' F' R2 B' L' B U D' F2 U R2 F2 R2 U' F2 D2"
input_array = kociemba_array.split()
face_order = ["U", "D", "F", "B", "R", "L"]

# For simulation purposes we assign colors to the faces
# U = Up = White = W
# D = Down = Yellow = Y
# F = Front = Red = R
# B = Back = Orange = O
# R = Right = Blue = B
# L = Left = Green = G

motor_output = ""
command_array = []

for i in  range (len(input_array)):

    face= input_array[i][0]
    try: 
        if input_array[i][1] == "'":
            direction = -90
        elif input_array[i][1] == "2":
            direction = 180
    except IndexError:
        direction = 90

    command_array.append([face, direction]) 

    

print(command_array)
