from scapy.all import *

def print_pkt(pkt):
	pkt.show()

sniff(filter='tcp',prn=print_pkt)

