import json
def fresh(name):
    base={
        "blocks":[

        ]
    }
    file = name+".aludb"
    print("Opening/Creating DB file.")
    open(file, 'a').close()
    print("File opened/created successfully.")
    dbname=name+".aludb"
    file=open(dbname,"w+")
    base["name"]=name
    base["encoding"]="JSON"
    base["dbtype"]="ALUDB"
    base["multiplekey"]="TRUE"
    print("Formatting DB file with I.S.")
    file.write(json.dumps(base))
    print("DB formatted and ready for production.")

def format(name):
    base={
        "blocks":[
        ]
    }
    try:
        print("Opening/Creating DB file.")
        file=open((name+".aludb"),mode="w")
    except:
        print("Error : False Database Name or Directory(Make sure the DB file is located in the same directory\nAnd do not include the extension along with the DB name.")
        quit()
    dbname=name+".aludb"
    base["name"]=name
    base["encoding"]="JSON"
    base["dbtype"]="ALUDB"
    base["multiplekey"]="TRUE"
    print("Formatting DB file with I.S.")
    file.write(str(json.dumps(base)))
    print("DB formatted and ready for production.")