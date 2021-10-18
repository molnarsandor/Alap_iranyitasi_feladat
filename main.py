import time

from djitellopy import Tello


tello = Tello()
tello.connect()

tello.takeoff()
time.sleep(3)
tello.rotate_clockwise(90)
time.sleep(3)
tello.move_forward(50)
time.sleep(3)
tello.land()
