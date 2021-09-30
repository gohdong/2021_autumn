from scapy.all import *

ip = IP(src="192.168.0.1",dst="8.8.8.8")
icmp = ICMP()
pkt = ip/icmp
pkt.show()
send(pkt,verbose=0)