# Reverse Caesar cipher debug program
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
    while i >= 0:
        # This adds the character to the translated variable
        translated = translated + message[i]
        # i gets reduced to go to the next letter in the string
        i -= 1
        
    return translated
    
def caesar(mode, message, key, alphabet):
    translated = ''
    # It does this for every character in the message
    for character in message:
        if character in alphabet:
            # Finding the character in the alphabet and recording the number
            letterNum = alphabet.find(character)
            if mode == 0:
                letterNum += key
            elif mode == 1:
                letterNum -= key
            
            # Handling the wrap around
            if letterNum > len(alphabet):
                letterNum -= len(alphabet)
            elif letterNum < 0:
                letterNum += len(alphabet)
            # Adding the translated text
            translated = translated + alphabet[letterNum]
            
        else:
            # If the translate failed for some reason just add the character anyways
            translated = translated + character
            
    return translated
    
def transposition(mode, msg, key):
    if mode == 0:
        # Encrypt
        char = col = 0
        translated = ''
    
        while char < len(message) and col < key:
            if not outOfRange(char, message):
                translated += message[char]
                
            char += key
            
            if outOfRange(char, message):
                if col < key:
                    col += 1
                    char = col
                    
        return translated
        
    if mode == 1:
        # Decrypt
        translated = ''
        char = col = 0
        rem = len(msg) % key
        rows = m.trunc(len(msg) / key)
        decryptRows = rows + 1 if rem > 0 else rows
        
        
        while len(msg) != len(translated) and col <= decryptRows:
            if outOfRange(char, msg):
                break
            
            translated += msg[char]
            char += decryptRows
            
            if outOfRange(char, msg):
                if col < decryptRows:
                    col += 1
                    char = col
                    continue
        
        return translated

def translate(key, mode, message, alphabet):
    translated = ''
    # If mode is decrypt then reverse the cipher first
    if mode == 1:
        message = reverse(message)
    
    translated = transposition(mode, caesar(mode, message, key, alphabet), key)
            
    if mode == 0:
        translated = reverse(translated)
        
    return translated # Returning translated text
       
mode = getMode()
alphabeticKey, spaceEncrypt = getAlphabeticKey()
alphabet = returnAlphabet(alphabeticKey, spaceEncrypt)
key = getKey(len(alphabet))
message = getMessage()

print()
print('Below is your translated text:')
print(translate(key, mode, message, alphabet))

