import os
import sys
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer


def open_file(self):
    filename = "home.html"
    file = open(filename, "r")
    for line in file:
        print(line),
        file.close()


class Server(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type:', 'text/html; charset=utf-8')
        self.end_headers()
        # self.wfile.write("Hello world!".encode())
        self.rfile.read(open_file)


def run(server_class=HTTPServer, handler_class=Server):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    run()
