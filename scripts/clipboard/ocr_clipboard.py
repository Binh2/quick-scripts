from PIL import ImageGrab
import pytesseract
import pyperclip

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = ImageGrab.grabclipboard()
text = pytesseract.image_to_string(img)
pyperclip.copy(text)