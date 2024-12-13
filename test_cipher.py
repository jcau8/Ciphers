import TRC
import pytest
import logging

TRC.logLevel = logging.DEBUG

@pytest.fixture
def message():
    '''Returns a message to encode'''
    msg = "This is a message for testing !#$|~"
    return msg

@pytest.mark.parametrize("key", [x for x in range(1,8)])
@pytest.mark.parametrize("alphabeticKey", ["0","0123"])
@pytest.mark.parametrize("spaceEncrypt", ["0","1"])
def test_caesar(message, key, alphabeticKey, spaceEncrypt):
    """Test the caesar function"""

    alphabet = TRC.returnAlphabet(alphabeticKey, spaceEncrypt)
    mode = 0
    encoded = TRC.caesar(mode, message, key, alphabet)
    mode = 1
    decoded = TRC.caesar(mode, encoded, key, alphabet)
    assert message == decoded

@pytest.mark.parametrize("key", [x for x in range(1,9)])
@pytest.mark.parametrize("alphabeticKey", ["0","0123"])
@pytest.mark.parametrize("spaceEncrypt", ["0","1"])
def test_transposition(message, key, alphabeticKey, spaceEncrypt):
    """Test the caesar function"""

    alphabet = TRC.returnAlphabet(alphabeticKey, spaceEncrypt)
    mode = 0
    encoded = TRC.transposition(mode, message, key)
    mode = 1
    decoded = TRC.transposition(mode, encoded, key)
    assert message == decoded

@pytest.mark.parametrize("key", [x for x in range(1,9)])
@pytest.mark.parametrize("alphabeticKey", ["0","0123"])
@pytest.mark.parametrize("spaceEncrypt", ["0","1"])
def test_transcode(message, key, alphabeticKey, spaceEncrypt):
    """Test the translate function"""

    alphabet = TRC.returnAlphabet(alphabeticKey, spaceEncrypt)

    mode = 0
    encoded = TRC.translate(key, mode, message, alphabet)
    mode = 1
    decoded = TRC.translate(key, mode, encoded, alphabet)
    assert message == decoded

