import string
letters = string.ascii_lowercase + string.ascii_uppercase
standardprobabilities = {'A' : 0.0817, 'N' : 0.0675,
'B' : 0.0150, 'O' : 0.0751,
'C' : 0.0278, 'P' : 0.0193,
'D' : 0.0425, 'Q' : 0.0010,
'E' : 0.1270, 'R' : 0.0599,
'F' : 0.0223, 'S' : 0.0633,
'G' : 0.0202, 'T' : 0.0906,
'H' : 0.0609, 'U' : 0.0276,
'I' : 0.0697, 'V' : 0.0098,
'J' : 0.0015, 'W' : 0.0236,
'K' : 0.0077, 'X' : 0.0015,
'L' : 0.0403, 'Y' : 0.0197,
'M' : 0.0241, 'Z' : 0.0007}

def encrypt(plaintext, key):
    ciphertext = ''
    for char in plaintext:
        if char in letters:
            ciphertext += letters[(letters.index(char) + key) % len(letters)]
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    for char in ciphertext:
        if char in letters:
            plaintext += letters[(letters.index(char) - key) % len(letters)]
        else:
            plaintext += char
    return plaintext

def bruteforce(ciphertext, search=None):
    plaintexts = []
    if search == None:
        for key in range(1, len(letters)):
            plaintexts.append(decrypt(ciphertext, key))
    else:
        for key in range(1, len(letters)):
            if search in decrypt(ciphertext, key):
                plaintexts.append(decrypt(ciphertext, key))
    return plaintexts

def charcount(ciphertext, probabilities=False):
    counts = {}
    for i in string.ascii_uppercase:
        amount = ciphertext.count(i.lower()) + ciphertext.count(i.upper())
        if probabilities:
            counts[i] = amount / len(ciphertext)
        else:
            counts[i] = amount
    return counts
    
