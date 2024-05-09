def Menú():
    print("\n-------------------------------------------------")
    print("Bienvenidos a claro")
    print("\nSeleccione la opción que necesita")
    print("1. Usuarios")    
    print("2. Gestión de Servicios")    
    print("3. Reportes")
    print("4. Ventas")
    print("5. Salir")
    print("\n-------------------------------------------------")
    
def usuarios():
    print("\n-------------------------------------------------")
    print("1. Actualizar Perfil")
    print("2. Crear un nuevo perfil")
    print("3. Elimir Perfil")
    print("4. Servicios y promociones personalizadas")
    print("5. Menú")
    print("\n-------------------------------------------------")

def Gestion_de_servicios():
    print("\n-------------------------------------------------")
    print("1. Agregar servicio")
    print("2. Modificar servicio")
    print("3. Eliminar servicio")
    print("4. Lista de servicios")
    print("5. Menú")
    print("\n-------------------------------------------------")
    
def Reportes():
    print("\n-------------------------------------------------")
    print("1. Informes")
    print("2. Servicios populares")
    print("3. Usuarios que han adquirido los servicios")
    print("4. Menú")
    print("\n-------------------------------------------------")
    
def ventas():
    print("\n-------------------------------------------------")
    print("1. Registro de productos y servicios")
    print("2. Registro de ventas")
    print("Menú")
    print("\n-------------------------------------------------")

def pedir_opcion():
    opc = 0
    try:
        opc = int(input("Ingrese su opción: "))
        print("\n-------------------------------------------------")
        return opc
    except Exception:
        print("Valor inválido")
        print("\n-------------------------------------------------")
        return -1
    

    
    
    
    