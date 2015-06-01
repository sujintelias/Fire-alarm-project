import socket
import serial

def main():
	while True:
	    sms=obj.read(100)
	    if len(sms)>1:
	        sms=sms.split('\n')
	        sms=sms[2]
	        print sms
	        s.sendto(sms,server)

if __name__ == '__main__':
	server=('127.0.0.1',5000)
	obj=serial.Serial('/dev/ttyUSB0',9600,serial.EIGHTBITS,serial.PARITY_NONE,serial.STOPBITS_ONE,1)
	s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	main()            
