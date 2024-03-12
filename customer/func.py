import json

def load_data():
    f=open('data.json','r')
    return json.load(f)

def save_data(custlist):
    f=open('data.json','w')
    json.dump(custlist,f,indent=2)
    f.close()
    



