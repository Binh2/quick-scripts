import numpy
import pyperclip
from PIL import ImageGrab
import cv2

if __name__ == '__main__':
    image = ImageGrab.grabclipboard()
    image.save(r'C:\Users\ADMIN\Downloads\clipboard.png', 'PNG')
    