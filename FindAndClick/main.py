from screen_search import *
import keyboard
import pyautogui
import win32api
from win32con import *
q = True
while q == True:
    search = Search("sample.png")
    pos = search.imagesearch()
    if pos[0] != -1:
        pyautogui.moveTo(pos[0]+5, pos[1]+5)
        pyautogui.click()
    else:
        win32api.mouse_event(MOUSEEVENTF_WHEEL, pos[0], pos[1], -50, 0)
    time.sleep(0.25)
    if keyboard.is_pressed("q"):
        q = False
    else:
        pass