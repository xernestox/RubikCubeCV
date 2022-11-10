import kociemba as cube
# http://kociemba.org/cube.htm
# https://pypi.org/project/kociemba/
# https://www.programiz.com/python-programming/online-compiler/?ref=758ecedd

# Definition of a solved cube would be UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB
# For simulation purposes we assign colors to the faces
# U = Up = White = W
# D = Down = Yellow = Y
# F = Front = Red = R
# B = Back = Orange = O
# R = Right = Blue = B
# L = Left = Green = G

# Facelets position:
#              |************|
#              |*U1**U2**U3*|
#              |************|
#              |*U4**U5**U6*|
#              |************|
#              |*U7**U8**U9*|
#              |************|
#  ************|************|************|************
#  *L1**L2**L3*|*F1**F2**F3*|*R1**R2**R3*|*B1**B2**B3*
#  ************|************|************|************
#  *L4**L5**L6*|*F4**F5**F6*|*R4**R5**R6*|*B4**B5**B6*
#  ************|************|************|************
#  *L7**L8**L9*|*F7**F8**F9*|*R7**R8**R9*|*B7**B8**B9*
#  ************|************|************|************
#              |************|
#              |*D1**D2**D3*|
#              |************|
#              |*D4**D5**D6*|
#              |************|
#              |*D7**D8**D9*|
#              |************|

def solve_cube(colors_array, centers_array):

    upF = colors_array[0]
    downF = colors_array[1]
    frontF = colors_array[2]
    backF = colors_array[3]
    rightF = colors_array[4]
    leftF = colors_array[5]

    # upF = "GBRYWWRYY"
    # downF = "RGOYYOOBR"
    # frontF = "YROWRBWRB"
    # backF = "WOWBORYYG"
    # rightF = "BGBRBWWGB"
    # leftF = "OGGWGOYOG" 

    allF = upF + rightF + frontF + downF + leftF + backF

    allF1 = allF.replace(centers_array[0], "U")
    allF2 = allF1.replace(centers_array[1], "R")
    allF3 = allF2.replace(centers_array[2], "B")
    allF4 = allF3.replace(centers_array[3], "L")
    allF5 = allF4.replace(centers_array[4], "F")
    allF6 = allF5.replace(centers_array[5], "D")
 
    # allF1 = allF.replace("W", "U")
    # allF2 = allF1.replace("Y", "D")
    # allF3 = allF2.replace("R", "F")
    # allF4 = allF3.replace("B", "R")
    # allF5 = allF4.replace("O", "B")
    # allF6 = allF5.replace("G", "L")
    
    solution = cube.solve(allF6)

    return(solution)
