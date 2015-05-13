import socket
import serial
server=('127.0.0.1',5000)
obj=serial.Serial('COM1',9600,serial.EIGHTBITS,serial.PARITY_NONE,serial.STOPBITS_ONE,1)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sms=obj.read(100)
while(sms!=0):
    if len(sms)>1:
        sms=sms.split('\n')
        sms=sms[2]
        print sms
        #s.sendto(sms,server)
'''msg=raw_input("->") 
while(msg!=0):
    s.sendto(msg,server)
    if msg=='q':
        s.close()
        break
    else:
        msg=raw_input("->") '''   
