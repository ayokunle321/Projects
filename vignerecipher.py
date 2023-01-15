from math import log2

ALPHABET = "\n !\"'(),-.0123456789:;?ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decrypt(text, key):

    """
    decrypt(text, key) - takes a ciphertext (encrypted text) and a short key,
    and deciphers it using vigenere's cipher
    text - Some text as a str. All characters must be in ALPHABET
    key - Some text as a str. All characters must be in ALPHABET
    """
    decrypted = ""
    for position in range(len(text)):
        text_character = ALPHABET.index(text[position])
        key_character = ALPHABET.index(key[position % len(key)])
        decrypted_char = (text_character - key_character) % len(ALPHABET)
        decrypted += ALPHABET[decrypted_char]
    return decrypted


def get_frequencies(text):
    
    '''
    Description: Function obtains the relative frequency of a particular charachter
    in a given text
    Input: Some text as a str
    Return: a dictionary which contains all the relative frequencies of each (ALPHABET) 
    charater in the text.
    
    '''
    letter_frequency = {}
    for letter in text:
        letter = letter.upper()
        keys = letter_frequency.keys()
        if letter in ALPHABET:
            if letter in keys:
                letter_frequency[letter] += 1 / len(text)
            else:
                letter_frequency[letter] = 1 / len(text)
        
    return letter_frequency

    
def cross_entropy(freqs1, freqs2): 
    '''
    Description: Function compares two dictionaries of frequencies and computes their cross entropy
    Input: Two different relative frequency dictionaries.
    Return: Cross entropy of the two frequency dictionaries as a float.
    
    '''
    merged = [] # getting the keys (characters) of the two dictionaries in one list without duplicates
    for key in freqs1.keys():
        merged.append(key)
    
    for key in freqs2.keys():
        if key not in freqs1.keys():
            merged.append(key)     
            
    cross_value = 0.0
    
    # getting the minimum value (relative frequency) of each dictionary
    f1_min = min(freqs1.values()) 
    f2_min = min(freqs2.values())
    
    for char in merged:
        
        # replacing the relative frequency of character that's not in either one of the
        # dictionaries (0) with the minmum relative frequency so the log can be safely taken care of
        
        if char in freqs1.keys(): 
            if  char not in freqs2.keys():
                freqs2[char] = f2_min
        
        
        if char in freqs2.keys():
            if char not in freqs1.keys():
                freqs1[char] = f1_min
                
        cross_value -= freqs1[char] * log2(freqs2[char])
            
    return cross_value
    

def guess_key(encrypted):
    
    '''
    Description: Guesses the key of the encrypted text in encrypted based on the frequencies in the dictionary english_frequencies.
    Input: Some encrypted text as a str
    Return: A key consisting of 3 characters as a str
    
    '''
    
    with open('frank.txt', 'r') as infile:
        english_text = infile.read()
        english_frequencies = get_frequencies(english_text)
    
    key = ""

    for i in range(3):
        chars_encrypted = encrypted[i::3].upper() # every third letter from the first three letters in the encrypted text
        char_cross_values = {}
        for char in ALPHABET:
            cross_value = cross_entropy(english_frequencies, get_frequencies(decrypt(chars_encrypted, char)))
            char_cross_values[char] = cross_value
        lowest_cross_char = min(char_cross_values, key = char_cross_values.get) #getting chararcter with lowest cross value
 
        key = key + lowest_cross_char 
    
    return key
    


def crack(encrypted_text):
    
    '''
    Function: Decrypts the text string encrypted_text using the guessed key
    Input: Some encrypted text as a str
    Returns: Some decrypted text as a str
    '''
    
    return decrypt(encrypted_text, guess_key(encrypted_text))





    
    
    


