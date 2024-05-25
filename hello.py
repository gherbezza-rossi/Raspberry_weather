import serial 
import time

arduinoSerialData = serial.Serial('/dev/ttyACM0',9600)

def maskON():
    print("mask ONNNNN")
    arduinoSerialData.write(1)

def maskOFF():
    arduinoSerialData.write(0)


while True:
    arduinoSerialData.write(0)
    
    if arduinoSerialData.in_waiting > 0:
        line = arduinoSerialData.readline().decode('utf-8').rstrip()
        print(line)

