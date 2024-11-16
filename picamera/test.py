# pi camera


import picamera
from time import sleep

#create object for PiCamera class
camera = picamera.PiCamera()
print(camera.revision)
    
    
#set resolution
camera.resolution = (320, 240)
camera.brightness = 60
camera.start_preview()
#add text on image
#camera.annotate_text = 'Hi Pi User'
sleep(5)
#store image
camera.capture('image1.jpeg')
camera.stop_preview()