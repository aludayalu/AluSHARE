import json 
def get(dbname,query,contains=False):
    res={}
    try:
        db=open((dbname+".aludb"),mode="r+")
    except:
        print("Error : False Database Name or Directory(Make sure the DB file is located in the same directory\nAnd do not include the extension along with the DB name.")
        quit()
    dbcontents=dict(json.loads(db.read()))
    totallength=len(dbcontents["blocks"])
    results={"results":[]}
    if totallength!=0:
        for i in range(totallength):
            for key in dbcontents["blocks"][i-1]:
                if key==query:
                    res=dict(dbcontents["blocks"][i-1])
                    results["results"].append(res)
                elif contains==True:
                    if query in key:
                        res=dict(dbcontents["blocks"][i-1])
            i+=1
        if len(res)>0:
            return res
        else:
            return "False"
    else:
        return "False"

def add(dbname,query: dict):
    try:
        db=open((dbname+".aludb"),mode="r+")
    except:
        print("Error : False Database Name or Directory(Make sure the DB file is located in the same directory\nAnd do not include the extension along with the DB name.")
        return False
    for key in query:
        dbkey=key
    try:
        if get(dbname,dbkey)=="False":
            dbcontents=dict(json.loads(db.read()))
            dbcontents["blocks"].append(query)
            db=open((dbname+".aludb"),"r+")
            db.write(str(json.dumps(dbcontents)))
            return True
        else:
            print(get(dbname,dbkey))
            print("duplication")
            return False
    except Exception as e:
        print(e)