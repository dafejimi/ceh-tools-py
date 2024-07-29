import ntplib
from time import ctime

def _print_time():
	ntp_client = ntplib.NTPClient()
	response = ntp_client.request('pool.ntp.org')
	print('ctime(response.tx_time)')
	
	print_time()