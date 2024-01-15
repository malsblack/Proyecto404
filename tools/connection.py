import json
import asyncio
import telnetlib


def lista_routers():
    with open('routers.json', 'r') as archivo:
        routers = json.load(archivo)
        return routers

async def verificar_router(ip, username, password):
    print(f"Verificando router {ip}...")
    try:
        tn = telnetlib.Telnet(ip, timeout=5)
        tn.read_until(b"Username: ", timeout=5)
        tn.write(username.encode('ascii') + b"\n")
        tn.read_until(b"Password: ", timeout=5)
        tn.write(password.encode('ascii') + b"\n")
        tn.write(b"exit\n")
        tn.read_all()
        tn.close()
        return True
    except Exception as e:
        print(f"Error en {ip}: {e}")
        return False

async def monitorear_routers():
    print("Iniciando verificación de routers....")
    routers = await lista_routers()
    tasks = []
    routers=dict(routers)
    for router in routers:
        ip = routers[f'{router}']["IP"]
        username = routers[f'{router}']["User"]
        password = routers[f'{router}']["Password"]
        task = asyncio.ensure_future(verificar_router(ip, username, password))
        tasks.append(task)

    resultados = await asyncio.gather(*tasks)
    resultado_final=[]
    for ip, resultado in zip([routers[f'{router}']["IP"] for router in routers], resultados):
        if resultado:
            print(f"{ip}: OK")
            resultado_final.append(f"{ip}: OK")
        else:
            print(f"{ip}: Router apagado")
            resultado_final.append(f"{ip}: Router apagado")
    return resultado_final

# Ejecutar la función monitorear_routers en el event loop
def iniciar():
    asyncio.run(monitorear_routers())
