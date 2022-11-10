import serial
import time

arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)

def write_read(x):
    arduino.write(x.encode())
    time.sleep(0.05)
    data = arduino.readline()
    return data

commands = list("26426364277426277227727272774372774277226427736427742773772277438888")
print(commands)

for x in commands:
    time.sleep(0.2)
    value = write_read(x)
    print(value)

