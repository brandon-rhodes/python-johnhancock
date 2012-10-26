"""Support for command: python -m johnhancock"""

import argparse
from StringIO import StringIO
from pyPdf import PdfFileWriter, PdfFileReader
from reportlab.pdfgen.canvas import Canvas

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('pdfpath', metavar='PDF-file', help='PDF file to sign')
    # parser.add_argument('-P', dest='pages', help='page to sign')

    args = parser.parse_args()

    # Draw the signature and date on a watermark page.

    # from reportlab.lib.utils import ImageReader

    canvas = Canvas('watermark.pdf')
    canvas.drawImage('../signature.png', x=134, y=124, width=160, height=160,
                     mask='auto', preserveAspectRatio=True, anchor='sw')
    canvas.drawString(380, 130, 'October 26, 2012')
    canvas.showPage()
    rendering = PdfFileReader(StringIO(canvas.getpdfdata()))
    watermark = rendering.getPage(0)

    # Produce the PDF, overlaying the signature where directed.

    document = PdfFileReader(open(args.pdfpath, 'rb'))
    output = PdfFileWriter()

    #print dir(document)
    for page in (document.pages[-1], ):
        page.mergePage(watermark)
        output.addPage(page)

    # pdfdata = StringIO()
    # output.write(pdfdata)

    output.write(open('signed-document.pdf', 'wb'))

    # return HttpResponse(pdfdata.getvalue(), content_type='application/pdf')
    # print args

main()
