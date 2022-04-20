def check(msg):
    try:
        import msgfilter,hasher
        e=msgfilter.filter(msg,"e")
        n=msgfilter.filter(msg,"n")
        sign=msgfilter.filter(msg,"sign")
        html=msgfilter.filter(msg,"html")
        hash=msgfilter.filter(msg,"orighash")
        if hasher.makehash(html)!=hash:
            return False
        import hasher,alursa
        hash=hasher.makehash(html)
        verifyresult=alursa.verify(sign,hash,e,n)
        if verifyresult=="Untampered":
            return True
        elif verifyresult=="tampered":
            return False
    except:
        return False