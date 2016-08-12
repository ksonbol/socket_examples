import socket, math

TCP_IP = 'localhost'
TCP_PORT = 9002
BUFFER_SIZE = 1024

s = socket.socket()
s.connect((TCP_IP, TCP_PORT))

with open('received.txt', 'wb') as f:
    count = 0
    print('waiting for server..')
    filesize = s.recv(BUFFER_SIZE)
    print("Received File Size..")
    s.send(b"File Size Received!")
    print("Acknowledgement Sent..")
    filesize = int(filesize)
    while True:
        data = s.recv(BUFFER_SIZE)
        if not data:
            print("Downloaded 100%")
            print('Total size: {}'.format(count*BUFFER_SIZE))
            f.close()
            break
        f.write(data)
        count += 1
        if count % 1000 == 0:
            progress = math.ceil(100 * count * BUFFER_SIZE / filesize)
            print("Downloaded {}%".format(progress))

s.close()
print('connection closed')
