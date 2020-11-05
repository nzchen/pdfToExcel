import sys
import os
import os.path 
import pdf2image 
import PIL
from PIL import Image
from pdf2image import convert_from_path, convert_from_bytes
from PyPDF2 import PdfFileMerger
import PyPDF2

poppler_path = r"C:\\Users\\Nathan\\Documents\\NCSU\Delta\\Release-20.10.0\\poppler-\\bin" 
quit = 0 
pdfFile = input('Enter PDF name: ')

while True:   
    if pdfFile == 'quit':
        quit = 1
        break
    elif os.path.isfile(pdfFile+".pdf"):
        break 
    else:
        pdfFile = input("Invalid pdf, enter new pdf name or quit to exit program: ")

if(not quit):
    if(os.path.isfile(pdfFile+"Edited.pdf")):
        deleteONot = input('Edited file currently exists, would you like to delete and rewrite? (y/n): ')
    if(deleteONot == 'y'):
        os.remove(pdfFile+"Edited.pdf")
        startPage = int(input('Enter Starting Page Number of Bill of Materials: '))
        endPage = int(input('Enter Ending Page Number of Bill of Materials: '))
        totalPage = endPage-startPage+1

        images = convert_from_path(pdfFile+".pdf", dpi=200, output_folder=None, 
                            first_page=None, last_page=None, fmt='ppm', 
                            jpegopt=None, thread_count=1, userpw=None, 
                            use_cropbox=False, strict=False, transparent=False, 
                            single_file=False, 
                            poppler_path=r"C:\\Users\\Nathan\\Documents\\NCSU\Delta\\Release-20.10.0\\poppler-\\bin", 
                            grayscale=False, size=None, paths_only=False, use_pdftocairo=False, timeout=600)
        #converts to PNG FILE
        i = 0
        for i in range(startPage-1, endPage):
            images[i].save('test'+str(i)+'.png', 'png')
            i = i + 1
        #crops the image
        for i in range(startPage-1, endPage):
            im = Image.open('test'+str(i)+'.png')
            left = 1360
            right = 3340
            bottom = 2200
            top = 100
            im = im.crop((left,top,right,bottom))
            im.save('cropped'+str(i)+'.png', 'png')
        #converts the cropped image back to a pdf
        for i in range(startPage-1, endPage):
            im1 = Image.open('cropped'+str(i)+'.png')
            im1.save('croppedPDF'+str(i)+'.pdf', 'pdf')
        #merges the pdf
        merger = PdfFileMerger()
        for i in range(startPage-1, endPage):
            merger.append('croppedPDF'+str(i)+'.pdf')
        merger.write(pdfFile+"Edited.pdf")
        merger.close()
        #removes unnecesary files
        for i in range(startPage-1, endPage):
            os.remove('test'+str(i)+'.png')
            os.remove('cropped'+str(i)+'.png')
            os.remove('croppedPDF'+str(i)+'.pdf')
            i = i + 1
