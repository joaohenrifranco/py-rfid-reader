import serial
from pynput.keyboard import Key, Controller

keyboard = Controller()

ser = serial.Serial('/dev/ttyACM0', 9600)

print(ser.name)         # check which port was really used

while (True):
    line = ser.readline().decode('UTF-8')

    for char in line:
        keyboard.press(char)
        
ser.close()