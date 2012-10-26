"""Support for command: python -m johnhancock"""

import argparse

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('pdfpath', metavar='PDF-file', help='PDF file to sign')
    parser.add_argument('-P', dest='pages', help='page to sign')

    args = parser.parse_args()

    print args

main()
