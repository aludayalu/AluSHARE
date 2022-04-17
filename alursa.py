import random
def randomkeygen(bits=1024):
    from Crypto.PublicKey import RSA
    keypair = RSA.generate(1024)
    d = keypair.d
    e = keypair.e
    n = keypair.n
    return d,e,n

def signature(hash,d,n):
    bytedhash = int.from_bytes(bytes.fromhex(hash), byteorder='big')
    signature = pow(bytedhash,d,n)
    return signature

def verify(signature,hash,e,n):
    bytedhash = int.from_bytes(bytes.fromhex(hash), byteorder='big')
    hashFromSignature = pow(signature,e,n)
    if hashFromSignature==bytedhash:
        return "Untampered"
    else:
        return "tampered"