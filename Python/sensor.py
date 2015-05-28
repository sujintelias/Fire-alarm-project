import socket
import serial
server=('192.168.1.16',5000)
obj=serial.Serial('COM13',9600,serial.EIGHTBITS,serial.PARITY_NONE,serial.STOPBITS_ONE,1)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    sen=obj.read(100)
    print sen
    s.sendto(sen,server)
