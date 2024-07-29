import optparse
import socket
from socket import *
screenLock = Semaphore(value=1)
def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('ViolentPython\r\n')
        results = connSkt.recv(100)
        screenLock.acquire()
        print("[+]%d/tcp open"% tgtPort)
        print("[+] " +str(results))
    except:
        screenLock.acquire()
        print("[-]%d/ tcp closed"% tgtPort)
    finally:
        screenLock.release()
        connSkt.close()

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print("[-] cannot resolve '%s': Unknown Host" %tgtHost)
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print("\n[+] Scan Results for:" + tgtName[0])
    except:
        print("\n[+] Scan Results For:" + tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print("Scanning port " + tgtPort)
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()
        
def main():
    parser = optparse.OptionParser("usage%prog "+"-H <target host> -p <target port>")
    parser.addoption('-H', dest='tgtHost', type='string', help='specify target host')
    parser.addoption('-p',dest='tgtPort', type='string', help='specify target port(s) separated by comma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPort = str(options.tgtPort).split(', ')
    if (tgtHost == None)| (tgtPort == None):
        print("[-] yoy must specify a target host and port(s).")
        exit(0)
    portScan(tgtHost, tgtPorts)
if __name__ ="__main__":
    main()
