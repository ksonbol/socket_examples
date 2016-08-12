import socket, selectors, string, sys

def prompt() :
    sys.stdout.write('<You> ')
    sys.stdout.flush()

if __name__ == "__main__":

    if(len(sys.argv) < 3) :
        print('Usage : python chatroom_client.py hostname port')
        sys.exit()

    RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2

    host = sys.argv[1]
    port = int(sys.argv[2])

    s = socket.socket()

    # connect to remote host
    try :
        s.connect((host, port))
    except :
        print('Unable to connect')
        sys.exit()

    print('Connected to remote host. Start sending messages')
    prompt()

    sel = selectors.DefaultSelector()
    sel.register(s, selectors.EVENT_READ, "in")
    sel.register(sys.stdin, selectors.EVENT_READ, "out")

    while True:
        events = sel.select()
        for key, mask in events:
            sock = key.fileobj
            if key.data == "in":
                #incoming message from remote server
                data = sock.recv(RECV_BUFFER)
                if data:
                    # print data
                    sys.stdout.write(data.decode())
                    prompt()
                else:
                    print('\nDisconnected from chat server')
                    sys.exit()

            else:
                #user entered a message
                msg = sys.stdin.readline()
                s.send(msg.encode())
                prompt()
