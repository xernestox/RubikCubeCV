import serial
import time

arduino = serial.Serial(port='COM3', baudrate=19200, timeout= 1.0)

def write_read(x):
    arduino.write(x.encode())
    # time.sleep(0.05)
    data = arduino.readline()
    return data

commands = list("11111111111111111111")

for x in commands:
    value = write_read(x)
    print(value)

