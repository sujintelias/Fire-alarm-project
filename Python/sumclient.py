import socket
server=('127.0.0.1',5000)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    print'enter first no: '
    num1=raw_input('first no: ')
    s.sendto(num1,server)
    print'enter second no: '
    num2=raw_input('second no: ')
    s.sendto(num2,server)
    res,addr=s.recvfrom(1024)
    res=int(res)
    print'sum: ' ,res
s.close()
