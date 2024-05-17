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
    
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        print(line)

