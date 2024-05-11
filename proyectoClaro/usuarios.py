def actualizar_perfil(datos:dict):
    
    nombre =input("Ingrese el nombre del cliente: ")
    for i in range(len(datos["usuarios"])):
        if datos["usuarios"][i]["nombre"]== nombre:
            usuario={}
            usuario["nombre"]=input("Ingrese el nombre: ")
            usuario["documento"]=input("Ingrese el numero de documento: ")
            usuario["direccion"]=input("Ingrese la direccion: ")
            usuario["contacto"]=input("Ingrese el contacto: ")
            usuario["correo electronico"]=input("Ingrese el correo electronico: ")
            usuario["categoría"]=input("Ingrese la categoría: ")
            usuario["servutilizado"]=input("Ingrese el servicio utilizado: ")
            
            datos["usuarios"][i].update(usuario)
        return datos
        
def crear_un_nuevo_perfil(datos):
    datos = dict(datos)
    usuario={}
    usuario["Nombre"]=input("Ingrese el nombre: ")
    usuario["Direccion"]=input("Ingrese la direccion: ")
    usuario["Contacto"]=input("Ingrese el contacto: ")
    usuario["Correo electronico"]=input("Ingrese el correo electronico: ")
    usuario["Categoría"]=input("Ingrese la categoría: ")
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
    nombre = input("Ingrese el nombre del cliente: ")
    if nombre in range(len(datos["usuarios"])):
        print("El cliente existe")
    servutilizado = input("Ingrese el servicio que el cliente está utilizando: ")
    for i in range(len(datos["usuarios"])):
        if datos ["usuarios"][i]["servutilizado"] == servutilizado:
            for i in range(len(datos["servicios"])):
                print("Señor(a)" + nombre + "le recomendamos los siguientes servicios: " + i )
    return datos

def salir(datos:dict):
    
    opc = 5
    try:
         if opc == 5:
            print("Has salido de VerSe")
    except Exception:
        opc == 0
        opc = int(input("Ingrese una opción valida: "))
    return datos

