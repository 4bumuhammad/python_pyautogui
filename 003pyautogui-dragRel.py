import pyautogui
import time

time.sleep(3)

pyautogui.mouseDown(-100, -241, button="left")
pyautogui.moveTo(-50, -241, 3)
pyautogui.mouseUp()
pyautogui.moveTo(0,-241, 3)

time.sleep(1)
distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0, 1, button="left")
    distance = distance - 10
    pyautogui.dragRel(0,distance, 1, button="left")
    pyautogui.dragRel(-distance, 0, 1, button="left")
    distance = distance - 10
    pyautogui.dragRel(0,-distance, 1, button="left")
time.sleep(2)