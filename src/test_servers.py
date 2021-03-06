# -*- coding: utf-8 -*-
"""Test client module."""
import pytest


def test_resolve_uri_nonexistant_file():
    """Assert function returns the correct body."""
    from server import resolve_uri
    path = resolve_uri('/WTF.txt')
    result = False
    assert path == result


def test_resolve_uri_nonexistant_dir():
    """Assert function returns the correct body."""
    from server import resolve_uri
    path = resolve_uri('/WTF')
    result = False
    assert path == result


def test_resolve_uri_images():
    """Test image files are present."""
    from server import resolve_uri
    our_tuple = resolve_uri('/images/Sample_Scene_Balls.jpg')
    assert our_tuple[1] == 'jpg'


def test_resolve_uri_files():
    """Test image files are present."""
    from server import resolve_uri
    our_tuple = resolve_uri('/sample.txt')
    assert our_tuple[1] == 'txt'


def test_resolve_uri_dir():
    """Test image files are present."""
    from server import resolve_uri
    our_tuple = resolve_uri('/images')
    assert our_tuple[1] == 'text/html'


@pytest.fixture(scope="function")
def response_ok():
    """Return 200 ok."""
    first = u'HTTP/1.1 200 OK'
    second_line = u'Content-Type: text/plain; charset=utf-8'
    header_break = u''
    body = u'/'
    bytes_ = body.encode('utf-8')
    fourth_line = u'Content-Length: {}'.format(len(bytes_))
    string_list = [first, second_line, fourth_line, header_break, body]
    string_list = '\r\n'.join(string_list)
    return string_list


def test_response_ok_status(response_ok):
    """Test for lead line in HTTP response."""
    output_ = 'HTTP/1.1 200 OK'
    response_ok = response_ok.split('\r\n')
    assert response_ok[0] == output_


def test_response_ok_content_type(response_ok):
    """Test for Content-Type in HTTP response header."""
    output_ = 'Content-Type: text/plain; charset=utf-8'
    response_ok = response_ok.split('\r\n')
    assert response_ok[1] == output_


def test_response_ok_header_break(response_ok):
    """Test for break between header and body in HTTP response header."""
    output_ = ''
    response_ok = response_ok.split('\r\n')
    assert response_ok[3] == output_


def test_response_error():
    """Test first line of server faliure response message."""
    from server import response_error
    output_ = 'HTTP/1.1 500 Internal Server Error'
    http_list = response_error().split('\r\n')
    assert http_list[0] == output_


def test_parse_method():
    """Assert for correct request method."""
    from server import parse_request
    request = 'PUT / HTTP/1.1'
    with pytest.raises(NameError):
        parse_request(request)


def test_parse_protocol():
    """Assert for correct request protol."""
    from server import parse_request
    request = 'GET / HTTP/2.1'
    with pytest.raises(TypeError):
        parse_request(request)


def test_parse_uri():
    """Assert for correct request uri."""
    from server import parse_request
    request = 'GET HTTP/1.1'
    with pytest.raises(SyntaxError):
        print(parse_request(request))


def test_parse():
    """Assert 404 error works correctly."""
    from server import response_error
    request = u'404 Page Not Found'
    response = response_error(request)
    response = response.split()
    assert response[1] == '404'
