
from detect_colors import detect_colors
from solve_cube import solve_cube
from motor_commands import arduino_commands
from send2arduino import send_commands
import time

colors_array = [None] * 6
centers_array = [None] * 6
colors_array[0], centers_array[0] = detect_colors()
print(colors_array[0], centers_array[0])
 
#detect up
send_commands("1")
time.sleep(4)




# colors_array = ["GGOGGBRBO","WWWYWWYYW","BOOROOROO","YWYYYWYYW","BRGORGBRR","RGGBBRBBG"]
# centers_array = ["G","W","O","Y","R","B"]

# #solve cube with kociemba algorithm
# kociemba_array = solve_cube(colors_array, centers_array)

# #transforms kociemba algorithm to arduino commands
# arduino_array = arduino_commands(kociemba_array)
# print(arduino_array)
