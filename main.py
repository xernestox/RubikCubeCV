from detect_colors import detect_colors
from solve_cube import solve_cube
from motor_commands import arduino_commands
from send2arduino import send_commands

colors_array, centers_array = []
 
#detect up

colors_array[0], centers_array[0] = detect_colors()
send_commands()

#detect right

colors_array[1], centers_array[1] = detect_colors()
send_commands()

#detect back

colors_array[2], centers_array[2] = detect_colors()
send_commands()

#detect left

colors_array[3], centers_array[3] = detect_colors()
send_commands()

#detect front

colors_array[4], centers_array[4] = detect_colors()
send_commands()

#detect down

colors_array[5], centers_array[5] = detect_colors()
send_commands()

#solve cube with kociemba algorithm
kociemba_array = solve_cube(colors_array, centers_array)

#transforms kociemba algorithm to arduino commands
arduino_array = arduino_commands(kociemba_array)
print(arduino_array)

#sends the commands to the arduino
send_commands(arduino_array)