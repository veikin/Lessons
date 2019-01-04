#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Импортируется модуль
import socket

# Создается сокет
sock = socket.socket()
# Сокет связывается с адресом хоста и портом с момощью bind
sock.bind(('', 9090))
# Включается режим прослушивания. Аргумент - очередь подключений
sock.listen(1)
# Принимается подключение, возвращает кортеж с новым сокетом и адресом клиента
conn, addr = sock.accept()

# Сообщение после поключения
print('conneted', addr)

while True:
    # получение данных по 1кб
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data.upper())
