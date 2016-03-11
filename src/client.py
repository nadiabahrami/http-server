# -*- coding: utf-8 -*-
"""Client module."""
from __future__ import unicode_literals
import socket
import sys


def client(message):
    """Return message to console after server echo."""
    info = socket.getaddrinfo('127.0.0.1', 5001)
    stream_info = [i for i in info if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])
    client.sendall(message.encode('utf-8'))
    client.shutdown(1)
    buffer_length = 8
    reply_complete = False
    full_string = ""
    while not reply_complete:
        part = client.recv(buffer_length)
        full_string = full_string + part.decode('utf-8')
        if len(part) < buffer_length:
            reply_complete = True
            client.close()
    print(full_string)
    return full_string


def client_request_header():
    """Return client request header."""
    first = u'GET / HTTP/1.1'
    return first


if __name__ == '__main__':
    message = sys.argv[1]
    client(message)
