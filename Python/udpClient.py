import socket

server = ('127.0.0.1',5000)

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
	data = raw_input("message ->")	
	s.sendto(data,server)
	msg,addr = s.recvfrom(1024) 
	print 'Msg: ' + msg
s.close()

