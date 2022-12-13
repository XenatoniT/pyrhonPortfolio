from getpass import getpass
from PyPDF2 import PdfFileWriter, PdfFileReader

pdfwriter = PdfFileWriter()
pdf = PdfFileReader('file_pdf.pdf')

for page in range(pdf.numPages):
    pdfwriter.add_page(pdf.pages[page])

password = getpass(prompt='Введите пароль: ')
pdfwriter.encrypt(password)

with open('protected.pdf', 'wb)') as file:
    pdfwriter.write(file)
