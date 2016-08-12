# file_transfer_server.py

import socket, time

HOST = socket.gethostname()
PORT = 6001
BUFFER_SIZE = 1024

s = socket.socket()
s.bind((HOST, PORT))
s.listen(5)

print('Server listening..')

while True:
    conn, addr = s.accept()
    print('New Connection from {}'.format(addr))
    with open('file.txt', 'rb') as f:
        print('Sending File..')
        count = 0
        # for python >= 3.5, use conn.sendfile(f) instead of the loop
        while True:
            l = f.read(BUFFER_SIZE)
            if not l:
                print('Total size: {}\n'.format(count*BUFFER_SIZE))
                conn.send(b'#FINISHED')
                break
            conn.send(l)
            count += 1
            if count % 1000 == 0:
                print('Bytes Sent: {}\n'.format(count*BUFFER_SIZE))
                # REMOVE THIS LINE IN REAL APPLICAIONS
                time.sleep(0.1) # for presentation purposes only

    print('Finished Sending.')

    conn.close()
    print('Connection closed')
