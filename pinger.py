def ping(ip):
    try:
        import socket,time
        host = ip
        port = 7777
        s = socket.socket(socket.AF_INET,
                          socket.SOCK_STREAM)

        s.settimeout(0.1)
        s.connect(("127.0.0.1", port))
        s.settimeout(None)
        msg="api-ping"
        s.send(msg.encode())
        return True
    except:
        return False