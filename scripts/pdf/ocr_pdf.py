from PyPDF2 import PdfReader, PdfWriter
import argparse
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def ocr_pdf(input_filename, output_filename):
    input_stream = None
    output_stream = None
    try:
        input_stream = open(input_filename, 'rb')
        output_stream = open(output_filename, 'wb')
        
        reader = PdfReader(input_stream)
        writer = PdfWriter()
        
        for i in range(len(reader.pages)):
            print(reader.pages[i])
            if not reader.pages[i].images:
                continue
            
            image = reader.pages[i].images[0]
            pdf = pytesseract.image_to_pdf_or_hocr(image, extension='pdf')
            writer.add_page(pdf.pages[0])
        writer.write(output_stream)
    finally:
        if input_stream:
            input_stream.close()
        if output_stream:
            output_stream.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='OCR PDF')
    parser.add_argument('-f', '--filename', default='document.pdf')
    args = parser.parse_args()
    
    ocr_pdf(args.filename, args.filename.split('.')[0] + "_result.pdf")