from scapy.all import *


def print_pkt(pkt):
	pkt.show()

sniff(filter='tcp and host 10.0.2.10 and port 80',prn=print_pkt)

