import socket

def find_service_name():
    for port in [80, 25]:
        print("port: %s => service name: %s" % (port,socket.getservbyport(port, 'tcp')))
    print("port: %s=> service name: %s" % (53, socket.getservbyport(53, 'udp')))


find_service_name()


print("port:8080 => service name: %s" % (8080,socket.getservbyport(8080, '')))
