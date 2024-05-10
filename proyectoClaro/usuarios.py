def crear_un_nuevo_perfil(datos):
    datos = dict(datos)
    usuario={}
    usuario["Nombre"]=input("Ingrese el nombre: ")
    usuario["Direccion"]=input("Ingrese la direccion: ")
    usuario["Contacto"]=input("Ingrese el contacto: ")
    usuario["Correo electronico"]=input("Ingrese el correo electronico: ")
    usuario["Categoría"]=input("Ingrese la categoría: ")
    return datos



    