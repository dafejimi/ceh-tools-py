import sys
import socket
import threading

def server_loop(local_host,local_port,remote_host,remote_port,receive_first):

        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        try:
                server.bind((local_host,local_port))
        except:
                print("[!!] Failed to listen on %s:%d % (local_host,local_port)")
                print("[!!] Check for other listening sockets or correct permissions.")
                sys.exit(0)
                print("[*] listening on %s:%d" % (local_host,local_port))

                server.listen(5)

                while true:
                        client_socket, addr = server.accept()

                        # print out the local connection information
                        print("[==>] Received incoming connection from %s:%d" % (addr[0],addr[1])

                        # start a thread to talk to the remote
                        proxy_thread = threading.Thread(target=proxy_handler, args=(client_socket,remote_host,remote_port,receive_first))

                        proxy_thread.start()

def main():

    # no fancy command-line parsing here
    if len(sys.argv[1:]) != 5
        print("Usage: ./proxy.py [localhost] [localport] [remotehost][remoteport] [receive first]")
        print("Example: ./proxy.py 127.0.0.1 9000 10.12.132.1 9000 True")
        sys.exit(0)

    # setup local listening parameters
    local_host = sys.argv[1]
    local_port = int(sys.argv[2])

    # setup remote target
    remote_host = sys.argv[3]
    remote_port = sys.argv[4]

    # this tells our proxy to connect and receive data
    # before sending to the remote host
    receive_first = sys.argv[5]

    if "True" in receive first:
        receive_first = True
    else:
        receive_first = False

    # now spin up our listening socket
    server_loop(loacal_host,local_port,remote_host,remote_port,receive_first)

main()

def proxy_handler(client_socket, remote_host, remote_port, receive_first)

    # connect to the remote host
    remote_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    remote_socket.connect((remote host,remote port))

    # receive data from the remote end if necessary
    if receive_first:

            remote_buffer = receive_from(remote_socket)
            hexdump(remote_buffer)

            # send it to our response handler
            remote_buffer = response_handler(remote_buffer)

            # if we have data to send to our local client, send it
            if len(remote_buffer):
                    print("[<==] Sending%d bytes to localhost." % len(remote_buffer))
                    client_socket.send(remote_buffer)
    # now lets loop and read from local,
    # send to remote, send to local
    #rinse, wash, repeat
    while True:

        #read from local host
        local_buffer = receive_from(client_socket)

        if len(local_buffer):

            print("[==>] received %d bytes from localhost." %len(local_buffer))
            hexdump(local_buffer)

            # send it to our request handler
            local_buffer = request_handler(local_buffer)

            # send off the data to the remote host
            remote_socket.send(local_buffer)
            print("[==>] Sent to remote")

            # receive back the response
            remote_buffer = receive_from(remote_socket)

            if len(remote_buffer):

                print("[<==] received %d bytes from remote" % len(remote_buffer))
                hexdump(remote_buffer)

                # send to our response handler
                remote_buffer = response_handler(remote_buffer)

                #send the response to the local socket
                client_socket.send(remote_buffer)

                print("[<==] Sent to local host")

           # if no more data on either side, close the connections
           if not len(local_buffer) or not len(remote_buffer):
                   client_socket.close()
                   remote_socket.close()
                   print("[*] No more data. Closing connections.")

                   break

     
# this is a pretty hex dumping function directly taken from the comments here:
# http://code.activestate.com/recipes/142812-hex-dumper/
def hexdump(src, length=16):
    result = []
    digits = 4 if isinstance(src, unicode) else 2
    for 1 in xrange(0, len(src), length):
        s = src[1:1+length]
        hexa = b' '.join(["%0*X" % (digits, ord(x)) for x in s])
        text = b''.join([x if 0x20 <= ord(x) < 0x7F else b'.' for x in s])
        result.append( b"%04X  %-*s  %s" % (i, length*(digits+1), hexa, text) )

    print(b'\n'.join(result))

def receive_from(connection):

    buffer =""

    # we get a two second timeout depending on your target, this may need to be adjusted
    connection.settimeout(2)

        try:
                #keep reading into the buffer until theres no more data or we time out
                while True:
                        data = connection.recv(4096)

                        if not data:
                                break

                        buffer += data
        except:
                pass

        return buffer

    # madify any requests destined for the remote host
    def request_handler(buffer):
        # perform packet modifications
        return buffer

    # modify any responses destined for the local host
    def response_handler(buffer):
        #perform packet modifications
        return buffer
    
