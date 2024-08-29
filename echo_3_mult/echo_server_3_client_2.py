import socket

HOST = "127.0.0.1"
PORT = 50432


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
        try:
            client_sock.connect((HOST, PORT))
            print("Подключено к серверу.")

            while True:
                message = input("Введите сообщение (или 'exit' для отключения): ")
                if message.strip().lower() == "exit":
                    print("Отключение от сервера...")
                    break

                if message:  # Проверка на пустое сообщение
                    client_sock.sendall(message.encode('utf-8'))
                    try:
                        data = client_sock.recv(1024)
                        print(f"Получено от сервера: {data.decode('utf-8')}")
                    except ConnectionResetError:
                        print("Сервер отключён. Завершение работы клиента.")
                        break
                else:
                    print("Сообщение не может быть пустым. Пожалуйста, введите текст.")

        except ConnectionRefusedError:
            print("Не удалось подключиться к серверу.")
        except Exception as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()