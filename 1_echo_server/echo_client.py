# Echo client program
import socket

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket()
s.connect((HOST, PORT))
msg = 'Are you the echo server?'
s.sendall(msg.encode())
print("Sent: " + msg)
data = s.recv(1024)
s.close()
print('Received: ' + data.decode())
