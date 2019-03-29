#! python3
# combine_pdfs.py -- Combines all the PDFs in the current working directory into
# into a single PDF.

import os
import PyPDF2


# Get all the PDF filenames.
PDF_FILES = []

for filename in os.listdir("./chapter13"):

    if filename.endswith(".pdf"):

        PDF_FILES.append(filename)

PDF_FILES.sort(key=str.lower)
print(PDF_FILES)

PDF_WRITER = PyPDF2.PdfFileWriter()

# Loop through all the PDF files.
for filename in PDF_FILES:

    pdf_file_obj = open("./chapter13/" + filename, "rb")
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)

    # Loop through all the pages (except the first) and add them.
    for pageNum in range(1, pdf_reader.numPages):

        page_obj = pdf_reader.getPage(pageNum)
        PDF_WRITER.addPage(page_obj)

# Save the resulting PDF to a file.
PDF_OUTPUT = open("./chapter13/all_minutes.pdf", "wb")
PDF_WRITER.write(PDF_OUTPUT)
PDF_OUTPUT.close()
