#!/usr/bin/python3

import socket


def Main():
    host = '127.0.0.1'
    port = 9090
    s = socket.socket()     # Создается сокет
    s.bind((host, port))    # Сокет связывается с адресом хоста и портом
    s.listen(1)     # Включается режим прослушивания. очередь подключений
    c, addr = s.accept()     # Принимается подключение
    print('Connected from: ' + str(addr))   # Сообщение после поключения

    while True:
        data = c.recv(1024).decode('utf-8')  # получение данных по 1кб
        if not data:
            break
        print("From connected user: " + data)
        data = data.upper()
        print("Sending: " + data)
        c.send(data.encode('utf-8'))
    c.close()


if __name__ == '__main__':
    Main()
