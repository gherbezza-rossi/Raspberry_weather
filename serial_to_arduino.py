import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.reset_input_buffer()


def light_regulation(value):
    if value > 5000:
        mes = "BLINDS: ON\n"
        ser.write(mes.encode())
    if value < 300:
        mes = "BLINDS: OFF\n"
        ser.write(mes.encode())

    line = ser.readline().decode('utf-8').rstrip()
    print(line)


def soil1_regulation(value):
    if value < 0.2:
        mes = "SOIL1:ON\n"
        ser.write(mes.encode())
    line = ser.readline().decode('utf-8').rstrip()
    print(line)


def soil2_regulation(value):
    if value < 0.2:
        mes = "SOIL2:ON\n"
        ser.write(mes.encode())
    line = ser.readline().decode('utf-8').rstrip()
    print(line)


def windows_regulation(value):
    if value > 40:
        mes = "WINDOW:OFF\n"
        ser.write(mes.encode())
    if value < 30:
        mes = "WINDOW:ON\n"
        ser.write(mes.encode())
    line = ser.readline().decode('utf-8').rstrip()
    print(line)





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