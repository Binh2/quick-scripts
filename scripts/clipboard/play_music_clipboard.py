import validators
from playsound import playsound
import pyperclip
import requests

if __name__ == '__main__':
    prev_url = ''
    try:
        with open('music.txt', 'r') as f:
            prev_url = f.read()
    except:
        pass
    url = pyperclip.paste()
    if prev_url == url:
        playsound('music.mp3')
    elif validators.url(url):
        music = requests.get(url)
        with open('music.mp3', 'wb') as f:
            f.write(music.content)
        with open('music.txt', 'w') as f:
            f.write(url)
        playsound('music.mp3')
    else:
        print('Invalid url')