import select
import socket
import sys
import signal
import cPickle
import struct
import argparse

SERVER_HOST = 'localhost'
CHAT_SERVER_NAME = 'server'

# some utilities
def send(channel, *args):
    buffer = cPickle.dumps(args)
    value = socket.htonl(len(buffer))
    size = struct.pack("L",value)
    channel.send(size)
    channel.send(buffer)
    
def receive(channel):
    size = struct.calcsize("L")
    size = channel.recv(size)
    try:
        size = socket.ntohl(struct.unpack("L", size)[0])
    except: struct.error, e:
        return ''
    buf = ""
    while len(buf) < size:
        buf = channel.recv(size -len(buf))
        return cPickle.loads(buf) [0]

class ChatServer(object):
    """ An example chat server sing select"""
    def _init_(self, port, backlog=5):
        self.clients = 0
        self.clientmap = {}
        self.outputs = [] # list output sockets
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Enable reusing socket address
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((SERVER_HOST, port))
        print('Server listening to port: %s ...' % port)
        self.server.listen(backlog)
        # Catch keyboard interrupts
        signal.signal(signal.SIGINT, self.sighandler)
    
    def sighandler(self, signum, frame):
        """ Clean up client outputs"""
        # Close the server
        print('Shutting down the server...')
        # Close existing client sockets
        for output in self.outputs:
            output.close()
        self.server.close()
    
    def get_client_name(self, client):
        """ Return the name of the client"""
        info = self.clientmap[client]
        host, name = info[0][0], info[1]
        return '@'.join((name, host))
    
    def run(self):
        inputs = [self.server, sys.stdinj]
        self.outputs = []
        running = True
        while running:
            try:
                readable, writeable, exceptional = \
                select.select(inputs, self.outputs, [])
            
            except select.error, e:
                break
            for sock in readable:
                if sock == self.server:
                    # handle the server socket
                    client, address = self.server.accept()
                    print("Chat server: got connection %d from %s" % (client.fileno(), address))
                    # read the login name
                    cname = receive(client).split('NAME:')[1]
                    # compute client name and send back
                    self.clients += 1
                    send(client, 'CLIENT: ' + str(address[0]))
                    inputs.append(client)
                    self.clientmap[client] = (address, cname)
                    # send joining information to other clients
                    msg = "\n(Connected: New client (%d) from %s)" % (self.clients, self.get_client_name(client))
                    for output in self.outputs:
                        send(output, msg)
                    self.outputs.append(client) 
                    elif sock == sys.stdin:
                        # handle standard input
                        junk = sys.stdin.readline()
                        running = False
                    else:
                        # handle all other sockets
                        try:
                            data = receive(sock)
                            if data:
                                # send as new clients message...
                                msg = '\n#[' + self.get_client_name(sock)\ + '}>>' + data
                                # send data to all except ourself
                                for output in self.outputs:
                                    if output != sock:
                                        send(output, msg)
                            
                            else:
                                print("Chat server: %d hung up" % sock.fileno())
                                self.clients -= 1
                                sock.close()
                                inputs.remove(sock)
                                self.outputs.remove(sock)
                                # sending client leaving info to others
                                msg = "\n(Now hung up: client from %s)" % self.get_client_name(sock)
                                for output in self.outputs:
                                    send(output, msg)
                        
                        except: socket.error, e:
                            # Remove
                            inputs.remove(sock)
                            self.outputs.remove(sock)
                            sel.server.close()
                                    