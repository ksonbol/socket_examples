# file_transfer_client.py

import socket, sys          # Import socket module

s = socket.socket()         # Create a socket object
HOST = socket.gethostname() # Get local machine name
PORT = 6000                 # Reserve a port for your service.
BUFFER_SIZE = 4096

s.connect((HOST, PORT))

with open('received.txt', 'wb') as f:
    received = 0
    count = 0
    print('waiting for server..')
    while True:
        data = s.recv(BUFFER_SIZE)
        if received == 0:
            print('downloading file..')
        if not data:
            print()
            print('Total size: {} bytes\n'.format(received))
            break
        f.write(data)
        received += len(data)
        count += 1
        if count % 1000 == 0:
            print(".", end="", flush=True)

print('File downloaded successfully.')

s.close()                  # Close the socket when done
print('Connection closed')
