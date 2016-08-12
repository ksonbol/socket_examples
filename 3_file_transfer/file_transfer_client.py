# file_transfer_client.py

import socket               # Import socket module

s = socket.socket()         # Create a socket object
HOST = socket.gethostname() # Get local machine name
PORT = 6001                 # Reserve a port for your service.
BUFFER_SIZE = 1024

s.connect((HOST, PORT))
with open('received.txt', 'wb') as f:
    count = 0
    print('waiting for server..')
    while True:
        data = s.recv(BUFFER_SIZE)
        if count == 0:
            print('downloading file..')
        if data == b'#FINISHED':
            print('Total size: {}\n'.format(count*BUFFER_SIZE))
            break
        f.write(data)
        count += 1
        if count % 100 == 0:
            print('Bytes Received: {}\n'.format(count*BUFFER_SIZE))

print('File downloaded successfully.')

s.close()                  # Close the socket when done
print('Connection closed')
