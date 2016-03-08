# -*- coding: utf-8 -*-
"""Test client module."""
from __future__ import unicode_literals
import pytest


def test_client():
    """Assert sent message and recieved message are the same."""
    from client import client
    message = 'Hey this works.'
    message2 = 'one'
    message3 = 'Hey this is a really long message and it will be sent totally. Yeah.'
    message4 = 'abcdefgh'
    message5 = 'ç'
    message6 = 'one\n'
    assert client(message) == message
    assert client(message2) == message2
    assert client(message3) == message3
    assert client(message4) == message4
    assert client(message5) == message5
    assert client(message6) == message6
