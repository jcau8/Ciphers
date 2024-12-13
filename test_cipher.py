import TRC
import pytest
import logging

TRC.logLevel = logging.DEBUG

@pytest.fixture
def message():
    '''Returns a message to encode'''
    msg = "This is a message for testing !#$|~"
    return msg

@pytest.mark.parametrize("key", [x for x in range(1,4)])
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
