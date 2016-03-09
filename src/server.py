# -​*- coding: utf-8 -*​-
"""Server module."""
from __future__ import unicode_literals
import socket


def server():
    """Return message to client."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5000)
    server.bind(address)
    server.listen(1)
    conn, addr = server.accept()
    try:
        while True:
            buffer_length = 8
            reply_complete = False
            full_string = ""
            while not reply_complete:
                part = conn.recv(buffer_length)
                full_string = full_string + part.decode('utf-8')
                if len(part) < buffer_length:  
                    reply_complete = True
            print(full_string)
            conn.sendall(full_string.encode('utf-8'))
            server.listen(1)
            conn, addr = server.accept()
    except KeyboardInterrupt:
        conn.close()
        server.close()

server()
