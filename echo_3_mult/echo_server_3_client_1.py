import socket

HOST = "127.0.0.1"
PORT = 50432


def main():
    """Основная функция клиента, которая подключается к серверу и отправляет сообщения.
    Клиент может дистанционно отключить сервер, отправив специальную команду."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
        try:
            client_sock.connect((HOST, PORT))
            print("Подключено к серверу.")

            while True:
                message = input("Введите сообщение (или 'exit' для отключения сервера): ")
                if message.strip().lower() == "exit":
                    print("Отправка команды отключения серверу...")
                    client_sock.sendall("exit".encode('utf-8'))
                    print("Ожидание подтверждения отключения...")
                    data = client_sock.recv(1024)
                    if data.decode('utf-8').strip().lower() == "server disconnected":
                        print("Сервер успешно отключен.")
                    else:
                        print("Не удалось отключить сервер.")
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
