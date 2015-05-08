import serial
obj=serial.Serial('COM1',9600,serial.EIGHTBITS,serial.PARITY_NONE,serial.STOPBITS_ONE,1)
cmd='ATEO\r\n'
obj.write(cmd)
reply=obj.read(100)
print reply
cmd='AT\r\n'
obj.write(cmd)
reply=obj.read(100)
print reply

