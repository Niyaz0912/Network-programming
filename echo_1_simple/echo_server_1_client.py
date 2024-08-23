import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)
    """По сравнению с сервером клиент довольно прост. В нём создаётся объект сокета. 
    Для подключения к серверу используется .connect(), 
    и для отправки сообщения вызывается s.sendall(), s.recv() считывает ответ, а затем этот ответ выводится."""

print(f"Received {data!r}")