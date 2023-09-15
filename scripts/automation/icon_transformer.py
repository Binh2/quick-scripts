from PIL import Image
filename = "toast.png"
img = Image.open(filename)
img.save('toast.ico')
