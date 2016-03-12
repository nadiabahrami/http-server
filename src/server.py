# -*- coding: utf-8 -*-
"""Server module."""
from __future__ import unicode_literals
import socket
import email.utils
import os
import io


def resolve_uri(uri):
    """Return request body and file type."""
    root = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'webroot')
    full_path = os.path.join(root, uri[1:])
    path_list = uri.split('/')
    path_list = [item for item in path_list if item]
    if path_list == []:
        return html_compiler(full_path)
    file_type = path_list[-1].split('.')
    try:
        if len(file_type) == 1:
            return html_compiler(full_path, uri)
        file = io.open(full_path, 'rb')
        body_content = file.read()
        file_type = file_type[-1]
        return (body_content, file_type)
    except (IOError, OSError):
        print('I am here fuck')
        return False


def html_compiler(full_path, uri=''):
    """Return a byte encoded html file."""
    file_type = u'text/html'
    list_ = os.listdir(full_path)
    html = u'<ul>'
    for file in list_:
        html += '<li><a href="{}/{}">{}</a></li>'.format(uri, file, file)
    html += '</ul>'
    return (html.encode('utf-8'), file_type)


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


def response_ok(body_tuple):
    """Return 200 ok."""
    first = u'HTTP/1.1 200 OK'
    second_line = u'Content-Type:' + body_tuple[1] + '; charset=utf-8'
    date = u'Date: ' + email.utils.formatdate(usegmt=True)
    header_break = u''
    body = body_tuple[0]
    fourth_line = u'Content-Length: {}'.format(len(body))
    string_list = [first, second_line, date, fourth_line, header_break]
    string_list = '\r\n'.join(string_list) + '\r\n'
    string_list = string_list.encode('utf-8') + body
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
                    body_tuple = resolve_uri(uri)
                    if body_tuple:
                        conn.send(response_ok(body_tuple))
                    else:
                        conn.sendall(response_error(u'404 Page Not Found'))
                    conn.close()
                except NameError('Method not GET'):
                    conn.sendall(response_error(u'405 Method Not Allowed'))
                    conn.close()
                except TypeError('HTTP protol incorrect'):
                    conn.sendall(response_error(u'505 HTTP Version Not Supported'))
                    conn.close()
                except SyntaxError('URI incorrect'):
                    conn.sendall(response_error(u'404 Page Not Found'))
                    conn.close()
                except IOError('File not found'):
                    conn.sendall(response_error(u'404 Page Not Found'))
                    conn.close()
            except SystemError('Request not fully received'):
                conn.sendall(response_error())
                conn.close()
    except KeyboardInterrupt:
        conn.close()
    finally:
        server.close()

if __name__ == '__main__':
    server()
