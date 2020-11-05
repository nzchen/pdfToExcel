#crops the image file

import sys
import os
import pdf2image 
import PIL
from PIL import Image
from pdf2image import convert_from_path, convert_from_bytes

poppler_path = r"C:\\Users\\Nathan\\Documents\\NCSU\Delta\\Release-20.10.0\\poppler-\\bin" 
print("imports successful")

#im = Image.open('test1.png')
#width, height = im.size
#print(width)
#print(height)
#left = 1360
#right = 3340
#bottom = 2200
#top = 100
#im = im.crop((left,top,right,bottom))
#im.show()

for i in range(30):
    im = Image.open('test'+str(i)+'.png')
    left = 1360
    right = 3340
    bottom = 2200
    top = 100
    im = im.crop((left,top,right,bottom))
    im.save('cropped'+str(i)+'.png', 'png')

