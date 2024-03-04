import pyautogui
import time

# pyautogui.moveTo(-655,-404)
# pyautogui.click()
# pyautogui.write("bismillah, assalamualaikum warahmatullah wabarakatuh.")

## Reference : 
## https://www.youtube.com/watch?v=3PekU8OGBCA&t=251s
## 19.50s

time.sleep(3)
# print(pyautogui.size())                   # Prints the resolution of screen --> Size(width=1440, height=900)
# print(pyautogui.position())               # Prints the current position of the mouse --> Point(x=-1771, y=-1049)
# pyautogui.moveTo(-884, -431,3)
# pyautogui.moveRel(-655, -404,3)           # Move the mouse relative to its current position
# pyautogui.click(-655, -404, 3, 3, button="left")
# pyautogui.tripleClick()
# pyautogui.doubleClick()
# pyautogui.tripleClick()
# pyautogui.doubleClick()

# pyautogui.scroll(-100)
# time.sleep(1)
# pyautogui.scroll(50)
# time.sleep(1)
# pyautogui.scroll(-20)
# time.sleep(1)
# pyautogui.scroll(-60)


## Example of mouse up and down
## Used https://jspaint.app

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