# -*- coding:utf-8 -*-
""""""
import socket
import sys

def client_send(message):
    info = socket.getaddrinfo('127.0.0.1', 5000)
    stream_info = [i for i in info if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])
    client.sendall(message.encode('utf8'))

    buffer_length = 8
    reply_complete = False
    full_string = ""
    while not reply_complete:
        part = client.recv(buffer_length)
        full_string = full_string + part.decode('utf8')
        if len(part) < buffer_length:  #add a time out or a zero byte push
            reply_complete = True
    print(full_string)


# def client(message):
#     client_send(message):
#     print(client_receive())#is there an internal parameter?


if __name__ == '__main__':
    message = sys.argv[1]
    client_send(message)
