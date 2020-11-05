import sys
import os
import pdf2image 
import PIL
from PIL import Image
from pdf2image import convert_from_path, convert_from_bytes

poppler_path = r"C:\\Users\\Nathan\\Documents\\NCSU\Delta\\Release-20.10.0\\poppler-\\bin" 
print("imports successful")


for i in range(30):
    im1 = Image.open('cropped'+str(i)+'.png')
    im1.save('croppedPDF'+str(i)+'.pdf', 'pdf')
