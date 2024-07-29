import socket
import struct
import sys
import time

NTP_SERVER = "0.uk.pool.ntp.org"
TIME1970 = 2208988800L

def sntp_client():
	client = socket.socket(socket.socket(socket.AF_INET, socket.SOCK_DGRAM))
	data = '\xlb' + 47 * '\0'
	client.sendto(data, (NTP_SERVER, 123))
	data, address = client.recvfrom(1024)
	if data:
		print('response received from:', address)
	t =struct.unpack( '!12I', data)[10]
	t -= TIME1970
	print ('\tTime=%s' % time.ctime(t))
	