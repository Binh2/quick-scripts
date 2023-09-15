import numpy
import pyperclip
from PIL import ImageGrab
import cv2

def read_qr_code(cv2_image):
    try:
        detect = cv2.QRCodeDetector()
        value, points, straight_qrcode = detect.detectAndDecode(cv2_image)
        return value
    except:
        return

if __name__ == '__main__':
    pil_image = ImageGrab.grabclipboard().convert('RGB')
    cv2_image = numpy.array(pil_image)
    url = read_qr_code(cv2_image)
    pyperclip.copy(url)