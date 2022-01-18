import serial
import time
import threading

running_listening_thread = False

def listening_thread(ser):
    global running_listening_thread
    print("start reader")
    while (running_listening_thread):
        if (ser.inWaiting() > 0):
            out = ser.read()
            print(out)

com = input("Enter COM: ")
baudrate = input("Enter baudrate: ")
timeout = input("Enter timeout: ")
ser = serial.Serial(com, int(baudrate), timeout=int(timeout))
temp = input("Do you want to start port listening? [Y/N]")
if (temp == "Y" or temp == "y" or temp == "Yes" or temp == "YES" or temp == "yes"):
    running_listening_thrad = True
    th = threading.Thread(target=listening_thread, args=(ser,))
    th.start()
time.sleep(1)
print("start writer")
while(1):
    temp = input()
    if temp == "-1":
        break;
    try:
        if int(temp) < 0:
            print("Number too small")
        elif int(temp) > 255:
            print("Number too big")
    except:
        break;
    ser.write(bytes([int(temp)]))
running_listening_thrad = False
time.sleep(1)
print("Program finished")
