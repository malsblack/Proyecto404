import json

def Accessibility_Focused():
    with open('./config/config.json', 'r') as archivo:
        data = json.load(archivo)
        return data['Accessibility_Focused']

def Modern_Technological():
    with open('./config/config.json', 'r') as archivo:
        data = json.load(archivo)
        return data['Modern_Technological']
    
def Warm_Friendly():
    with open('./config/config.json', 'r') as archivo:
        data = json.load(archivo)
        return data['Warm_Friendly']
    
def Professional_Sober():
    with open('./config/config.json', 'r') as archivo:
        data = json.load(archivo)
        return data['Professional_Sober']
    
def Modern_Classic():
    with open('./config/config.json', 'r') as archivo:
        data = json.load(archivo)
        return data['Modern_Classic']
    
def Elegant_Contemporary():
    with open('./config/config.json', 'r') as archivo:
        data = json.load(archivo)
        return data['Elegant_Contemporary']
    
def Dynamic_Vibrant():
    with open('./config/config.json', 'r') as archivo:
        data = json.load(archivo)
        return data['Dynamic_Vibrant']
    
def Minimalist_Chic():
    with open('./config/config.json', 'r') as archivo:
        data = json.load(archivo)
        return data['Minimalist_Chic']
    
