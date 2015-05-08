import serial
obj=serial.Serial('COM1',9600,serial.EIGHTBITS,serial.PARITY_NONE,serial.STOPBITS_ONE,1)
cmd='AT+CMGF=1/r/n'
obj.write(cmd)
cmd='ATEO/r/t'
obj.write(cmd)
cmd='AT+CNMI=1,2,0,0,0,/r/n'
obj.write(cmd)
reply=obj.read(100)
print reply
