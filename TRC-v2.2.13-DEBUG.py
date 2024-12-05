# Transposition Reverse Caesar cipher Debug Program
import math as m

def outOfRange(char, msg):
    # Simple range check 
    return char >= len(msg)

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
    print('Please enter a key (1 - %s)' % alphabetLength)
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
            
def getMessage():
    print('Please enter your message')
    message = input()
    
    return message # Returns message
    
def getMode():
    print('Please enter your mode (e = encrypt, d = decrypt)')
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
    SYMBOLS = '`-=[]\;,./~!@#$%^&*()_+{}|:"<>?'
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
    print('Value of i: %s' % i)
    while i >= 0:
        # This adds the character to the translated variable
        print('Added reversed character: %s' % message[i])
        translated = translated + message[i]
        # i gets reduced to go to the next letter in the string
        i -= 1
        print('New value of i: %s' % i)
        
    print('Final reversed message: %s' % translated)
        
    return translated
    
def caesar(code, message, key, alphabet):
    print()
    translated = ''
    # It does this for every character in the message
    for character in message:
        if character in alphabet:
            # Finding the character in the alphabet and recording the number
            letterNum = alphabet.find(character)
            print('letterNum: %s' % letterNum)
            
            if mode == 0:
                letterNum += key
                print('Mode C encrypt')
                print('New letterNum: %s' % letterNum)
            elif mode == 1:
                letterNum -= key
                print('Mode C decrypt')
                print('New letterNum: %s' %  letterNum)
            
            # Handling the wrap around
            if letterNum > len(alphabet):
                print('Wrap around 1')
                letterNum -= len(alphabet)
                print('New letterNum: %s' % letterNum)
            elif letterNum < 0:
                print('Wrap around 2')
                letterNum += len(alphabet)
                print('New letterNum: %s' % letterNum)
                
            # Adding the translated text
            translated = translated + alphabet[letterNum]
            print('C Adding: %s' % alphabet[letterNum])
            
        else:
            # If the translate failed for some reason just add the character anyways
            translated = translated + character
            print('Failed, adding character anyways: %s' % character)
            
    print('Final Caesar: %s' % translated)
    return translated
    
def transposition(mode, msg, key):
    print()
    if mode == 0:
        # Encrypt
        print('Mode T is encrypt')
        char = col = 0
        print('char: %s, col: %s' % (char, col))
        translated = ''
    
        while char < len(message) and col < key:
            if not outOfRange(char, message):
                print('Adding %s' % message[char])
                translated += message[char]
                
            char += key
            print('New char: %s' % char)
            
            if outOfRange(char, message):
                print('Range check 2e')
                if col < key:
                    col += 1
                    char = col
                    print('New char; %s, new col: %s' % (char, col))
                    
        print('Final encrypted transposition output: %s' % translated)
        return translated
        
    if mode == 1:
        # Decrypt
        print('Mode T decrypt')
        translated = ''
        char = col = 0
        print('char: %s, col: %s' % (char, col))
        rem = len(msg) % key
        print('Rem: %s' % rem)
        rows = m.trunc(len(msg) / key)
        print('Rows: %s' % rows)
        decryptRows = rows + 1 if rem > 0 else rows
        print('DecryptRows: %s' % decryptRows)
        
        
        while len(msg) != len(translated) and col <= decryptRows:
            if outOfRange(char, msg):
                print('Range check 1d')
                break
            
            translated += msg[char]
            print('Adding: %s' % msg[char])
            char += decryptRows
            print('New char: %s' % char)
            
            if outOfRange(char, msg):
                print('Range check 2d')
                if col < decryptRows:
                    col += 1
                    char = col
                    print('New char: %s, col: %s' % (char, col))
                    continue
        
        print('Final decrypted transposition output: %s' % translated)
        return translated

def translate(key, mode, message, alphabet):
    print()
    translated = ''
    # If mode is decrypt then reverse the cipher first
    if mode == 1:
        print('Mode D, reversing message...')
        message = reverse(message)
        print('Message: %s' % message)
    
    translated = transposition(mode, caesar(mode, message, key, alphabet), key)
            
    if mode == 0:
        print('Mode E, reversing message...')
        translated = reverse(translated)
        print('Translated: %s' % translated)
        
    print('Final fully translated message: %s' % translated)
    return translated # Returning translated text
       
mode = getMode()
alphabeticKey, spaceEncrypt = getAlphabeticKey()
alphabet = returnAlphabet(alphabeticKey, spaceEncrypt)
key = getKey(len(alphabet))
message = getMessage()

print()
print('Below is your translated text:\n\n')
print(translate(key, mode, message, alphabet))

