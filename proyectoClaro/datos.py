import json

def cargar_datos(archivo):
    with open(archivo, "r") as file:
        datos=json.load(file)
    return datos

def guardar_datos(datos, archivo):
    datos = dict(datos)
    
    diccionario=json.dumps(datos)
    file=open(archivo, "w")
    file.write(diccionario)
    file.close

