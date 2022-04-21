import json 
def get(dbname,query):
    try:
        path=dbname+"\\"+query
        file=open(path)
        return file.read()
    except:
        return "False"

def add(dbname,query):
    import os.path
    import hasher
    filehash=hasher.makehash(query)
    pathtohash=dbname+"\\"+filehash
    file_exists = os.path.exists(pathtohash)
    if file_exists==False:
        with open(pathtohash, 'x') as f:
            f.write(query)
        return True
    else:
        return False