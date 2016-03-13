# -*- coding: utf-8 -*-
"""Gevent implemnation of http server."""
from server import response_error
from server import response_ok
from server import resolve_uri
from server import parse_request


def server(conn, address):
    """Return message to client."""
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
        conn.close()


if __name__ == '__main__':
    from gevent.server import StreamServer
    from gevent.monkey import patch_all
    patch_all()
    server = StreamServer(('127.0.0.1', 10000), server)
    print('Starting echo server on 1000')
    server.serve_forever()
