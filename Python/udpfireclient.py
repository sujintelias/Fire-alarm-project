import socket
import serial
server=('127.0.0.1',5000)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
def cmnd(cmd):
    cmd=(cmd+'/r/n')
    return cmd
    obj.write(cmd)
msg=raw_input("->")
while(1):
    s.sendto(msg,server)
    if msg=='q':
        s.close()
        break
    else:
        msg=raw_input("->")
    
