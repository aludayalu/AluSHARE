hashtooutput = 'xxxxxxxxxxxxxxxx'
def currentletterhasher(letter,seq):
    number = ord(letter)
    currenthash = int(number) % int(seq)
    return currenthash

def loophash(stringletter):
    sequence = 1
    outputh = ''
    lastletter = 'F'
    for letter in hashtooutput:
        sequence = sequence + 1
        hashletter = letter
        currentord = ord(hashletter)
        lastord =  ord(lastletter)
        stringord = ord(stringletter)
        processhash = chr(round((currentletterhasher(lastletter,sequence)+lastord+currentletterhasher(hashletter,ord(stringletter))*(round(len(outputh)+sequence)))))
        outputh = str(processhash) + str(outputh)
        lastletter = letter
    return outputh

def makehash(estreng):
    try:
        global hashtooutput
        hashtooutput = 'xxxxxxxxxxxxxxxx'
        for letter in estreng:
            k = loophash(letter)
            hashtooutput = k
        return hashtooutput.encode('utf-8', 'replace').hex()
    except Exception as e:
        print("Hashing Error : ",e)