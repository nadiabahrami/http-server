# -*- coding: utf-8 -*-
"""Test client module."""
from __future__ import unicode_literals


def test_client_message():
    """Assert sent message and recieved message are the same."""
    from client import client
    message = 'Hey this works.'
    assert client(message) == message


def test_client_less_than_8():
    """Assert sent message and recieved message are the same."""
    from client import client
    message2 = 'one'
    assert client(message2) == message2


def test_client_long():
    """Assert sent message and recieved message are the same."""
    from client import client
    message3 = 'Hey this is a really long message and it will be sent totally.'
    assert client(message3) == message3


def test_client_exact_buffer_length():
    """Assert sent message and recieved message are the same."""
    from client import client
    message4 = 'abcdefgh'
    assert client(message4) == message4


def test_client_non_ascii():
    """Assert sent message and recieved message are the same."""
    from client import client
    message5 = 'ç'
    assert client(message5) == message5


def test_client_newline():
    """Assert sent message and recieved message are the same."""
    from client import client
    message6 = 'one\n'
    assert client(message6) == message6   


def test_response_ok():
    """"""
    from server import response_ok
    pass


def test_response_error():
    """"""
    from server import response_error
    pass
