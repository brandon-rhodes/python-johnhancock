"""Support for command: python -m johnhancock"""

import argparse
from StringIO import StringIO
from pyPdf import PdfFileWriter, PdfFileReader
from reportlab.pdfgen.canvas import Canvas

class Watermark(object):

    def __init__(self):
        self.canvas = Canvas('watermark.pdf', pagesize=(612, 792))

    def sign(self, x, y, phrases=(), dx=0):
        c = self.canvas
        c.drawImage('../signature.png', x=x, y=y, width=120, height=100,
                    mask='auto', preserveAspectRatio=True, anchor='sw')
        for phrase in phrases:
            y -= 14
            c.drawString(x + 20 + dx, y, phrase)

    def page(self):
        self.canvas.showPage()
        return PdfFileReader(StringIO(self.canvas.getpdfdata())).getPage(0)

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('pdfpath', metavar='PDF-file', help='PDF file to sign')
    # parser.add_argument('-P', dest='pages', help='page to sign')

    args = parser.parse_args()

    # Produce the PDF, overlaying the signature where directed.

    document = PdfFileReader(open(args.pdfpath, 'rb'))
    output = PdfFileWriter()

    pages = document.pages

    w = Watermark()
    w.sign(150, 264.5, []) #['Brandon C Rhodes'])
    w.canvas.drawString(432, 268, '22 July 2013')
    pages[0].mergePage(w.page())

    output.addPage(pages[0])

    output.write(open('signed-document.pdf', 'wb'))

if __name__ == '__main__':
    main()
