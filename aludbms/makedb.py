import json,os
def fresh(name):
    if not os.path.exists(name):
        os.makedirs(name)
    else:    
        pass