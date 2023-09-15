# from PyPDF2 import PdfWriter, PdfReader

# def read_pdf(filename: str, num_of_pages: int):
    # input_pdf = PdfReader(open(filename, "rb"))
    
    # for i in range(num_of_pages):
        # print(input_pdf.pages[i].get_contents())

import sys, fitz
import argparse

def read_pdf(filename, num_of_pages):
    doc = fitz.open(filename)  # open document
    for page in doc:  # iterate through the pages
        pix = page.get_pixmap()  # render page to an image
        print(pix)
        if page.number >= num_of_pages + 1:
            continue
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Read PDF')
    parser.add_argument('-f', '--file', default='document.pdf')
    parser.add_argument('-n', '--number-of-pages', default=1, type=int)
    args = parser.parse_args()
    read_pdf(args.file, args.number_of_pages)