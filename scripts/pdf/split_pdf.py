from PyPDF2 import PdfWriter, PdfReader

def split_pdf(filename: str, num_of_pages: int):
    input_pdf = PdfReader(open(filename, "rb"))
    num_of_pages_in_splitted = len(input_pdf.pages) // num_of_pages + 1
    
    for i in range(num_of_pages):
        output = PdfWriter()
        for j in range(i * num_of_pages_in_splitted, min((i + 1) * num_of_pages_in_splitted, len(input_pdf.pages))):
            output.add_page(input_pdf.pages[j])
        with open("%s%s.pdf" % (filename.split('.')[0], i), "wb") as output_pdf:
            output.write(output_pdf)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(prog='Split PDF')
    parser.add_argument('-f', '--file', default='document.pdf')
    parser.add_argument('-n', '--number-of-pages', default=2, type=int)
    args = parser.parse_args()
    split_pdf(args.file, args.number_of_pages)
