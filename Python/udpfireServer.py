import socket
import serial
import time
host=''
port=5000
obj=serial.Serial('/dev/ttyS0',9600,serial.EIGHTBITS,serial.PARITY_NONE,serial.STOPBITS_ONE,1) 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print"server stared"
s.bind((host,port))
while(1):
        #data,addr=s.recvfrom(1024)
        obj.write('f')
        #print"Sending to serial->"+str(data)
        print"Sending to serial->"+str('f')
        while True:
                reply=obj.read(100)
                if len(reply)>0:
                        print"Replay from Serial:"+str(reply)
                        break
        time.sleep(1)