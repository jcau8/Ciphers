import TRCH
import pytest
import logging

TRCH.logLevel = logging.DEBUG

@pytest.fixture
def message():
    '''Returns a message to encode'''
    msg = "This is a message for testing !#$|~"
    return msg

@pytest.mark.skip
@pytest.mark.parametrize("key", [x for x in range(1,23)])
@pytest.mark.parametrize("alphabeticKey", ["0","0123"])
@pytest.mark.parametrize("spaceEncrypt", ["0","1"])
def test_caesar(message, key, alphabeticKey, spaceEncrypt):
    """Test the caesar function"""

    alphabet = TRCH.returnAlphabet(alphabeticKey, spaceEncrypt)
    mode = 0
    encoded = TRCH.caesar(mode, message, key, alphabet)
    mode = 1
    decoded = TRCH.caesar(mode, encoded, key, alphabet)
    assert message == decoded

@pytest.mark.skip
@pytest.mark.parametrize("key", [x for x in range(1,23)])
@pytest.mark.parametrize("alphabeticKey", ["0","0123"])
@pytest.mark.parametrize("spaceEncrypt", ["0","1"])
def test_transposition(message, key, alphabeticKey, spaceEncrypt, caplog):
    """Test the transposition function"""
    caplog.set_level(logging.DEBUG)

    alphabet = TRCH.returnAlphabet(alphabeticKey, spaceEncrypt)
    mode = 0
    encoded = TRCH.transposition(mode, message, key)
    mode = 1
    decoded = TRCH.transposition(mode, encoded, key)
    assert message == decoded

# @pytest.mark.skip
@pytest.mark.parametrize("key", [x for x in range(1,43)])
@pytest.mark.parametrize("alphabeticKey", ["0","0123"])
@pytest.mark.parametrize("spaceEncrypt", ["0", "1"])
def test_transcode(message, key, alphabeticKey, spaceEncrypt):
    """Test the translate function"""

    alphabet = TRCH.returnAlphabet(alphabeticKey, spaceEncrypt)

    mode = 0
    encoded = TRCH.translate(key, mode, message, alphabet)
    mode = 1
    decoded = TRCH.translate(key, mode, encoded, alphabet)
    assert message == decoded

