import socket,json,time,requests
from array import array
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
def test(ip,uid):
    host = ip.split(":")[0]
    port = int(ip.split(":")[1])
    s.settimeout(1)
    s.connect((host, port))
    s.settimeout(None)
    s.send("dev".encode())
    time.sleep(0.5)
    s.send("hi".encode())
    msg=s.recv(1024)
    message=json.dumps({"type":"get","domain":uid})
    s.send(message.encode())
    msg=s.recv(1024000).decode()
    if msg=="File does not exist/corrupted!":
        s.close()
        return False
    else:
        s.close()
        return msg

def crawl(uid):
    nodelist=requests.get("https://ltzapi.loca.lt/nodes/")
    nodes=json.loads(nodelist.text)
    out=""
    print("Finding Document on all Nodes")
    for x in nodes:
        resultoftest=test(x,uid)
        if resultoftest!=False:
            out=resultoftest
            break
    if out=="":
        return False
    else:
        return out