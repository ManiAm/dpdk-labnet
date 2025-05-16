from scapy.all import sendp, Ether, IP, UDP

# Create the packet
eth_layer = Ether(dst="ff:ff:ff:ff:ff:ff")
ip_layer = IP(dst="255.255.255.255")
udp_layer = UDP(dport=999, sport=666)
payload = "Hello World!"

packet = eth_layer / ip_layer / udp_layer / payload

# Send the packet
sendp(packet, iface="enp0s9")
