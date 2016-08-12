import socket, time, os, math
from threading import Thread

TCP_IP = 'localhost'
TCP_PORT = 9002
BUFFER_SIZE = 1024

class ClientThread(Thread):

    def __init__(self,ip,port,sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print("New thread started for "+ ip + ":" + str(port))

    def run(self):
        filename='file.txt'
        filesize = os.path.getsize(filename)
        f = open(filename,'rb')
        count = 0
        print('Sending file size..')
        self.sock.send(str(filesize).encode())
        ack = self.sock.recv(1024) # wait for acknowledgement since send is non-blocking
        if not ack: raise Exception("File Size not received")
        print('Uploading file:')
        while True:
            l = f.read(BUFFER_SIZE)
            if not l:
                print("Uploaded 100%")
                print('Total size: {}'.format(count*BUFFER_SIZE))
                f.close()
                self.sock.close()
                break

            self.sock.send(l)
            count += 1
            if count % 1000 == 0:
                progress = math.ceil(100 * count * BUFFER_SIZE / filesize)
                print("Uploaded {}% to {}".format(progress, self.port))
                time.sleep(0.1) # for presentation purposes only

tcpsock = socket.socket()
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
tcpsock.listen(5)

while True:
    print("Waiting for incoming connections...")
    (conn, (ip,port)) = tcpsock.accept()
    print('Got connection from ', (ip,port))
    newthread = ClientThread(ip,port,conn)
    newthread.start()
