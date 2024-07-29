import socket
from binascii import hexlify

def convert_ipv4():
    
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    packed_ip = socket.inet_aton(ip_address)
    print("packed ip is %s" % hexlify(packed_ip))

    return


convert_ipv4()



