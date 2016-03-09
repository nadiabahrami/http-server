# -*- coding: utf-8 -*-
"""Server module."""
from __future__ import unicode_literals
import socket
import email.utils


def response_ok(body):
    """Return 200 ok."""
    first_line = 'HTTP/1.1 200 OK'
    second_line = 'Content-Type: text/plain; charset=utf-8'
    # date_line = 'Date: {}'.format(email.utils.formatdate(usegmt=True))
    header_break = '\r\n'
    bytes = body.encode('utf-8')
    fourth_line = 'Content-Length: {}'.format(len(bytes))
    body_message = 'Body: It is all good'
    string_list = [first_line, second_line, fourth_line, header_break, body_message]
    string_list = '\r\n'.join(string_list)
    return string_list


def response_error(body):
    """Return 500 internal server error."""
    first_line = 'HTTP/1.1 500 Internal Server Error'
    second_line = 'Content-Type: text/plain; charset=utf-8'
    # date_line = email.utils.formatdate(usegmt=True)
    header_break = '<CRLF>'
    bytes = body.encode('utf-8')
    fourth_line = 'Content-Length: {}'.format(len(bytes))
    body_message = 'Body: The system is down'
    string_list = [first_line, second_line, fourth_line, header_break, body_message]
    string_list = '\r\n'.join(string_list)
    return string_list


def server():
    """Return message to client."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5000)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(address)
    server.listen(1)
    conn, addr = server.accept()
    try:
        while True:
            buffer_length = 8
            reply_complete = False
            full_string = u""
            while not reply_complete:
                part = conn.recv(buffer_length)
                full_string = full_string + part.decode('utf-8')
                if len(part) < buffer_length:
                    reply_complete = True
            print(full_string)
            body = full_string
            print(response_ok(body))
            conn.sendall(response_ok(body).encode('utf-8'))
            server.listen(1)
            conn, addr = server.accept()
    except KeyboardInterrupt:
    	conn.close()
    	server.close()
server()




