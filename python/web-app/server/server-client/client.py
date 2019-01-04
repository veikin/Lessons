#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Импортируется модуль
import socket

# Создается сокет
sock = socket.socket()
# Связывется сокет с адресом и портом
sock.connect(('localhost', 9090))
# После подключения клиент отправляет сообщение
sock.send('hello server!')
# Количество байт для чтения
data = sock.recv(1024)
# Закрыть соединение
sock.close()

print(data)
