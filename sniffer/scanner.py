--snip--
class IP(Structure):
--snip--

class ICMP(Structure):

    _fields_ = [
        ("type",         c_ubyte),
        ("code",         c_ubyte),
        ("checksum",     c_ushort),
        ("unused",       c_ushort),
        ("next_hop_mtu", c_ushort)
        ]

    def _new_(self, socket_buffer):
        return self.from_buffer_copy(socket_buffer)

    def _init_(self, socket_buffer):
        pass

--snip--

    print("protocol: %s %s ->  %s" % (ip_header.protocol, ip_header.src_address, ip_header.dst_address))

    #if its ICMP, we want it
    if ip_header.protocol == "ICMP":

        #calculate where our ICMP packet starts
        offset = ip_header.ihl * 4
        buf = raw_buffer[[offset:offset + sizeof(ICMP)]

        # create our ICMP structure
        icmp_header = ICMP(buf)

        print("ICMP -> Type %d Code: %d" % (icmp_header.type, icmp_header.code))



import threading
import time
from netaddr import IPNetwork,IPAddress
--snip--

# host to listen on
host = "192.168.0.187"

# subnet to target
subnet = "192.168.0.0/24"

# magic string we'll check ICMP responses for
mzgic_message = "PYTHONRULES!"

# this sprays out the UDP datagrams
def udp_sender(subnet,magic_message):
    time.sleep(5)
    sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    for ip in IPNetwork(subnet):
        try:
            sender.sendto(magic_message,("%s" % ip,65212))
        except:
            pass

--snip--

#start srnding packets
t = threading.Thread(target=udp_sender,args=(subnet,magic_message))
t.start()

--snip--
try:
    while True:
        --snip--
            # print("ICMP -> type: %d code: %d" % (icmp_header.type, icmp_header.code))

                # now check for the TYPE 3 and CODE
                if icmp_header.code == 3 and icmp_header.type == 3:

                    # make sure host is in our target subnet
                    if IPAddress(ip_header.src_address) in IPNetwork(subnet):

                        # make sure it has our magic message
                        if raw_buffer[len(raw_buffer-len(magic_message):)] ==
                        magic_message:
                            print("Host up: %s" % (ip_header.src_address))
