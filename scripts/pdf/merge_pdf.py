import sys
from PyPDF2 import PdfReader, PdfWriter

def merge_pdf(input_files, output_filename):
    input_streams = []
    output_stream = None
    try:
        output_stream = open(output_filename, 'wb')
        for input_file in input_files:
            input_streams.append(open(input_file, 'rb'))
        writer = PdfWriter()
        for reader in map(PdfReader, input_streams):
            for n in range(len(reader.pages)):
                writer.add_page(reader.pages[n])
        writer.write(output_stream)
    finally:
        for f in input_streams:
            f.close()
        if output_stream: 
            output_stream.close()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(prog='Merge PDF')
    parser.add_argument('-f', '--files', nargs='+', default=[])
    parser.add_argument('-i', '--index', type=int, default=0)
    parser.add_argument('-n', '--number-of-files', type=int, default=2)
    parser.add_argument('-b', '--base-filename', default='document.pdf')
    args = parser.parse_args()
    
    output_filename = args.base_filename.split('.')[0] + '_result.pdf'
    if args.files:
        merge_pdf(args.files, output_filename)
    else:
        merge_pdf([ args.base_filename.split('.')[0] + str(i) + '.pdf' for i in range(args.index, args.index + args.number_of_files)], output_filename)