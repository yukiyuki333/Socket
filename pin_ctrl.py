import RPi.GPIO as GPIO
import socket
import sys
import threading
def create_thread(target):
    thread=threading.Thread(target=target)
    thread.daemon=True
    thread.start()
PORT=30000
FORMAT="utf-8"
SERVER="192.168.100.173"
ADDR=(SERVER,PORT)
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(ADDR)
buffer=[]
def rec_msg():
     if len(buffer)!=0:
         c.send(buffer[0].encode(FORMAT))
         del buffer[0]
        
GPIO.setmode(GPIO.BOARD)
left_led=29
right_led=31
left_in=33
right_in=35
GPIO.setup(left_led,GPIO.OUT)
GPIO.setup(right_led,GPIO.OUT)
GPIO.setup(left_in,GPIO.IN)
GPIO.setup(right_in,GPIO.IN)
connmsg="connected"
c.send(connmsg.encode(FORMAT))
print("connected")
while(True):
    val=GPIO.input(left_in)
    msgtoserver=""
    if(val==GPIO.LOW):
        GPIO.output(left_led,True)
        msgtoserver="Left"
    else:
        GPIO.output(left_led,False)
    val=GPIO.input(right_in)
    if(val==GPIO.LOW):
        GPIO.output(right_led,True)
        msgtoserver="Right"
    else:
        GPIO.output(right_led,False)
    if msgtoserver!="":
        buffer.append(msgtoserver)
    create_thread(rec_msg)
    if msgtoserver=="quit":
        break





