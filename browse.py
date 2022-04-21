def connect():
	print("Welcome to the decentralized browser :)")
	domain=input("Input The Hash Of The File You Need To Find : ")
	from importlib import reload
	try:
		import socket,json,time,requests,hashcrawl,hasher,browser
		reload(hashcrawl)
		income=hashcrawl.crawl(domain)
		if income!=False:
			print("Found Document!")
			html= income[1:-1]
			if domain!=hasher.makehash(html):
				print("The File Received Was Tampered!")
			else:
				browser.start(html)
		else:
			print("File does not exist/corrupted on this node! Try a different node if you think this is a false alert.")
	except Exception as e:
		if str(e)=="dictionary update sequence element #0 has length 1; 2 is required":
			print("File in-existant on the node!\nTry a different node if you think this is a false alert.")
		else:
			print(e)