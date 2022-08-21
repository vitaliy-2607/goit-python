import socket


def client():
    host = socket.gethostname()
    port = 8000

    client_socket = socket.socket()
    client_socket.connect((host, port))
    message = input('Повідомлення: ')

    while message.lower().strip() != 'end':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print(f'received message: {data}')
        message = input('Повідомлення: ')

    client_socket.close()


if __name__ == '__main__':
    client()
