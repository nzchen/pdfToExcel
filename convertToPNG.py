#convert pdf to image file 

import sys
import os
import pdf2image 
import PIL
from PIL import Image
from pdf2image import convert_from_path, convert_from_bytes

poppler_path = r"YOUR PATH TO POPPLER BIN" 
print("imports successful")

images = convert_from_path('IS70150_C.pdf', dpi=200, output_folder=None, 
                            first_page=None, last_page=None, fmt='ppm', 
                            jpegopt=None, thread_count=1, userpw=None, 
                            use_cropbox=False, strict=False, transparent=False, 
                            single_file=False, 
                            poppler_path=r"C:\\Users\\Nathan\\Documents\\NCSU\Delta\\Release-20.10.0\\poppler-\\bin", 
                            grayscale=False, size=None, paths_only=False, use_pdftocairo=False, timeout=600)

#i = 0
#for image in images:
#    images[i].save('test'+str(i)+'.png', 'png')
#    i = i + 1
#print(i)

