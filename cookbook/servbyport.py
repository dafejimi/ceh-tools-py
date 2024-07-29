import socket


print("port: %s=> service name: %s" % (53, socket.getservbyport(53, 'udp')))
