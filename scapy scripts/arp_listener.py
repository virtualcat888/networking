from scapy.all import *
import time

def dhcp_listener():
    sniff(prn=print_packet, filter="arp")

def print_packet(packet):
    source_ip = packet[ARP].psrc
    source_mac = packet[ARP].hwsrc
    dest_ip = packet[ARP].pdst
    dest_mac = packet[ARP].hwdst

    if packet[ARP].op == 1:
            print("this client sent a ARP request: " + source_ip + " || MAC: " + source_mac + \
                " to find out who is: " + dest_ip)
    elif packet[ARP].op == 2:
            print("this client: " + dest_ip + " || MAC: " + dest_mac + " now knows client: " + source_ip + \
                " || MAC: " + source_mac)

if __name__ == "__main__":
    dhcp_listener()