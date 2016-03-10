# -*- coding: utf-8 -*-
"""Server module."""
from __future__ import unicode_literals
import socket
import email.utils


def parse_request(request):
    """Parse and validate request to confirm parts are correct."""
    lines = requet.split('\r\n')
    if lines[1][:3] == 'GET':
        pass
    else:
        raise RuntimeError('Only accepts GET requests.')
    if lines[1][-8:] == 'HTTP/1.1':
        pass
    else:
        raise RuntimeError('Only accepts HTTP/1.1 protocol requests.')
    if len(lines[1].split()) == 3 and lines[1][0] == '/':
        pass
    else:
        raise RuntimeError('URI not properly formatted.')
    return lines[1]


def response_ok():
    """Return 200 ok."""
    first_line = u'HTTP/1.1 200 OK'
    second_line = u'Content-Type: text/plain; charset=utf-8'
    date_line = u'Date: ' + email.utils.formatdate(usegmt=True)
    header_break = u''
    body = u'It is all good'
    bytes = body.encode('utf-8')
    fourth_line = u'Content-Length: {}'.format(len(bytes))
    string_list = [first_line, second_line, date_line, fourth_line, header_break, body]
    string_list = '\r\n'.join(string_list)
    return string_list


def response_error():
    """Return 500 internal server error."""
    first_line = u'HTTP/1.1 500 Internal Server Error'
    second_line = u'Content-Type: text/plain; charset=utf-8'
    date_line = email.utils.formatdate(usegmt=True)
    header_break = u''
    body = u'The system is down'
    bytes = body.encode('utf-8')
    fourth_line = u'Content-Length: {}'.format(len(bytes))
    string_list = [first_line, second_line, date_line, fourth_line, header_break, body]
    string_list = '\r\n'.join(string_list)
    return string_list


def server():
    """Return message to client."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    address = ('127.0.0.1', 5001)
    server.bind(address)
    server.listen(1)
    conn, addr = server.accept()
    try:
        while True:
            try:
                buffer_length = 8
                reply_complete = False
                full_string = u""
                while not reply_complete:
                    part = conn.recv(buffer_length)
                    full_string = full_string + part.decode('utf-8')
                    if len(part) < buffer_length:
                        reply_complete = True
                print(full_string)
                # parse_request(full_string)
                conn.sendall(response_ok().encode('utf-8'))
                server.listen(1)
                conn, addr = server.accept()
            except:
                response_error()
                raise
    except KeyboardInterrupt:
        conn.close()
        server.close()

if __name__ == '__main__':
    server()





