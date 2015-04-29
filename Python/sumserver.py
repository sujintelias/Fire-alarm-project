import socket
host='127.0.01'
port=5000
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind((host,port))
print'server started.....'
while True:
    data1,addr=s.recvfrom(1024)
    data1=int(data1)
    print'first no: ',data1
    data2,addr=s.recvfrom(1024)
    data2=int(data2)
    print'second no: ',data2
    data=data1+data2
    data=str(data)
    s.sendto(data,addr)
s.close
