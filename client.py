import socket

def client():
    sock = socket.socket()


    try:
        sock.connect(('localhost', 9090))
    except ConnectionRefusedError:
        print("Сервер не запущен. Мы не можем подключиться")
    else:
        send = input("send: ")
        sock.send(send.encode())

        data = sock.recv(1024)
        sock.close()

        print(data)

        

