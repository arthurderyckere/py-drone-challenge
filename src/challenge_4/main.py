from djitellopy import Tello
from pynput import keyboard


tello = Tello()

tello.connect()
tello.takeoff()

def on_press(key):
    try:
        print(key)
        if (key == keyboard.Key.up):
            tello.move_up(20)
        elif (key == keyboard.Key.left):
            tello.move_left(20)
        elif (key == keyboard.Key.right):
            tello.move_right(20)
        elif (key == keyboard.Key.down):
            tello.move_down(20)
        elif (key == keyboard.Key.page_down):
            tello.move_back(20)
        elif (key == keyboard.Key.page_up):
            tello.move_forward(20)
        else : tello.land()
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    if key == keyboard.Key.esc:
        tello.land()
        return False

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()