import socket
s=socket.socket()
host=socket.gethostname()
port=5001
s.bind((host,port))
print "Waiting for client to connect. . ."
s.listen(1)
cl,addr=s.accept()
data='x'
msg='x'
while data!='q':
    msg=raw_input('sujin: ')
    cl.send (msg)
    if msg=='q':
        break
    data=cl.recv(100)
    print 'sarath:'+data
s.close()
