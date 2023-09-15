import urllib.request

with open("./input.txt", "r") as file:
    urls = file.read().split('\n')
    for i in range(len(urls)):
        url = urls[i]
        ext = url.split('.')[-1]
        urllib.request.urlretrieve(url, "./images/" + str(i) + '.' + ext)
    