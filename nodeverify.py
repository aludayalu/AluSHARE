def check(msg):
    import msgfilter
    e=msgfilter.filter(msg,"e")
    n=msgfilter.filter(msg,"n")
    sign=msgfilter.filter(msg,"sign")
    html=msgfilter.filter(msg,"html")
    import hasher,alursa
    hash=hasher.makehash(html)
    verifyresult=alursa.verify(sign,hash,e,n)
    if verifyresult=="Untampered":
        return True
    elif verifyresult=="tampered":
        return False