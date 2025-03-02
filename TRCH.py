# Transposition Reverse Caesar cipher Program
import numpy as np
import logging
from lib import inverse
from sympy import Matrix

# Initiate logger
log = logging.getLogger(__name__)
logLevel = logging.DEBUG
logging.basicConfig(level=logLevel, format='%(levelname)s: %(message)s')

def outOfRange(char, msg):
    # Simple range check 
    return char >= len(msg)

def tryParseAlphabeticString(string):
    for i in range(len(string)):
        if string[i] not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            return False
        
    return True

def tryParseInt(string):
    # You could also use .isdigit() instead
    try:
        # Attempt to convert the string to an integer\
        integer = int(string)
        return True
    except ValueError:
        # If conversion fails, return None and False
        return False

def getKey(alphabetLength):
    # Gets a valid key
    i = 0
    print('Please enter a numeric key (1 - %s)' % alphabetLength)
    key = input()
    
    while True:
        if tryParseInt(key) != True:
            print('Please enter a valid key')
            key = input()
            continue
        elif key == '':
            print('Please enter a valid key')
            key = input()
            continue
        elif len(key) > 2:
            print('Please enter a valid key')
            key = input()
            continue
        elif int(key) > 96 or int(key) < 1:
            print('Please enter a valid key')
            key = input()
            continue
        elif int(key) > alphabetLength:
            print('Please enter a valid key')
            key = input
            continue
        else:
            break
    
    return int(key) # Returns the key as a valid integer

def getHillKey(matrixSize):
    print('Please enter a %s character text key (A-Z):' % (matrixSize * matrixSize))
    key = input()

    while len(key) != (matrixSize * matrixSize) or not tryParseAlphabeticString(key) or key == '':
        print('Please enter a valid key')
        key = input()

    return key


def getMatrixSize():
    print('Please enter a matrix size:')
    size = input()

    while not tryParseInt(size):
        print('Please enter a valid matrix size')
        size = input()

    return int(size)
            

def getMessage():
    print('Please enter your message')
    message = input()
    
    return message # Returns message
    
def getMode():
    print('Please enter your mode (e = encrypt, d = decrypt)')
    mode = input()

    while mode == '':
        mode = input()
    
    while mode[0].lower() != 'e' and mode[0].lower() != 'd':
        print('Please enter a valid mode')
        mode = input()
    # It should be a valid mode now so we need to allocate it a binary value
    # 0 for encrypt, 1 for decrypt
    if mode[0].lower() == 'e':
        validMode = 0
    else:
        validMode = 1
    return validMode
            

def getAlphabeticKey():
    # This gets the alphabetic key from the user
    print('Please enter your alphabetic key (0 = lower, 1 = upper, 2 = numeric, 3 = symbolic)')
    alphabeticKey = input()
    for i in range(1):
        
        while alphabeticKey[i] == '':
            print('Please enter a valid alphabetic key')
            alphabeticKey = input()
        
        while alphabeticKey[i] not in '0123':
            print('Please enter a valid alphabetic key')
            alphabeticKey = input()
        
        while len(alphabeticKey) > 4:
            print('Please enter a valid alphabetic key')
            alphabeticKey = input()
            
    # Check for space encrypting
    print('Would you like to translate spaces? (0 = No, 1 = Yes)')
    spaceEncrypt = input()
    
    for i in range(1):
        while spaceEncrypt == '':
            print('Please enter a valid space translate key')
            spaceEncrypt = input()
        
        while len(spaceEncrypt) > 1 or spaceEncrypt[i] not in '01':
            print('Please enter a valid space translate key')
            spaceEncrypt = input()
    
    return alphabeticKey, spaceEncrypt
    
def returnAlphabet(alphabeticKey, spaceEncrypt):
    # Alphabets
    LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
    UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    NUMERIC = '1234567890'
    SYMBOLS = '`-=[]\\;,./~!@#$%^&*()_+{}|:"<>?'
    SPACE = ' '
    
    finalAlphabet = ''
    
    for i in range(len(alphabeticKey)):
        
        if alphabeticKey[i] == '0':
            finalAlphabet += LOWERCASE
        elif alphabeticKey[i] == '1':
            finalAlphabet += UPPERCASE
        elif alphabeticKey[i] == '2':
            finalAlphabet += NUMERIC
        elif alphabeticKey[i] == '3':
            finalAlphabet += SYMBOLS
            
    if spaceEncrypt == '1':
        finalAlphabet += SPACE
    
    return finalAlphabet
    
def reverse(message):
    translated = ''
    
    i = len(message) - 1
    log.debug('Value of i: %s' % i)
    while i >= 0:
        # This adds the character to the translated variable
        log.debug('Added reversed character: %s' % message[i])
        translated = translated + message[i]
        # i gets reduced to go to the next letter in the string
        i -= 1
        log.debug('New value of i: %s' % i)
        
    log.debug('Final reversed message: %s' % translated)
        
    return translated
    
def caesar(mode, message, key, alphabet):
    log.debug('Caesar cipher:')
    log.debug(' ')
    translated = ''
    # It does this for every character in the message
    for character in message:
        log.debug('for loop 1c')
        if character in alphabet:
            # Finding the character in the alphabet and recording the number
            letterNum = alphabet.find(character)
            log.debug('letterNum: %s' % letterNum)
            
            if mode == 0:
                letterNum += key
                log.debug('Mode C encrypt')
                log.debug('Changing letterNum by: %s' % key)
                log.debug('New letterNum: %s' % letterNum)
                log.debug(' ')
            elif mode == 1:
                letterNum -= key
                log.debug('Mode C decrypt')
                log.debug('Changing letterNum by: %s' % key)
                log.debug('New letterNum: %s' %  letterNum)
                log.debug(' ')
            
            # Handling the wrap around
            if letterNum >= len(alphabet):
                log.debug('Wrap around 1')
                letterNum -= len(alphabet)
                log.debug('New letterNum: %s' % letterNum)
                log.debug(' ')
            elif letterNum < 0:
                log.debug('Wrap around 2')
                letterNum += len(alphabet)
                log.debug('New letterNum: %s' % letterNum)
                log.debug(' ')
                
            # Adding the translated text
            try:
                translated = translated + alphabet[letterNum]
            except IndexError:
                log.debug(f'Index is: {letterNum}')
                log.debug(f'Alphabet len is: {len(alphabet)}')
            log.debug('C Adding: %s' % alphabet[letterNum])
            log.debug(' ')
            
        else:
            # If the translate failed for some reason just add the character anyways
            translated = translated + character
            log.debug('Failed, adding character anyways: %s' % character)
            log.debug(' ')
            
    log.debug('Final Caesar: %s' % translated)
    return translated
    
def transposition(mode, msg, key):
    log.debug('Transposition cipher:')
    log.debug(' ')

    if mode == 0:
        # Encrypt
        log.debug('Mode T encrypt')
        char = col = 0
        log.debug('char: %s, col: %s' % (char, col))
        translated = ''
        rem = len(msg) % key
        log.debug('Rem: %s' % rem)
        rows = np.trunc(len(msg) / key)
        log.debug('Rows: %s' % rows)
        decryptRows = rows + 1 if rem > 0 else rows
        log.debug('DecryptRows: %s' % decryptRows)
        log.debug(' ')

        dif = int((decryptRows * key) - len(msg))
        if dif > 0:
            for i in range(dif):
                msg += "ꣾ"
    
        while char < len(msg) and col < key:
            if not outOfRange(char, msg):
                log.debug('Adding %s' % msg[char])
                log.debug(' ')
                translated += msg[char]
                
            char += key
            log.debug('New char: %s' % char)
            log.debug(' ')
            
            if outOfRange(char, msg):
                log.debug('Range check 2e')
                if col < key:
                    col += 1
                    char = col
                    log.debug('New char; %s, new col: %s' % (char, col))
                    log.debug(' ')

        log.debug('Final encrypted transposition output: %s' % translated)
        return translated
        
    if mode == 1:
        # Decrypt
        log.debug('Mode T decrypt')
        translated = ''
        char = col = 0
        log.debug('char: %s, col: %s' % (char, col))
        rem = len(msg) % key
        log.debug('Rem: %s' % rem)
        rows = np.trunc(len(msg) / key)
        log.debug('Rows: %s' % rows)
        decryptRows = rows + 1 if rem > 0 else rows
        log.debug('DecryptRows: %s' % decryptRows)
        log.debug(' ')
        
        
        while len(msg) != len(translated) and col <= decryptRows:
            if outOfRange(char, msg):
                log.debug('Range check 1d')
                break
            
            translated += msg[char]
            log.debug('Adding: %s' % msg[char])
            char += decryptRows
            log.debug('New char: %s' % char)
            log.debug(' ')
            
            if outOfRange(char, msg):
                log.debug('Range check 2d')
                if col < decryptRows:
                    col += 1
                    char = col
                    log.debug('New char: %s, col: %s' % (char, col))
                    log.debug(' ')
                    continue
        
        translated = translated.rstrip("ꣾ")

        log.debug('Final decrypted transposition output: %s' % translated)
        return translated

def hill(mode, msg, key, matrixSize):
    log.debug('Hill Cipher:')
    log.debug(' ')
    keyMatrix = np.zeros((matrixSize, matrixSize), dtype=int).reshape(3,3)
    textVector = np.zeros((matrixSize, 1), dtype=int).reshape(3,1)
    cipherVector = np.zeros((matrixSize, 1), dtype=int).reshape(3,1)
    vectorDict = {}
    translated = ''

    k = 0
    for i in range(matrixSize):
        log.debug(i)
        for x in range(matrixSize):
            log.debug(x)
            keyMatrix[i][x] = ord(key[k])
            log.debug(keyMatrix)
            k += 1
            log.debug(k)

    rem = len(msg) % matrixSize
    while rem != 0:
        msg += "ꣾ"
        log.debug('New msg: %s' % msg)
        rem = len(msg) % matrixSize
        log.debug('New rem: %s' % rem)

    
    numVecs = int(len(msg) / matrixSize)
    log.debug(numVecs)
    for i in range(numVecs):
        vectorDict[f'tvec{i}'] = textVector.copy()
        log.debug(vectorDict)
        vectorDict[f'cvec{i}'] = cipherVector.copy()
        log.debug(vectorDict)

    if mode == 1:
        log.debug('Hill Decrypt:')
        # keyMatrix = np.linalg.inv(keyMatrix) % 26
        keyMatrix = inverse(keyMatrix, 26)
        log.debug(f'Hill inv key matrix: {keyMatrix}')
        charOffset = 0
    else:
        log.debug('Hill Encrypt:')
        charOffset = 0

    
    log.debug(' ')

    index = 0
    log.debug('index: %s' % index)
    for i in range(numVecs):
        log.debug('i: %s' % i)
        for x in range(matrixSize):
            log.debug('x: %s' % x)
            vectorDict[f'tvec{i}'][x] = ord(msg[index])
            log.debug(vectorDict)
            index += 1
            log.debug('index: %s' % index)

    for i in range(numVecs):
        vectorDict[f'cvec{i}'] = np.dot(keyMatrix, vectorDict[f'tvec{i}']) % 26 + charOffset
        log.debug(vectorDict)
        log.debug(i)

    for i in range(numVecs):
        log.debug(i)
        for x in range(matrixSize):
            log.debug('x: %s' % x)
            log.debug('str vector: %s' % str(vectorDict[f'cvec{i}'][x]))
            translated += chr(int(str(vectorDict[f'cvec{i}'][x]).strip('[]')))
            log.debug('translated: %s' % translated)

    return translated
    
    
    

def translate(key, mode, message, alphabet, hillKey, matrixSize):
    log.debug(' ')
    translated = ''
    # If mode is decrypt then reverse the cipher first
    if mode == 1:
        log.debug('Mode D, reversing message...')
        message = reverse(message)
        log.debug('Message: %s' % message)
    
    translatedCaesar = caesar(mode, message, key, alphabet)
    log.debug(translatedCaesar)
    translatedTransCaesar = transposition(mode, translatedCaesar, key)
    log.debug(translatedCaesar)
    translated = hill(mode, translatedTransCaesar, hillKey, matrixSize)
    log.debug(translated)

    
    if mode == 0:
        log.debug('Mode E, reversing message...')
        translated = reverse(translated)
        log.debug('Translated: %s' % translated)
        
    log.debug('Final fully translated message: %s' % translated)
    return translated # Returning translated text

if __name__ == '__main__':
    # gMode = getMode()

    # alphabeticKey, spaceEncrypt = getAlphabeticKey()
    # alphabet = returnAlphabet(alphabeticKey, spaceEncrypt)
    # numKey = getKey(len(alphabet))
    # matrixSize = getMatrixSize()
    # hillKey = getHillKey(matrixSize)
    # gMessage = getMessage()

    print()
    print('Below is your translated text:\n')
    log.debug(' ')
    #print(translate(numKey, gMode, gMessage, alphabet, hillKey, matrixSize))
    message = 'Hello World!'
    key = 'LOGBIGAND'
    encMessage = hill(0, message, key, 3)
    print(encMessage)
    decMessage = hill(1, encMessage, key, 3)
    print(decMessage)

