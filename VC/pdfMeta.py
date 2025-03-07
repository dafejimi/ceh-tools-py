import pyPdf
import optpasre
from pyPdf import PdfFileReader
def printMeta(fileName):
    pdfFile = PdfFileReader(file(fileName, 'rb'))
    docInfo = pdfFile.getDocumentInfo()
    print("[*] PDF Metadata For: " + str(fileName))
    for metaItem in docInfo:
        print("[+] " + metaItem + ':' + docInfo[metaItem])
def main():
    parser = optparse.OptionParser('usage%prog '+ ' -F <PDF file name>')
    parser.add_option('-F', dest='fileName', type='string', help='specify PDF fle name')
    (options, args) = parser.parse_args()
    fileName = options.fileName
    if fileName == None:
        print(parser.usage)
        exit(0)
    else:
        printMeta(fileName)

if __name__ == '__main__':
    main()
