def connect():
	print("Welcome to the decentralized browser :)")
	domain=input("Input The Hash Of The File You Need To Find : ")
	try:
		import socket,json,time,requests,uidcrawl
		income=uidcrawl.crawl(domain)
		if income!=False:
			print("Found Document!")
			html= dict(json.loads(income))[domain]
			f = open('alushare.html', 'w')
			f.write(html)
			f.close()
			import webbrowser
			webbrowser.open('alushare.html') 
		else:
			print("File does not exist/corrupted on this node! Try a different node if you think this is a false alert.")
	except Exception as e:
		if str(e)=="dictionary update sequence element #0 has length 1; 2 is required":
			print("File in-existant on the node! Try a different node if you think this is a false alert.")
		else:
			print(e)