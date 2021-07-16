import socket

def init_server():
    print("Starting Server...")
    sock = socket.socket()
    sock.bind(('', 9090))
    sock.listen(1)
    print("Wait for connect...")

    conn, addr = sock.accept()

    while True:
        data = conn.recv(1024) 
        print("Клиент прислал: " + data.decode())
        if not data:
            break
        conn.send(data.upper())

    conn.close()