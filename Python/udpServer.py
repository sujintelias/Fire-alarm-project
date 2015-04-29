import socket

 	
host = '127.0.0.1'
port = 5000

s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))

print "Server Started"


while True:

	data,addr = s.recvfrom(1024)
	data = data.upper()
	s.sendto(data,addr)		
	#print "message from:" + str(addr)
	print "Date: " + data
		
	

