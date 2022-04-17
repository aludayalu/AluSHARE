import socket,json,time
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
def message(msg: dict,ip):
    host = ip.split(":")[0]
    port = ip.split(":")[1]
    s.settimeout(0.1)
    s.connect((ip, port))
    s.settimeout(None)
    s.send("hi".encode())
    time.sleep(0.1)
    s.send("hi".encode())
    s.recv(1024000)
    message=json.dumps(msg)
    s.send(message.encode())
    s.recv(1024000)
    s.close()