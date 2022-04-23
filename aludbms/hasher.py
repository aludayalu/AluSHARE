hashtooutput="xxxxxxxxxxxxxxxxxxxxxxxx"
lastletter="#"
def currentletterhasher(letter,seq):
    number = ord(letter)
    currenthash = int(number) % int(seq)
    return currenthash

def chargen(char):
    global hashtooutput
    global lastletter
    out=''
    lastnum = ''
    numbers = ''
    lastord = '1'
    lastord =  ord(lastletter)
    sequence=1
    for x in hashtooutput:
        sequence+=1
        newchr=(chr(currentletterhasher(lastletter,sequence)+lastord+currentletterhasher(x,ord(char))*(round(len(out)/sequence))))
        out+=str(newchr)
        lastord=ord(x)
    hashtooutput=out
    return hashtooutput

def makehash(msg):
    global hashtooutput
    hashtooutput="xxxxxxxxxxxxxxxxxxxxxxxx"
    for x in msg:
        chargen(x)
    return (hashtooutput.encode().hex())[6:]
