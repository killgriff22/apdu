import serial
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
ser = serial.Serial("COM3",9600)
byte = ser.read()
dumpfile = open("dump.txt","w")
try:
    while byte:
        dumpfile.write(byte.decode())
        print(byte.decode(),end="")
        #prepare the next frame
        byte = ser.read()
except KeyboardInterrupt:
    ser.close()
    dumpfile.close()
    exit()
