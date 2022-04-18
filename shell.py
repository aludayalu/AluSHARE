import time
logo="""""""""
                                                                       %%%%%.%                                                                       
                                                                    %%%% %%%%%%%%%%                                                                   
                                                               %%%%%%%%%%%%%%%%%%%%%%%%,                                                              
                                                           %%%%%%%%%%%%%% %#%%%%%%%%%%#%%%%%                                                          
                                                       %%%%%%%%%%%%%%%%% %%%% %%%%%%% %%%%%%%%%%                                                      
                                                     %%%%%%%%%%%%%%%%%% %%%%%%% %%%% %%%%%%%%%%%%%                                                    
                                                      %%%%%%%%%%%%%%%%,%%%%%%%%%%. %%%%%%%%%%%%%%%                                                    
                                                     %% %%%%%%%%%%%%%%%%%%%%%%%%%  %%%%%%%%%%%%%%%                                                    
                                                     %%%% %%%%%%%%% %%%%%%%%%%%%,%%% %%%%%%%%%%%%%                                                    
                                                     %%%%%% %%%%%% %%%%%%%%%%% %%%%%%% %%%%%%%%%%%                                                    
                                                     %%%%%%%% %%% %%%%%%%%%%% %%%%%%%%%#%%%%%%%%%%                                                    
                                                     %%%%%%%%%%  %%%%%%%%%%%%%%%%%%%%%%%% %%%%%%%                                                     
                                                     %%%%%%%%%%/% %%%%%%%% %%%%%%%%%%%%%%%% %%%%,%                                                    
                                                     %%%%%%%%#%%%%% %%%%% %%%%%%%%%%%%%%%%%%%. %%%                                                    
                                                     %%%%%%% %%%%%%%% %#%%%%%%%%%%%%%%%%%%%%%  %%%                                                    
                                                     %%%%%% %%%%%%%%%% .%%%%%%%%%%%%%%%%%%%%%%%% %                                                    
                                                         % %%%%%%%%%% %%%/%%%%%%%%%%%%%%%% %%%                                                        
                                                             %%%%%%.%%%%%%%##%%%%%%%%%%%%                                                             
                                                                 / %%%%%%%%%%%,%%%%%%                                                                 
                                                                      %%%%%%%%%%                                                                      
                                                                          %%%                                                                                                              
"""""""""
print(logo)
loggedin=False
d=0
e=0
n=0

def launchnode():
    if loggedin==True:
        import node
        node.launch()
    else:
        print("You are not logged in! Please issue the login/signup command.")

def greet():
    print("Hello my lovely user <3")
greet()

def login():
    global d
    global e
    global n
    from Crypto.PublicKey import RSA
    try:
        file = open("keys.ltz", "r+").read()
    except:
        print("Unable to open/find keys.ltz.\nPlease manually create a file called ""keys.ltz"" in the same directory as this file \nor if the file exists please give the script permissions to access files.")
    try:
        d = int(file.splitlines()[0])
        e = int(file.splitlines()[1])
        n = int(file.splitlines()[2])
    except:
        print("The file does not have 'd', 'e', 'n' key values in it.\nEither they are in the wrong format/corrupted or simply non existant")
    kp=f"d={d} e={e} n={n}"
    print(f'Importing Private key from Disk...\n{kp}\nKeyPair imported Successfully!\nSuccessfully logged in!')
    global loggedin
    loggedin=True

def signup():
    import alursa
    d,e,n=alursa.randomkeygen()
    file = open("keys.ltz", "w")
    writemsg=f'{d}\n{e}\n{n}'
    file.write(writemsg)
    print(f'd={d} e={e} n={n}')
    print("Successfully generated and stored keypair!")

def myip():
    from requests import get
    ip = get('https://api.ipify.org').text
    print("Your public ipv4 address is : ",ip)

def about():
    print("Hi i am Rockie! Your command line buddy for setting up and managing your nodes onto the Lumatozer Blockchain.\nI dont only manage nodes but can do thing like tell you some jokes, show random news, retreive system info and benchmark DUCK-Hash algo")

def joke():
    from requests import get
    joke=get("https://v2.jokeapi.dev/joke/Any?format=txt&type=single")
    print(joke.text)

def news():
    import random
    import requests
    url = ('https://newsapi.org/v2/top-headlines?'
           'country=us&'
           'apiKey=fdaa905ca01b470399689b918d55539f')
    response = requests.get(url)
    total=len(response.json()['articles'])-1
    newstitle=response.json()['articles'][random.randint(0,total)]['title']
    newsdisc = response.json()['articles'][random.randint(0, total)]['description']
    newsjson=newstitle+"\n"+newsdisc
    print(newsjson)

def logo():
    print(logo)


def ipconfig():
    import socket
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    print("Your Computer Name is : " + hostname)
    print("Your Computers Local IP Address is : " + IPAddr)
    from requests import get
    ip = get('https://api.ipify.org').text
    print("Your Computers Public IP Address is : " + ip)

def ifconfig():
    import socket
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    print("Your Computer Name is : " + hostname)
    print("Your Computers Local IP Address is : " + IPAddr)
    from requests import get
    ip = get('https://api.ipify.org').text
    print("Your Computers Public IP Address is : " + ip)

def uwu():
    import webbrowser
    url="https://www.youtube.com/watch?v=zRHmhtwA2Hk"
    webbrowser.open(url, new=0, autoraise=True)

def UwU():
    import webbrowser
    url="https://www.youtube.com/watch?v=zRHmhtwA2Hk"
    webbrowser.open(url, new=0, autoraise=True)

def credits():
    print("The project was made by Team Lumatozer.\nMay the Ducks rule the world!")

def browse():
    import browser
    browser.connect()

def upload():
    if loggedin==True:
        import dev
        dev.upload(d,e,n)
    else:
        print("You are not logged in! Please issue the login/signup command.")

def sync():
    import sync
    myip="force"
    sync.start(myip)

while True:
    command=input("Rockie >> ")
    try:
        globals()[command]()
    except Exception as e:
        print(f'Error : Command {e} was not found.')