import sys
import os
import pdf2image 
import PIL
from PIL import Image
from pdf2image import convert_from_path, convert_from_bytes

poppler_path = r"YOUR PATH TO POPPLER BIN" 
print("imports successful")


for i in range(30):
    im1 = Image.open('cropped'+str(i)+'.png')
    im1.save('croppedPDF'+str(i)+'.pdf', 'pdf')
