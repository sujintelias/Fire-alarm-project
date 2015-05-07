import socket
import serial
host=''
port=5000
obj=serial.Serial('COM1',9600,serial.EIGHTBITS,serial.PARITY_NONE,serial.STOPBITS_ONE,1) 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print"server stared"
s.bind((host,port))
while(1):
        data,addr=s.recvfrom(1024)
        if data=='q':
                obj.write(data)
                reply=obj.read(100)
                print"Replay from Serial:"+str(reply)
                s.close()
                break
        else:
                print"sending to serial->"+str(data)
                obj.write(data)
                reply=obj.read(100)
                print"Replay from Serial:"+str(reply)
