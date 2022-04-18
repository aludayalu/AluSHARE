def upload(d,e,n):
    print("Welcome to the dev-ops section of the network")
    inphtml=input("Enter the data u want to be uploaded either in the form of html or plain text : ")
    import alursa,hasher
    hash=hasher.makehash(inphtml)
    sign=alursa.signature(hash,d,n)
    import socket,requests,json,random,time,uid
    api_nodes=requests.get("https://ltzapi.loca.lt/node")
    mynode=str(api_nodes.text)
    host = mynode.split(":")[0]
    port = mynode.split(":")[1]
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('127.0.0.1', port))
    s.send("dev".encode())
    time.sleep(0.1)
    s.send("hi".encode())
    msg=s.recv(1024000)
    print(msg)
    time.sleep(0.1)
    domainuid=uid.gen()
    domain=domainuid
    postmsg=json.dumps({"type":"post","domain":domain,"html":inphtml,"e":e,"n":n,"sign":sign})
    s.send(postmsg.encode())
    status=s.recv(1024000).decode()
    if status=="True":
        print("Sent")
        print("Your uid was : " + domainuid)
        print("Upload uri : " + domain)
    else:
        print("File upload failed!")