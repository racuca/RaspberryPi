import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
"""
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.output(5, GPIO.HIGH)
time.sleep(1)
GPIO.output(5, GPIO.LOW)
time.sleep(1)
GPIO.output(6, GPIO.HIGH)
time.sleep(1)
GPIO.output(6, GPIO.LOW)
time.sleep(1)
GPIO.output((5,6), GPIO.HIGH)
time.sleep(1)
GPIO.output((5,6), GPIO.LOW)

"""
GPIO.setup(4, GPIO.IN)
print(GPIO.input(4))

# add rising edge detection on a channel
GPIO.add_event_detect(4, GPIO.BOTH)

event = 1
buttoneventcount = 4
while event:    
    time.sleep(1)
    print('wait 1 sec')
    if GPIO.event_detected(4):
        if GPIO.input(4) == 0:
            print('Button pressed')
        elif GPIO.input(4) == 1:
            print('Button released')
        
        buttoneventcount -= 1
        
    if buttoneventcount == 0:
        break
    
GPIO.cleanup()


