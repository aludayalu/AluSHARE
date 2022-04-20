raddr=''
def launch():
    global remoteaddr
    import socket, requests, time, json,msgfilter,nodeverify,hasher
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
    p=input("Port to listen at : ")
    p=int(p)
    s.bind(("0.0.0.0", p))
    print("Binding port "+str(p))
    s.listen()
    print("Trying to List your node to the api...")
    try:
        in1=input("Are you using a proxy or tunneling agent?(yes/no)(default:no) : ")
        if in1=="yes" or in1=="y" or in1=="Yes":
            ip = input("Input your tunnelled/proxied address without the scheme : ")
            port = input("Port : ")
            raddr=ip+":"+port
            req_base = f"https://ltzapi.loca.lt/addnode?ip={ip}:{port}"
            addnodereq = get(req_base).text
        elif in1=="no" or in1=="n" or in1=="No":
            print("Outsourcing I.P.")
            ip = get('https://api.ipify.org').text
            req_base = f"https://ltzapi.loca.lt/addnode?ip={ip}:{port}" 
            addnodereq = get(req_base).text
            raddr=ip+":"+str(p)
    except Exception as e:
        print(e)
        raddr="127.0.0.1:"+str(p)
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
    print("Node Init Successful.")
    def client_thread(client):
        global all_clients
        while True:
            try:
                msgenc = client.recv(1024)
                msg = str(msgenc.decode())
                if msg == "hi":
                    print("Sending 3rd Handshake")
                    client.send("yo".encode())
                    print("Successful Handshake")
                elif msgfilter.filter(msg,"type")=="post":
                    print("Incoming Post Request")
                    if nodeverify.check(msg)==True:
                        print("Integrity Verification Passed!")
                        html=str(msgfilter.filter(msg,"html"))
                        domain=hasher.makehash(html)
                        query.add("chain",{domain:html})
                        client.send("True".encode())
                        time.sleep(0.5)
                        client.send(domain.encode())
                        print("Successful Upload!")
                    elif nodeverify.check(msg)==False:
                        print("Integrity Verification Failed!")
                        client.send("False".encode())
                elif msgfilter.filter(msg,"type")=="get":
                    print("Incoming GET Request!")
                    try:
                        domain=msgfilter.filter(msg,"domain")
                        result=json.dumps(query.get("chain",domain))
                        if result=="False":
                            print("Requested File Does Not Exist On Our Node!")
                            client.send("File does not exist/corrupted!".encode())
                        else:
                            print("File Hash Found! Sending File!")
                            client.send(str(result).encode())
                    except:
                        client.send("File does not exist/corrupted!".encode())
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
                    print("\n------NEW-SOCKET-CONNECTION------\n----------------------------------")
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