import zipfile
import optparse
from threading import Thread
def extracFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print("[+] Found Password" + password + "\n")
    except:
        pass

def main():
    parser = optparse.OptionParser("usage%prog "+"-f <zipfile> -d <dictionary>")
    parser.addoption('-f', dest='zname', type='string', help='specify zip file')
    parser.addoption('-d', dest=dname, type='string', help='specify dictionary file')
    (options, args) = parser.parse_args()
    
    if (options.zname == None) | (options.dname == None):
        print (parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
        
    zFile = zipfile.Zipfile('evil.zip')
    passFile = open('dictionary.txt')
    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile, args=(zFile,password))
        t.start()

if __name__ == "__main__":
    main()
