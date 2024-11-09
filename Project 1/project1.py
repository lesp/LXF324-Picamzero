from picamzero import Camera
from time import gmtime, strftime, sleep

cam = Camera()
cam.start_preview()
sleep(2)
cam.take_photo(strftime("%Y-%m-%d %H:%M:%S", gmtime())+".jpg")
cam.stop_preview()