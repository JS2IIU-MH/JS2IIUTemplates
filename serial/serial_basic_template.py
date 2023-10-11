'''
pyserial example
    $ pip install pyserial

    see reference
    [Welcome to pySerials documentation — pySerial 3.4 documentation]
    (https://pyserial.readthedocs.io/en/latest/)
'''

import serial

ser = serial.Serial(port='COM12',
                    baudrate=115200,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    timeout=None)

ser.write(b'Hello')
line = ser.readline()
print(line)
ser.close()
