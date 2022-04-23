def upload(d,e,n):
    print("Welcome to the dev-ops section of the network")
    choice=input("Do you want to upload a html/txt file or raw txt/html?( 1=raw, 2=file ) : ")
    if choice=="2":
        try:
            fn=input("Enter the file name : ")
            inphtml=open(fn).read()
        except Exception as e:
            print("Unable To Find File!")
            print(e)
            inphtml=input("Enter the data u want to be uploaded either in the form of plain text or basic html : ")
    elif choice=="1":
        inphtml=input("Enter the data u want to be uploaded either in the form of plain text or basic html : ")
    else:
        print("Invalid Choice")
        quit()
    import alursa,hasher
    hash=hasher.makehash(inphtml)
    sign=alursa.signature(hash,d,n)
    import socket,requests,json,random,time
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
        s.send(postmsg.encode('utf-8', 'replace'))
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