def start():
    from requests import get
    print("------Sync-Initiated------")
    myip=get('https://api.ipify.org').text
    myip="127.0.0.1"
    ip=(get("http://127.0.0.1:8080/node").text)[1:-1]
    if ip!=myip:
        print(f'Node selected to Sync with : {ip}\n')
        import socket,time,json
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        port = 7777
        s.settimeout(0.1)
        s.connect((ip, port))
        s.settimeout(None)
        s.send("hi".encode())
        time.sleep(0.1)
        s.send("hi".encode())
        a=s.recv(1024000)
        msg=str({"type":"sync"})
        s.send(msg.encode())
        data=s.recv(10240000000).decode()
        if data!="Sync Error : ":
            file=open("chain.aludb","r+")
            file.write(str(data))
            print("Synced\n")
        else:
            print("Error while syncing databases\n")
    else:
        print("The given node to sync was same as your local machine.\nTherefore Node syncing was cancelled\nPlease retry manually with the sync command in rockie if you really need to sync.\n")