from scapy.all import *

print("Sending Spoofed ICMP Packet......")
ip = IP(src="192.168.19.1",dst ="8.8.8.8")
icmp = ICMP()
pkt = ip/icmp
pkt.show()
send(pkt,verbose=0)
