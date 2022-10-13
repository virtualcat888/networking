import nmap3
import re


# re pattern to recognise IPv4 addresses.
ip_addr_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")

# re pattern to specify number of ports to scan from lowest to highest port number
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")

port_min = 0
port_max = 65535
open_ports = []

while True:
    user_input_ip_addr = input("\nPlease enter the ip address you wan to scan: ")
    if ip_addr_pattern.search(user_input_ip_addr):
        print(f"{user_input_ip_addr} is a valid ip address")
        break

"""
while True:
    port_range = input("Please enter the range of ports you want to scan ie. 20-22: ")
    check_port_range = port_range_pattern.search(port_range.replace(" ",""))
    if check_port_range:
        port_min = int(check_port_range.group(1))
        port_max = int(check_port_range.group(2))
        break
"""

nmap = nmap3.Nmap()

results = nmap.scan_top_ports(user_input_ip_addr)
port_results = results[user_input_ip_addr]["ports"]
for item in port_results:
    print(item["portid"], item["state"])
    if item["portid"] == "80":
        print("http is open")

"""
for port in range(port_min, port_max + 1):
    try:
        result = nm.scan(user_input_ip_addr, str(port))
        port_status = (result['scan'][user_input_ip_addr]['tcp'][port]['state'])
        print(f"Port {port} is {port_status}")
    except:
        print(f"Cannot scan port {port}.")
"""