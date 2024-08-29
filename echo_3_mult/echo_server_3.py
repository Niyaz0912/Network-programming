import socket
import threading

HOST = "127.0.0.1"  # Использовать все адреса: виден и снаружи, и изнутри
PORT = 50432  # Port to listen on (non-privileged ports are > 1023


def handle_client(sock, addr):
    print(f"Подключение по {addr}")
    with sock:
        while True:
            try:
                data = sock.recv(1024)
                if not data:  # Если клиент отключился
                    print(f"Клиент {addr} отключился.")
                    break

                message = data.decode('utf-8')
                if message.strip().lower() == "exit":
                    print(f"Клиент {addr} запросил отключение.")
                    break

                print(f"Получено: {message}, от: {addr}")
                response = message.upper()
                sock.sendall(response.encode('utf-8'))
            except ConnectionError:
                print(f"Клиент {addr} внезапно отключился.")
                break
            except Exception as e:
                print(f"Ошибка: {e}")
                break
    print("Отключение по", addr)


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serv_sock:
        serv_sock.bind((HOST, PORT))
        serv_sock.listen()
        print("Сервер запущен, ожидаю подключения...")

        while True:
            sock, addr = serv_sock.accept()
            client_thread = threading.Thread(target=handle_client, args=(sock, addr))
            client_thread.start()


if __name__ == "__main__":
    main()
