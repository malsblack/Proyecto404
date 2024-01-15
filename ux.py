# Definiré una función que acepta el nombre del router y devuelve las credenciales para ese router específico.
from tools.connection import lista_routers


def obtener_credenciales(router, datos):

    if router in datos:
        print(datos[router]["User"])
        print(datos[router]["Password"])
        
    else:
        return "Router no encontrado."


datos_routers=lista_routers()
print(datos_routers)
obtener_credenciales("R2", datos_routers)
