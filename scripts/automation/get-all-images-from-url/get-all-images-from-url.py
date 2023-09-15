import requests
from io import BytesIO
from bs4 import BeautifulSoup
import sys
import shutil
from urllib.parse import urlparse
import traceback
import validators
import matplotlib.pyplot as plt
from PIL import Image

with open('./counter.txt', 'r') as f:
    i = int(f.read())

url = "https://www.geeksforgeeks.org/"
try:
    url = sys.argv[1]
except:
    print("Please input a url")
    
html = requests.get(url).text

soup = BeautifulSoup(html, 'html.parser')
for item in soup.find_all('img'):
    try:
        image_url = item['src']
        if validators.url(image_url):
            print(image_url)
            res = requests.get(image_url, stream=True)
            res.raw.decode_content = True
            # Try getting image url if exists (mostly from Yandex)
            image_filename = ''
            try:
                image_filename = parse_qs(urlparse(url).query)['img_url']
            except:
                pass
                
            image_filename = urlparse(image_url).path.replace('/', '-').replace('\\', '-').replace('.', '-')[-20:] + '.png'
            save_location = './images/' + str(i) + '_' + image_filename
            
            img = Image.open(BytesIO(res.content))
            img.save(save_location)
            i += 1
            del res
    except:
        traceback.print_exc()

with open('./counter.txt', 'w') as f:
    f.write(str(i))