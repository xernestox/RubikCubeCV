from contextlib import nullcontext
from traceback import print_tb
import kociemba


def arduino_commands(kociemba_array):
   input_array = kociemba_array.split()

   # For simulation purposes we assign colors to the faces
   # U = Up = White = W
   # D = Down = Yellow = Y
   # F = Front = Red = R
   # B = Back = Orange = O
   # R = Right = Blue = B
   # L = Left = Green = G

   motor_output = ""
   command_array = []

   #Orders command array per face and direction.

   for i in  range (len(input_array)):

      face= input_array[i][0]
      try: 
         if input_array[i][1] == "'":
               direction = 1
         elif input_array[i][1] == "2":
               direction = 2
      except IndexError:
         direction = 0

      command_array.append([face, direction]) 

   #Permutations for face tracking

   for j in range (len(input_array)):
      for i in range(j, len(input_array)-1):
         match command_array[j][0]:
               case "U":
                  if command_array[i+1][0] == "U":
                     command_array[i+1][0] = "D"
                  elif command_array[i+1][0] == "L":
                     command_array[i+1][0] = "R"
                  elif command_array[i+1][0] == "R":
                     command_array[i+1][0] = "L"            
                  elif command_array[i+1][0] == "D":
                     command_array[i+1][0] = "U"

               case "L":
                  if command_array[i+1][0] == "L":
                     command_array[i+1][0] = "D"
                  elif command_array[i+1][0] == "U":
                     command_array[i+1][0] = "L"
                  elif command_array[i+1][0] == "R":
                     command_array[i+1][0] = "U"            
                  elif command_array[i+1][0] == "D":
                     command_array[i+1][0] = "R"
               
               case "R": 
                  if command_array[i+1][0] == "R":
                     command_array[i+1][0] = "D"
                  elif command_array[i+1][0] == "U":
                     command_array[i+1][0] = "R"
                  elif command_array[i+1][0] == "L":
                     command_array[i+1][0] = "U"            
                  elif command_array[i+1][0] == "D":
                     command_array[i+1][0] = "L"

               case "B": 
                  if command_array[i+1][0] == "B":
                     command_array[i+1][0] = "D"
                  elif command_array[i+1][0] == "U":
                     command_array[i+1][0] = "L"
                  elif command_array[i+1][0] == "L":
                     command_array[i+1][0] = "F"            
                  elif command_array[i+1][0] == "R":
                     command_array[i+1][0] = "B"
                  elif command_array[i+1][0] == "F":
                     command_array[i+1][0] = "U"            
                  elif command_array[i+1][0] == "D":
                     command_array[i+1][0] = "R"

               case "F":
                  if command_array[i+1][0] == "F":
                     command_array[i+1][0] = "D"
                  elif command_array[i+1][0] == "U":
                     command_array[i+1][0] = "R"
                  elif command_array[i+1][0] == "L":
                     command_array[i+1][0] = "F"            
                  elif command_array[i+1][0] == "R":
                     command_array[i+1][0] = "B"
                  elif command_array[i+1][0] == "B":
                     command_array[i+1][0] = "U"            
                  elif command_array[i+1][0] == "D":
                     command_array[i+1][0] = "L"


   arduino_commands = ""

   for x in range(len(command_array)):
      match command_array[x][0]: 
         case "U":
            arduino_commands += "22"
         case "L":
            arduino_commands += "2"
         case "R":
            arduino_commands += "3"
         case "B":
            arduino_commands += "42"
         case "F":
            arduino_commands += "43"
         case "D":
            arduino_commands += ""
         
      match command_array[x][1]: 
         case 0:
            arduino_commands += "7"
         case 1:
            arduino_commands += "6"
         case 2:
            arduino_commands += "77"
         
            
   print(command_array)
   print(arduino_commands)
   return(arduino_commands)
