from python_imagesearch.imagesearch import *
import pyautogui
import win32api
import keyboard
import mouse
import time

exit_hotkey = "delete" #hotkey na vypnutí programu ("example", "shift+example")
image_sample = "sample.png"

x1 = 0
y1 = 0
x2 = 1920
y2 = 1080
lookfor = []

#Area selection kde program vidí
while True:
    if mouse.is_pressed("left"):
        x1, y1 = mouse.get_position()
        print(x1, y1)
        time.sleep(0.3)
    elif mouse.is_pressed("right"):
        x2, y2 = mouse.get_position()
        print(x2, y2)
        time.sleep(0.3)
    elif keyboard.is_pressed(exit_hotkey):
        break
    time.sleep(0.01)

time.sleep(2)


while True:

    pos = imagesearcharea(image_sample, 0, 0, int(x2), int(y2), 0.8)
    if pos[0] != -1:
        print("position : ", pos[0], pos[1])
    else:
        print("image not found")

pyautogui.LocateOnScreen