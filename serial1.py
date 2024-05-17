import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.reset_input_buffer()

def maskOn():
    ser.write(b"on\n")
    line = ser.readline().decode('utf-8').rstrip()
    print(line)


def maskOff():
    ser.write(b"off\n")
    line = ser.readline().decode('utf-8').rstrip()
    print(line)

def mask():
    while True:
        ser.write(b"on\n")
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        time.sleep(1)
        ser.write(b"off\n")
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        time.sleep(1)