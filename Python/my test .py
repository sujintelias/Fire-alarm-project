import serial
obj=serial.Serial('COM1',9600,serial.EIGHTBITS,serial.PARITY_NONE,serial.STOPBITS_ONE,1)
def cmnd(cmd):
    cmd=(cmd+'\r\n')
    return cmd
obj.write(cmnd('AT'))
reply=obj.read(100)
print reply

