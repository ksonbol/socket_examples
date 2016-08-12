# Packet sniffer in Python for Linux, sniffs only incoming TCP packets
# Run this file with root privileges, e.g. sudo python3 sniffer.py

import socket

#create an INET, raw socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

# receive a packet
while True:
  print(s.recvfrom(65565))
