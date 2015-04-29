import socket
host='127.0.0.1'
port=5000

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind ((host,port))
print "server started"
data=0
msg=0
while data!='q':
	data,addr=s.recvfrom(1024)
	print 'client: '+data
	msg=raw_input("server: ")
	s.sendto (msg,addr)
	if msg=='q':
		break
	
s.close()
