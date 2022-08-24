from scapy.all import *
import time

def listener():
    sniff(prn=print_packet, filter='udp and (port 67 or port 68_')

def print_packet(packet):
    # initialize variables to None at first
    target_mac, requested_ip, hostname, vendor_id = [None] * 4
    # get MAC address of the DHCP requester
    if packet.haslayer(Ether):
        target_mac = packet.getlayer(Ether).src
    # get DHCP options
    if packet.haslayer(DHCP):
        dhcp_options = packet[DHCP].options

        for item in dhcp_options:
            try:
                label, value = item
            except ValueError:
                continue
            if label == 'requested_addr':
                requested_ip = value
            elif label == 'hostname':
                hostname = value.decode()
            elif label == 'vendor_class_id':
                vendor_id = value.decode()
        if target_mac and vendor_id and hostname and requested_ip:
            # if all variables are NOT None, print device details
            time_now = time.strftime("[%Y-%m-%d - %H:%M:%S]")
            print(f"{time_now} : {target_mac} - {hostname} / {vendor_id} requested {requested_ip}")

if __name__ == "__main__":
    listener()