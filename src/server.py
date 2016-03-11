# -*- coding: utf-8 -*-
"""Server module."""
from __future__ import unicode_literals
import socket
import email.utils

RESOURCES = {
    'images':

}



def resolve_uri(uri):
    """Return request body and file type."""
    file_path = uri.split('/')
    print(file_path)
    if file_path[0] != 'webroot':
        response_error(u'400 Bad Request')
        raise LookupError('File path not found.')
    else:
        file = file_path[-1].split('.')
        file_type = file[1]
        file_name = file[0]
        if file_type == 'png' or file_type == 'jpg':
            return



def parse_request(request):
    """Parse and validate request to confirm parts are correct."""
    lines = request.split('\r\n')
    if:
        lines[0][:3] == 'GET'
    else:
        raise RuntimeError('Only accepts GET requests.')
    if:
        lines[1][-8:] == 'HTTP/1.1'
    else:
        raise TypeError
    if:
        len(lines[1].split()) == 3 and lines[1][0] == '/'
        uri = lines[1].split()
        lines = resolve_uri(uri)
    else:
        raise SyntaxError
    return lines


def response_ok(uri):
    """Return 200 ok."""
    first = u'HTTP/1.1 200 OK'
    second_line = u'Content-Type: text/plain; charset=utf-8'
    date = u'Date: ' + email.utils.formatdate(usegmt=True)
    header_break = u''
    body = uri
    bytes_ = body.encode('utf-8')
    fourth_line = u'Content-Length: {}'.format(len(bytes_))
    string_list = [first, second_line, date, fourth_line, header_break, body]
    string_list = '\r\n'.join(string_list)
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
                try:
                    conn.sendall(response_ok(parse_request(full_string)).encode('utf-8'))
                except:
                    pass
                # server.listen(1)
                conn, addr = server.accept()
            except:
                response_error()
                raise
    except KeyboardInterrupt:
        conn.close()
    finally:
        server.close()

if __name__ == '__main__':
    server()


"""u'405 Method Not Allowed'
u'505 HTTP Version Not Supported'
u'404 Page Not Found'"""


