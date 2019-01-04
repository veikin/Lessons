import socket


def Main():
    host = '127.0.0.1'
    port = 9090
    s = socket.socket()     # Создается сокет
    s.connect((host, port))     # Связывется сокет с адресом и портом
    massage = input("-> ")
    while massage != 'q':
        s.send(massage.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')     # Количество байт для чтения
        print("Recieved from server: " + data)
        massage = input("-> ")
    s.close()   # Закрыть соединение


if __name__ == '__main__':
    Main()
