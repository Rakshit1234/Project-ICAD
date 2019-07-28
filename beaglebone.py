import can
import time
import  socket
can.rc['interface'] = 'socketcan_ctypes'

from can.interfaces.interface import Bus
from can import Message
s=socket.socket()
host='192.168.7.1'
port=9999
s.connect((host,post))

def main():
    can_interface='can0'
    bus=Bus(can_interface)
    data_scoket=s.recv(1024)

    print(data_scoket)
    data_can=[0x01]
    if data_scoket[0]=='0':
        data_can=[0x00]
    elif data_scoket[0]=='+':
        data_can=[0x02]

    print(data_can)
    print "send a message..."
    Message.extended_id=False
    Message.is_remote_frame = False
    Message.id_type=0
    Message.is_error_frame=False
    Message.arbitration_id=0x65D
    Message.dlc=1
    Message.data=data_can
    try:
        bus.send(Message);
    except:
        print "Upss something went wrong"

if __name__=="__main__":
    while True:
        main()


