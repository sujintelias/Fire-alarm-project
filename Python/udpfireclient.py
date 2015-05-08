import socket
import serial
server=('127.0.0.1',5000)
obj=serial.Serial('COM1',9600,serial.EIGHTBITS,serial.PARITY_NONE,serial.STOPBITS_ONE,1)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
def cmnd(cmd):
    cmd=(cmd+'\r\n')
    obj.write(cmd)
    reply=obj.read(100)
    print reply
cmnd('AT')
cmnd('ATEO')
cmnd('AT+CMGF=1')
cmnd('AT+CNMI=1,2,0,0,0,')
'''msg=raw_input("->") 
while(1):
    s.sendto(msg,server)
    if msg=='q':
        s.close()
        break
    else:
        msg=raw_input("->")'''
    
