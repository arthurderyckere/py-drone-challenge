from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()

tello.move_left(35)
tello.move_right(35)
tello.rotate_counter_clockwise(360)


tello.land()