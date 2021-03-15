"""

Desired file format:

    Username_1 69 0 0 46 23 0 69 5,2800 zł
    Username_2 23 0 0 9 24 10 33 1,4000 zł
    Username_3 64 0 0 0 64 0 64 1,0000 zł
    Username_4 53 0 0 0 53 0 53 0,9000 zł
    Username_5 9 0 0 4 5 0 9 0,5400 zł
    Username sometimes contains many words 23 0 0 0 23 0 23 0,3700 zł
    Username_7 15 0 1 0 16 2 17 0,3200 zł
    Username_8 17 0 0 0 17 0 17 0,2700 zł
    Username_9 Film 0 0 0 1 7 8 8 0,2500 zł
    .
    .
    Username_n 1 0 0 0 1 0 1 0,0200 zł

"""

import PyPDF2

pdfFileObj  = PyPDF2.PdfFileReader('Print_report.pdf')
numbers_of_pages = pdfFileObj.numPages

extractedText = ""
for i in range(numbers_of_pages):
    extractedText += pdfFileObj.getPage(i).extractText()

text = extractedText

pdfFileObj.close()




