from random import randint

# Generate a random integer between 1 and 26
#SHIFT = 22 #randint(1,26)

TEXT = "ESTE ES UN MENSAJE DE AMISTAD"
TEXT2 = "AOPA AO QJ IAJOWFA ZA WIEOPWZ"


#ENCRYPTION = ""
#DECRYPTION = ""

def encryption(text, SHIFT):
    ENCRYPTION = ""    
    for character in text:
        # Check if character us an uppercase letter
        if character == ' ':
            ENCRYPTION += character 
        elif character.isupper():
            ENCRYPTION = ENCRYPTION + chr((ord(character) + SHIFT - 65) % 26 + 65)
        else:
            ENCRYPTION = ENCRYPTION + chr((ord(character) + SHIFT - 97) % 26 + 97)
    
    print(f'The key is: {SHIFT}')
    print(f'The plain text is: {text}')
    print(f'Encrypted text is: {ENCRYPTION}')
    return ENCRYPTION




def decryption(text, SHIFT):
    DECRYPTION = ""    
    for character in text:
        # Check if character us an uppercase letter
        if character == ' ':
            DECRYPTION += character 
        elif character.isupper():
            DECRYPTION = DECRYPTION + chr((ord(character) - SHIFT - 65) % 26 + 65)
        else:
            DECRYPTION = DECRYPTION + chr((ord(character) - SHIFT - 97) % 26 + 97)
    
    print(f'The key is: {SHIFT}')
    print(f'The plain text is: {text}')
    print(f'Decrypted text is: {DECRYPTION}')
    return DECRYPTION


def isBlank (myString):
    if myString and myString.strip():
        #myString is not None AND myString is not empty or blank
        return False
    #myString is None OR myString is empty or blank
    return True

