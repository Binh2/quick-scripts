import ctypes
import os
import time

def change_python_title(title = os.path.basename(__file__)):
    ctypes.windll.kernel32.SetConsoleTitleW(title)
