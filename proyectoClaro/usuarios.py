import json

def actualizar_perfil(datos):
    datos = dict(datos)
    datos = {}
    lista = datos.get("usuarios")
    documento_cliente =input("Ingrese el documento del cliente: ")
    for i in lista:
        if i.get("documento") == documento_cliente:
            usuario={}
            usuario["nombre"]=input("Ingrese el nombre: ")
            usuario["documento"]=input("Ingrese el numero de documento: ")
            usuario["direccion"]=input("Ingrese la direccion: ")
            usuario["contacto"]=input("Ingrese el contacto: ")
            usuario["correo electronico"]=input("Ingrese el correo electronico: ")
            usuario["categoría"]=input("Ingrese la categoría: ")
            usuario["servutilizado"]=input("Ingrese el servicio que está utilizado: ")
            datos["muestra"][lista.index(i)] == usuario
        return datos
        
def crear_un_nuevo_perfil(datos):
    datos = dict(datos)
    usuario={}
    usuario["nombre"]=input("Ingrese el nombre: ")
    usuario["documento"]=input("Ingrese el numero de documento: ")
    usuario["direccion"]=input("Ingrese la direccion: ")
    usuario["contacto"]=input("Ingrese el contacto: ")
    usuario["correo electronico"]=input("Ingrese el correo electronico: ")
    usuario["categoría"]=input("Ingrese la categoría: ")
    usuario["servutilizado"]=input("Ingrese el servicio que está utilizado: ")
    return datos

def eliminar_perfil(datos):
    datos = dict(datos)
    documento =input("Ingrese el documento del cliente: ")
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["documento"] == documento:
            datos["usuarios"].pop(i)
            print("Cliente eliminado")
            return datos

def servicios_y_promociones_personalizadas(datos):
    datos = dict(datos)
    documento_cliente = input("Ingrese el documento del cliente: ")
    if documento_cliente in range(len(datos["usuarios"])):
        print("El cliente existe")
    servutilizado = input("Ingrese el servicio que el cliente está utilizando: ")
    for i in range(len(datos["usuarios"])):
        if datos ["usuarios"][i]["servutilizado"] == servutilizado:
            for i in range(len(datos["servicios"])):
                print("Señor(a) le recomendamos los siguientes servicios: " + i )
    return datos

def salir(datos):
    datos = dict(datos)
    opc = 5
    try:
         if opc == 5:
            print("Has salido de VerSe")
    except Exception:
        opc == 0
        opc = int(input("Ingrese una opción valida: "))
    return datos


    
    
