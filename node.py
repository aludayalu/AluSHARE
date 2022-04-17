def launch():
    import socket, requests, time, json,msgfilter,informer,nodeverify,sync
    from aludbms import makedb,query
    try:
        open("chain.aludb","r+")
    except:
        makedb.fresh("chain")
    from random import random
    from requests import get
    from threading import Thread
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    invisible = False
    s.bind(("0.0.0.0", 7777))
    print("Binding port 7777")
    s.listen()
    print("Trying to List your node to the api...")
    try:
        in1=input("Are you using a proxy or tunnelling agent?(yes/no)(default:no) : ")
        if in1=="yes" or in1=="y" or in1=="Yes":
            ip = input("Input your tunnelled/proxied address without the scheme : ")
            req_base = f"http://127.0.0.1:8080/addnode?ip={ip}" 
            addnodereq = get(req_base).text
        else:
            ip = get('https://api.ipify.org').text
            req_base = f"http://127.0.0.1:8080/addnode?ip={ip}" 
            addnodereq = get(req_base).text
    except:
        invisible=True
        addnodereq="Rest-Api is not online."
        print("HUH")
    all_clients = []
    if "Error : " not in addnodereq:
        print("\n------Node-Successfully-Listed------")
        print("|                                  |")
        print("|   ###         LTZ         ###    |")
        print("|                                  |")
        print("#################-##################")
    else:
        print("Unable to list node")
        print(f"Error : {addnodereq}")
        print("--------------------------------")
        print("Launching node in invisible mode")
        invisible = True
        print('Listening for new clients on local network')
    try:
        sync.start()
    except Exception as e:
        print("Error : "+str(e))
    print("Node Init Successful.")
    def client_thread(client):
        global all_clients
        while True:
            try:
                msgenc = client.recv(1024)
                msg = str(msgenc.decode())
                if msg == "hi":
                    client.send("yo".encode())
                    print("Normalized")
                elif msgfilter.filter(msg,"type")=="post":
                    if nodeverify.check(msg)==True:
                        domain=str(msgfilter.filter(msg,"domain"))
                        html=str(msgfilter.filter(msg,"html"))
                        query.add("chain",{domain:html})
                        client.send("True".encode())
                        if msgfilter.filter(msg,"relayed")!=False:
                            msg["relayed"]="True"
                            informer.inform(msg,ip)
                    elif nodeverify.check(msg)==False:
                        client.send("False".encode())
                elif msgfilter.filter(msg,"type")=="get":
                    try:
                        domain=msgfilter.filter(msg,"domain")
                        result=json.dumps(query.get("chain",domain))
                        if result=="False":
                            client.send("File does not exist/corrupted!".encode())
                        else:
                            client.send(str(result).encode())
                    except:
                        client.send("File does not exist/corrupted!".encode())
                elif msgfilter.filter(msg,"type")=="sync":
                    try:
                        print("Dumping DB for syncing.")
                        file=open("chain.aludb","r+")
                        data=str(json.dumps(file.read()))
                        s.send(data.encode())
                    except Exception as e:
                        client.send(("Sync Error : ").encode())
            except Exception as e:
                print("Client Disconnected!")
                client.close()
                break

    while True:
        try:
            client, addr = s.accept()
            if invisible==True:
                if "127.0.0.1" in addr:
                    all_clients.append(client)
                    print("\n------NEW--SOCKET-CONNECTION------")
                    print("----------------------------------")
                    srvenc = client.recv(1024)
                    srvmsg = str(srvenc.decode())
                    if srvmsg == "api-ping":
                        client.close()
                        all_clients.remove(client)
                        print("Api-Ping socket")
                    else:
                        thread = Thread(target=client_thread, args=(client,))
                        thread.start()
                else:
                    print("Addresses outside of your local machine will not be allowed to connect during invisible mode!")
            else:
                all_clients.append(client)
                print("\n------NEW--SOCKET-CONNECTION------")
                srvenc = client.recv(1024)
                srvmsg = str(srvenc.decode())
                if srvmsg == "api-ping":
                    client.close()
                    all_clients.remove(client)
                    print("Api-Ping socket was established")
                else:
                    thread = Thread(target=client_thread, args=(client,))
                    thread.start()
        except:
            print("A socket was falsely connected to")