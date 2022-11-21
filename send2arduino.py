import serial 
import time

startMarker = 60
endMarker = 62

serPort = 'COM3'
baudRate = 9600
ser = serial.Serial(serPort, baudRate)
print("Serial port " + serPort + " opened  Baudrate " + str(baudRate))

def write_read(x):
    ser.write(x.encode())
    time.sleep(0.05)
    data = ser.readline()
    return data

def waitForArduino():

   # wait until the Arduino sends 'Arduino Ready' - allows time for Arduino reset
   # it also ensures that any bytes left over from a previous message are discarded
   
    global startMarker, endMarker
    
    msg = b''
    while msg.find(b'Arduino is ready') == -1:

      while ser.inWaiting() == 0:
        pass
        
      msg = recvFromArduino()

      print(msg)
      print()

def recvFromArduino():
  global startMarker, endMarker
  
  ck = b''
  x = "z" # any value that is not an end- or startMarker
  byteCount = -1 # to allow for the fact that the last increment will be one too many
  
  # wait for the start character
  while  ord(x) != startMarker: 
    x = ser.read()
  
  # save data until the end marker is found
  while ord(x) != endMarker:
    if ord(x) != startMarker:
      ck = ck + x
      byteCount += 1
    x = ser.read()
  
  return(ck)

def send_commands(arduino_commands):    

  try: 
    ser.open()
    waitForArduino()

    commands = list(arduino_commands)
  
    for x in commands:
        value = write_read(x)
        print(value.decode("utf-8"))

        # ser.close()
  except: 
    commands = list(arduino_commands)
  
    for x in commands:
        value = write_read(x)
        print(value.decode("utf-8"))

  time.sleep(1)
  return("end of arduino commands")