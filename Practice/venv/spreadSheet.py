print("This is the script to work with SpreadSheets and PDF")

import csv
import PyPDF2

data = open("example.csv",encoding='utf-8')
csv_data = csv.reader(data)

data_lines = list(csv_data)

# for line in data_lines[:10]:
#     print(line)


f = open("Working_Business_Proposal.pdf",'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
print(pdf_reader.numPages)

page_one = pdf_reader.getPage(0)
page_one_text = page_one.extractText()
print(page_one_text)