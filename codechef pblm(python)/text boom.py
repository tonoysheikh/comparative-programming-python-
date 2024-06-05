import pyautogui
import time

for count in range(0,101):
    pyautogui.typewrite("Hello")
    time.sleep(3)
    pyautogui.press("enter")