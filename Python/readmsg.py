import socket
import serial
from threading import Thread
server=('127.0.0.1',5000)
obj=serial.Serial('COM1',9600,serial.EIGHTBITS,serial.PARITY_NONE,serial.STOPBITS_ONE,1)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
class sms(Thread):
    def run(self):
        while True:
            sms=obj.read(100)
            if len(sms)>1:
                sms=sms.split('\n')
                sms=sms[2]
                print sms
            else:
                print 'no sms'

class msg(Thread):
    def run(self):
        msg=raw_input("->") 
        while True :
            s.sendto(msg,server)
            if msg=='q':
                s.close()
                break
            else:
                msg=raw_input("->")
  
t1Obj = sms()
t2Obj = msg()

t1Obj.start()
t2Obj.start()
