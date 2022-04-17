from more_itertools import peekable


def ping(ip,port):
    try:
        import socket,time
        host = ip
        s = socket.socket(socket.AF_INET,
                          socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((ip, port))
        s.settimeout(None)
        msg="api-ping"
        s.send(msg.encode())
        return True
    except Exception as e:
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print(e)
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        return False