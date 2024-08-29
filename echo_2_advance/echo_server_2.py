import socket

HOST = "127.0.0.1"  # Использовать все адреса: виден и снаружи, и изнутри
PORT = 50432  # Порт для прослушивания (непривилегированные порты > 1023)


def handle_client(sock, addr):
    """Обрабатывает подключение клиента.
    :param sock: Объект сокета для связи с клиентом.
    :param addr: Адрес клиента."""
    print(f"Подключение по {addr}")
    with sock:
        while True:
            try:
                data = sock.recv(1024)
                if not data:  # Если клиент отключился
                    print(f"Клиент {addr} отключился.")
                    break

                message = data.decode('utf-8')
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
    """Основная функция, которая запускает сервер и ожидает подключения клиента.
    Обрабатывает только одно подключение за раз.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serv_sock:
        serv_sock.bind((HOST, PORT))
        serv_sock.listen()
        print("Сервер запущен, ожидаю подключения...")

        # Ожидание только одного клиента
        sock, addr = serv_sock.accept()
        handle_client(sock, addr)


if __name__ == "__main__":
    main()
