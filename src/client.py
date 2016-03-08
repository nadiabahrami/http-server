# -*- coding:utf-8 -*-
""""""
import socket
import sys

def client_send(message):
    info = socket.getaddrinfo('127.0.0.1', 5000)
    stream_info = [i for it in info if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])
    client.sendall(message.encode('utf-8'))

def client_receive(message):
    buffer_length = 8
    reply_complete = False
    full_string = ""
    while not reply_complete:
        part = client.recv(buffer_length)
        fullstring += part.decode('utf8')
        if len(part) < buffer_length:  #add a time out or a zero byte push
            break
    return full_string

if __name__ == '__main__':