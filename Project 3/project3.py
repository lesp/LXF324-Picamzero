from picamzero import Camera

cam = Camera()
cam.start_preview()
cam.capture_sequence(filename="sequence.jpg", num_images=10, interval=1, make_video=True)
cam.stop_preview()