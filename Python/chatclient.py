import socket
s=socket.socket()
host='192.168.1.16'
port=5001
s.connect((host,port))
msg='x'
data=0
while msg!='q' :
    data=s.recv(100)
    if data=='q':
        break
    print 'sujin: '+data
    msg=raw_input('sarath: ')
    s.send (msg)
s.close()
