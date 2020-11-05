import sys
import os
from PyPDF2 import PdfFileMerger

merger = PdfFileMerger()

for i in range(30):
    merger.append('croppedPDF'+str(i)+'.pdf')

merger.write("results.pdf")
merger.close()