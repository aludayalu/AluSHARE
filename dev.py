from os import stat


def upload(d,e,n):
    print("Welcome to the dev-ops section of the network")
    inphtml=input("Enter the data u want to be uploaded either in the form of plain text or basic html : ")
    #input("Enter the data u want to be uploaded either in the form of plain text or basic html : ")
    import alursa,hasher
    hash=hasher.makehash(inphtml)
    sign=alursa.signature(hash,d,n)
    import socket,requests,json,random,time,uid
    api_nodes=requests.get("https://ltzapi.loca.lt/node")
    mynode=str(api_nodes.text)
    host = str(mynode.split(":")[0])[1:]
    port = int(str(mynode.split(":")[1])[:-1])
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host, port))
    print("Initiating 3 Step Handshake")
    s.send("dev".encode())
    print("Step 1")
    time.sleep(0.5)
    s.send("hi".encode())
    print("Step 2")
    msg=s.recv(1024000).decode()
    print("Step 3 : Successful Handshake with Node")
    time.sleep(0.5)
    print("Uploading Data")
    postmsg=json.dumps({"type":"post","html":inphtml,"e":e,"n":n,"sign":sign,"orighash":hash})
    try:
        s.send(postmsg.encode())
    except Exception as e:
        print(e+" huh")
    status=s.recv(1024).decode()
    if status=="True":
        print("Sent")
        domainuid=s.recv(1024).decode()
        print("Your Hash Was : " + domainuid)
    elif status=="False":
        print("Confirmed False Upload!")
    else:
        print("File upload failed!")