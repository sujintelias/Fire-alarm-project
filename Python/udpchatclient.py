import socket
server=('127.0.0.1',5000)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
data=0
msg=0
while data!='q':	
	
	msg=raw_input('client: ')
	if msg=='q':
		break
	s.sendto(msg,server)
	data,addr=s.recvfrom(1024)
	print 'server: '+data
s.close()
