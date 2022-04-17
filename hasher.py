hashtooutput = 'xxxxxxxxxxxxxxxxxxxxxxxx'
hashlength = len(hashtooutput)
lastnum = '0'

def currentletterhasher(letter,seq):
    number = ord(letter)
    currenthash = int(number) % int(seq)
    return currenthash

def loophash(stringletter):
    global hashtooutput
    stringord = ord(stringletter)
    sequence = 1
    outputh = ''
    ll = "f"
    for letter in hashtooutput:
        sequence = sequence + 1
        hashletter = letter
        currentord = ord(hashletter)
        lastord = ord(ll)
        processhash = chr(round((currentletterhasher(letter,sequence)+currentletterhasher(ll,sequence))*(stringord)))
        outputh = str(processhash) + str(outputh)
        ll = letter
    return outputh
def makehash(msg):
    global hashtooutput
    hashtooutput='xxxxxxxxxxxxxxxxxxxxxxxx'
    for char in msg:
        a = loophash(char)
        hashtooutput=a
    return hashtooutput.encode().hex()