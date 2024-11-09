from picamzero import Camera
from gpiozero import MotionSensor
from time import gmtime, strftime, sleep

pir = MotionSensor(17)
cam = Camera()

def timelapse():
    print("Sensor triggered")
    filename = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    cam.start_preview()
    cam.capture_sequence(filename=filename+".jpg", num_images=10, interval=1, make_video=True)

while True:
    print("Waiting for sensor to be triggered")
    pir.when_motion = timelapse
    sleep(1)

