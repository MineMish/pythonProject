import keyboard
import mouse
import time

def change():
    global work
    work = not work

work = False

keyboard.add_hotkey("0", change)

while True:
    if work:
        mouse.click(button='left')
        time.sleep(0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)