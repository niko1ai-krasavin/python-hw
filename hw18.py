#!/usr/bin/python3

# It is necessary to add the values of width and length in pixels as parameters
# for example '480, 640'

import sys
from PIL import Image, ImageOps


size1 = sys.argv[1].replace(',', '')
size2 = sys.argv[2]
size = (int(size1), int(size2))

image = Image.open('IMG_hw17.jpg')
file_name = 'IMG_hw17.jpg'

thumb = ImageOps.fit(Image.open(file_name), size, Image.ANTIALIAS)
thumb.save('{}_thumb.jpg'.format(file_name[:file_name.rfind('.')]), "JPEG")
