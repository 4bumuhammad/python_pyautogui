import pyautogui

img1 = pyautogui.screenshot()
img1.save('testimagescr1.png')

im2 = pyautogui.screenshot(region=(-173, -358, 940, 360))
im2.save("testimagescr2.png")


print('screenshot taken')

