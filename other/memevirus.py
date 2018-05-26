import os
from PIL import Image
import time
import random
import imghdr

directory = "Memes/"

arr = os.listdir(directory)
upbound = len(arr) - 1
imagetypes = set(['gif', 'png', 'jpeg', 'jpg', 'bmp'])
last = ""

while True:
    file_name = directory + arr[random.randint(0, upbound)]
    print([imghdr.what(file_name)], imagetypes)
    img = Image.open(file_name)
    if imghdr.what(file_name) in imagetypes and file_name != last:
        img.show()
        time.sleep(random.randint(2,5))
        last = file_name


