import socket
from concurrent import futures

def send_message(conn):
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f'Отримано повідомлення: {data}')
        message = input('Повідомлення: ')
        conn.send(message.encode())
    print('Okey!')
    conn.close()


def main():
    host = socket.gethostname()
    port = 8000

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(20)
    with futures.ThreadPoolExecutor(10) as pool:
        while True:
            conn, address = server_socket.accept()
            pool.submit(send_message, conn)
            print(f'Зєднання з {address}')


if __name__ == '__main__':
    main()
