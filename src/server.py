# -*- coding: utf-8 -*-
"""Server module."""
from __future__ import unicode_literals
import socket
import email.utils
import os
import io


def resolve_uri(uri):
    """Return request body and file type."""
    root = os.getcwd() + '/webroot' + uri
    print('this is the uri' + uri)
    print(root)
    file_path = uri.split('/')
    file_path.remove('')
    print(file_path)
    if io.open(root, 'rb'):
        body_content = io.open(root, 'rb')
        body_content = body_content.read()
        file_type = file_path[-1].split('.')
        file_type = file_type[-1]
        return (body_content, file_type)
    else:
        raise IOError('File not found')


def parse_request(request):
    """Parse and validate request to confirm parts are correct."""
    lines = request.split('\r\n')
    words = lines[0].split()
    if lines[0][:3] == 'GET':
        pass
    else:
        raise NameError
    if lines[0][-8:] == 'HTTP/1.1':
        pass
    else:
        raise TypeError
    if len(words) == 3 and words[1][0] == '/':
        pass
    else:
        raise SyntaxError
    return words[1]


def response_ok(body_content):
    """Return 200 ok."""
    first = u'HTTP/1.1 200 OK'
    second_line = u'Content-Type: text/plain; charset=utf-8'
    date = u'Date: ' + email.utils.formatdate(usegmt=True)
    header_break = u''
    body = body_content[0]
    # bytes_ = body.encode('utf-8')
    fourth_line = u'Content-Length: {}'.format(len(body))
    string_list = [first, second_line, date, fourth_line, header_break]
    string_list = '\r\n'.join(string_list).encode('utf-8')
    string_list = string_list + body
    return string_list


def response_error(error='500 Internal Server Error'):
    """Return 500 internal server error."""
    first = u'HTTP/1.1 {}'.format(error)
    second_line = u'Content-Type: text/plain; charset=utf-8'
    date = email.utils.formatdate(usegmt=True)
    header_break = u''
    body = u'The system is down'
    bytes_ = body.encode('utf-8')
    fourth_line = u'Content-Length: {}'.format(len(bytes_))
    string_list = [first, second_line, date, fourth_line, header_break, body]
    string_list = '\r\n'.join(string_list)
    return string_list


def server():
    """Return message to client."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    address = ('127.0.0.1', 5001)
    server.bind(address)
    server.listen(1)
    try:
        while True:
            conn, addr = server.accept()
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
                try:
                    uri = parse_request(full_string)
                    print(uri)
                    body_content = resolve_uri(uri)
                    print(body_content)
                    conn.sendall(response_ok(body_content))
                except NameError('Method not GET'):
                    conn.sendall(response_error(u'405 Method Not Allowed'))
                except TypeError('HTTP protol incorrect'):
                    conn.sendall(response_error(u'505 HTTP Version Not Supported'))
                except SyntaxError('URI incorrect'):
                    conn.sendall(response_error(u'404 Page Not Found'))
                except IOError('File not found'):
                    conn.sendall(response_error(u'404 Page Not Found'))
            except SystemError('Request not fully received'):
                conn.sendall(response_error())
    except KeyboardInterrupt:
        conn.close()
    finally:
        server.close()

if __name__ == '__main__':
    server()
