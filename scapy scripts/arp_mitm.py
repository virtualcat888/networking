from scapy.all import *
import os
import sys
import re


def get_gateway(gateway_ip):
    result = subprocess.run(["route", "-n"], capture_output=True).stdout.decode().split("\n")
    for row in result:
        new_row = re.split(' +', row)
        if gateway_ip in row:
            return True
    return False

def get_interface_name():
    """The interface names of a networks are listed in the /sys/class/net folder in Kali. 
    This function returns a list of interfaces in Kali."""
    os.chdir("/sys/class/net")
    interface_names = os.listdir()
    return interface_names