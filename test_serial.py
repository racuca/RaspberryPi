# racuca@gmail.com
# Raspberry Pi CM4 Nano Serial Test Sample
# send 10 packets like [test0], [test1], [test2], ...
# Receive and print packet data
# pip install pyserial


import threading
import time

import serial

port = '/dev/ttyS0'
baud = 115200  # serial speed
alive = True
strencoding = None
strcmd = None

ser = serial.Serial(
   port = port,
   baudrate = baud,
   bytesize = serial.EIGHTBITS,
   parity = serial.PARITY_NONE,
   stopbits = serial.STOPBITS_ONE,
   timeout = 3
)

# Thread
def readthread(ser):
    line = ''

    print('readthread init\n')

    while alive:
        try:
            for c in ser.read():
                line += (chr(c))
                if line.startswith('['): 
                    if line.endswith(']'):
                        print('receive data=' + line)
                        if line == '[end]':
                            print('end command\n')
                        # line reset
                        line = ''
                        #ser.write('ok'.encode())
                else:
                    line = ''
        except Exception as e:
            print('read exception')

    print('thread exit')

    ser.close()


def main():
    global alive
    global strcmd
    global strencoding

    # Thread
    thread = threading.Thread(target=readthread, args=(ser,))
    thread.daemon = True
    thread.start()

    #         start  packet length   command    variable data   checksum end
    #strcmd = [0x11,     0x09,         0x01,        0x35,           sum      0xFF]
    
    
    for count in range(0, 10):
        strcmd = '[test' + str(count) + ']'
        print('send data=' + strcmd)
        strencoding = strcmd.encode()
        ser.write(strencoding)
        time.sleep(0.5)

    print('main exit')
    alive = False


main()
