def actualizar_perfil(datos):
    datos = dict(datos)
    usuario={}
    print("¿Que dato desea actualizar?")
    print("1.Nombre, 2.Direccion, 3.Contacto, 4.Correo electronico y 5.Categoría")
    numero = int(input("Ingrese el numero: "))
    if numero == 1:
        usuario["Nombre"]=input("Ingrese el nombre: ")
    elif numero == 2:
        usuario["Direccion"]=input("Ingrese la direccion: ")
    elif numero == 3:
        usuario["Contacto"]=input("Ingrese el contacto: ")
    elif numero == 4:
        usuario["Correo electronico"]=input("Ingrese el correo electronico: ")
    elif numero == 5:
        usuario["Categoría"]=input("Ingrese la categoría: ")
    else:
        print("Ingresa una opción valida")
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

