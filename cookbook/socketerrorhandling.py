import sys
import socket
import argparse

def main():
    # setup argument parsing
    parser = argparse.ArgumentParser(description='Socket Error Examples')
    parser.add_argument('--host', action="store", dest="host", required="False")
    parser.add_argument('--port', action="store", dest="port", type="int", required="False")
    parser.add_argument('--file', action="store", dest="file", required="False")
    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.host
    filename = given_args.file

    # first try-except block
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except socket.error, e:
        print('Error creating socket: %s' % e)
        sys.exit(1)

    # second try-except block
    try:
        s.connect((host,port))
    except socket.gaierror, e:
        print('Address related error connecting to server: %s' % e)
        sys.exit(1)
    except socket.error, e:
        print('connection error: %s' % e)
        sys.exit(1)

    # third try-except block
    try:
        s.sendall("GET %s HTTP/1.0\r\n\r\n" % filename)
    except socket.error, e:
        print('error sending data: %s' % e)
        sys.exit(1)

    while 1:
        # fourth try-except block
        try:
            buf = s.recv(2048)
        except socket.error, e:
            print('error receiving data: %s' % e)
            sys.exit(1)
        if not len(buf):
            break
        # write the received data
        sys.stdout.write(buf)


main()
        
        
