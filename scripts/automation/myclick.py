import win32api, win32con, win32gui
import sys
import utilities
import pyautogui
import time

utilities.minimize_window()

(x, y) = win32gui.GetCursorPos()
if len(sys.argv) > 3:
    for i in range(int(float(sys.argv[2]))):
        pyautogui.click(x, y)
if len(sys.argv) == 3:
    for i in range(int(float(sys.argv[2]))):
        pyautogui.click(x, y)
else:
    pyautogui.click(x, y)
