# Pico Micropython Serial Example

from machine import UART, Pin
import time

workflag = True

uart0 = UART(0, 115200, bits=8, parity=None, stop=1)

#txData = b'[Hello World]'
#uart0.write(txData)
time.sleep(0.5)

while workflag:
    time.sleep(0.1)    
    if uart0.any() == 0:
        #print("no data")
        continue
    else:
        rxData = bytes()
        while uart0.any() > 0:
            rxData += uart0.read(1)    
        # data parsing and processing
        print(rxData)
        if rxData == b'[end]':
            workflag = False




