from array import array
import messenger,requests,json
def inform(msg: dict,me):
    msg["relay"]="no"
    nodelist=requests.get("http://127.0.0.1:8080/nodes/")
    nodes=array(json.loads(nodelist.text))
    for x in nodes:
        if x!=me:
            try:
                messenger.message(msg,x)
            except:
                print("Unreachable node for broadcast")