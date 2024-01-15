import json

def routers():
    with open('routers.json', 'r') as archivo:
        routers = json.load(archivo)
        return routers

