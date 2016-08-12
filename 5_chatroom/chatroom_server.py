import socket, selectors, copy

def broadcast_data (sock, message):
    connections = sel.get_map()
    c = copy.copy(connections)
    for value in c.values():
        conn = value.fileobj
        # do not send message to sender or server socket
        if value.data == accept or conn == sock:
            continue
        try:
            conn.send(message.encode())
        except:
            # broken socket connection, chat client pressed ctrl+c for example
            sel.unregister(conn)
            conn.close()
            broadcast_data(conn, "Client (%s, %s) has leaved the room" % addr)

def accept(sock):
    conn, addr = sock.accept()  # Should be ready
    print("Client (%s, %s) connected" % addr)
    broadcast_data(sock, "[%s:%s] entered room\n" % addr)
    # conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn):
    data = conn.recv(RECV_BUFFER)  # Should be ready
    if data:
        msg = "\n<{}> {}".format(conn.getpeername(), data.decode())
        broadcast_data(conn, msg)
    else:
        print("Client (%s, %s) is offline" % conn.getpeername())
        print('closing', conn.getpeername())
        broadcast_data(conn, "Client (%s, %s) has leaved the room" % conn.getpeername())
        sel.unregister(conn)
        conn.close()

if __name__ == "__main__":

    RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
    PORT = 5000

    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", PORT))
    server_socket.listen(10)

    sel = selectors.DefaultSelector()
    sel.register(server_socket, selectors.EVENT_READ, accept)

    print("Chat server started on port " + str(PORT))

    while True:
        events = sel.select()
        for key, mask in events:
            sock = key.fileobj
            callback = key.data
            callback(sock)
