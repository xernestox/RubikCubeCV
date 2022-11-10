import serial
import time

arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)

def send_commands(commands):

    def write_read(x):
        arduino.write(bytes(x, 'utf-8'))
        time.sleep(0.2)
        data = arduino.readline()
        return data


    value = write_read(commands)
    print(value)