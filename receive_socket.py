import socket
import os
import subprocess
import can
can.rc['interface'] = 'socketcan_ctypes'

from threading import Thread,Lock
from time import sleep

from can.interfaces.interface import Bus
from can import Message

def can_send():
    print ("Send a message...") 
    while(1):
        print ("ID : 0x11")
        Can(0x11)
        sleep(1)
        print ("ID : 0x22")
        Can(0x22)
        sleep(1)

def Can(id):
   can_interface = 'can0'
   bus = Bus(can_interface)
   
   Message.extended_id = False
   Message.is_remote_frame = False
   Message.id_type = 1
   Message.is_error_frame = False
   if id==0x22:
        Message.arbitration_id=id
        Message.dlc=3
        Message.data=[0x22]
   if id==0x11:
        Message.arbitration_id=id
        Message.dlc=3
        Message.data=[0x11]
   try:
        bus.send(Message);
        print ("Data=",Message.data)
        print ("ID=",id)
   except:
        print ("Oops!!! Something went wrong!")
def main():
   data=0
   while(1):
        s = socket.socket()
host = '192.168.7.1'
port = 9999

s.connect((host, port))

while True:
    data = s.recv(1024)
    if data == 'quit':
        s.close()
     if data == '123':
        
    print(data[:].decode("utf-8"))
        can_interface = 'can0'
        bus = Bus(can_interface)

        #print "Send a message...a heart beat"
        Message.extended_id = False
        Message.is_remote_frame = False
        Message.id_type = 1
        Message.is_error_frame = False
        Message.arbitration_id = 0x33
        Message.dlc = 1

        data=data+1
        Message.data = [data]
        try:
            bus.send(Message);
            print (Message.data)
        except:
            print ("Ups something went wrong!")
        sleep(0.1)


if __name__=="__main__":
    main()
