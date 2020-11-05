import sys
import os
import PyPDF2
from PyPDF2 import PdfFileMerger

print('imports success')

startPage = int(input('Enter Starting Page Number of Bill of Materials: '))
endPage = int(input('Enter Starting Page Number of Bill of Materials: '))
totalPage = endPage-startPage+1
trueStart = startPage - 1
merger = PdfFileMerger()

for i in range(totalPage):
    merger.append('croppedPDF'+str(trueStart)+'.pdf')
    trueStart = trueStart + 1

merger.write("resultsSelected.pdf")
merger.close()


