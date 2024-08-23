import socket

HOST = "127.0.0.1"
PORT = 50131

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    while True:
        data = input("Напечатайте сообщение для отправки: ")
        data_bytes = data.encode()
        sock.sendall(data_bytes)
        data_bytes = sock.recv(1024)
        data = data_bytes.decode()
        print("Received:", data)