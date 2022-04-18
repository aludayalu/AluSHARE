def connect():
	print("Welcome to the decentralized browser :)")
	domain=input("Input domain name : ")
	try:
		import socket,json,time,requests
		api_nodes=requests.get("https://ltzapi.loca.lt/node")
		mynode=str(api_nodes.text)[1:-1]
		host = mynode.split(":")[0]
		port = int(mynode.split(":")[1])
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.settimeout(1)
		s.connect((host, port))
		s.settimeout(None)
		s.send("client".encode())
		time.sleep(1)
		s.send("hi".encode())
		naach=json.dumps({"type":"get","domain":domain})
		msg = s.recv(1024)
		time.sleep(0.1)
		s.send(naach.encode())
		income=s.recv(1024000).decode()
		if income!="File does not exist/corrupted!":
			html= dict(json.loads(income))[domain]
			f = open('out.html', 'w')
			f.write(html)
			f.close()
			import webbrowser
			webbrowser.open('out.html') 
		else:
			print("File does not exist/corrupted on this node! Try a different node if you think this is a false alert.")
	except Exception as e:
		if str(e)=="dictionary update sequence element #0 has length 1; 2 is required":
			print("File in-existant on the node! Try a different node if you think this is a false alert.")
		else:
			print(e)