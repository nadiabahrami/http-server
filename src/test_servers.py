# -*- coding: utf-8 -*-
"""Test client module."""


def test_response_ok_status():
    """Test for lead line in HTTP response."""
    from server import response_ok
    output_ = 'HTTP/1.1 200 OK'
    http_list = response_ok().split('\r\n')
    assert http_list[0] == output_


def test_response_ok_content_type():
    """Test for Content-Type in HTTP response header."""
    from server import response_ok
    output_ = 'Content-Type: text/plain; charset=utf-8'
    http_list = response_ok().split('\r\n')
    assert http_list[1] == output_


def test_response_ok_header_break():
    """Test for break between header and body in HTTP response header."""
    from server import response_ok
    output_ = ''
    http_list = response_ok().split('\r\n')
    assert http_list[4] == output_


def test_response_error():
    """Test first line of server faliure response message."""
    from server import response_error
    output_ = 'HTTP/1.1 500 Internal Server Error'
    http_list = response_error().split('\r\n')
    assert http_list[0] == output_
