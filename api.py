from flask import *
import socket,pinger,os,random
import time
app = Flask(__name__)
app.config.from_object(__name__)
nodes=[]

def generateMet(data):
        metrics = json.dumps(data)
        return metrics

def nodecheck():
    for x in nodes:
        if pinger.ping(x)==True:
            print(x," Is still up and running")
        else:
            nodes.remove(x)
    print("In total ",len(nodes)," Nodes are running")

@app.route('/node',methods = ['GET'])
def giveanynode():
    ip_addr = request.environ['REMOTE_ADDR']
    try:
        selectednode = nodes[random.randint(0, (len(nodes) - 1))]
    except:
        selectednode=nodes
    response = make_response(generateMet(selectednode), 200)
    response.mimetype = "text/plain"
    return response

@app.route('/nodes/',methods = ['GET'])
def getlist():
    ip_addr = request.environ['REMOTE_ADDR']
    print(ip_addr)
    print(nodes)
    #if ip_addr in nodes:
    if 1==1:
        def generateMetrics():
            nodecheck()
            metrics = json.dumps(nodes)
            return metrics
        response = make_response(generateMetrics(), 200)
        response.mimetype = "text/plain"
        return response
    else:
        return "uWu"

@app.route('/addnode',methods = ['POST','GET'])
def addnode():
    args=request.args
    ipport=args.get("ip")
    ip=str(ipport).split(":")[0]
    port=int(str(ipport).split(":")[1])
    if (ip==None):
        return "Error : Invalid I.P. addresses are not accepted!"
    else:
        if ip=="0.0.0.0":
            return "Error : Invalid I.P. addresses are not accepted!"
        else:
            if ip in nodes:
                response = make_response(generateMet("Already In List"), 200)
                response.mimetype = "text/plain"
                return response
            else:
                if pinger.ping(ip,port) == True:
                    nodes.append(ipport)
                    response = make_response(generateMet("Added"), 200)
                    response.mimetype = "text/plain"
                    return response
                else:
                    response = make_response(
                        generateMet("Error : Un-Pingable. Please check if port 7777 is portforwarded on your node"), 200)
                    response.mimetype = "text/plain"
                    return response
app.run(host="0.0.0.0",port=8080)