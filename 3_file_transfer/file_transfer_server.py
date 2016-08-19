# file_transfer_server.py

import socket, time

HOST = socket.gethostname()
PORT = 6000
BUFFER_SIZE = 4096

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)

print('Server listening..')

while True:
    conn, addr = s.accept()
    print('New Connection from {}'.format(addr))
    with open('file.txt', 'rb') as f:
        print('Sending File..')
        sent = 0
        count = 0
        # for python >= 3.5, use conn.sendfile(f) instead of the loop
        while True:
            l = f.read(BUFFER_SIZE)
            if not l:
                print()
                print('Total size: {} bytes\n'.format(sent))
                break
            conn.sendall(l)
            sent += len(l)
            count += 1
            if count % 1000 == 0:
                print(".", end="", flush=True)


    print('Finished Sending.')

    conn.close()
    print('Connection closed')
