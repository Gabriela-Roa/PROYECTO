def Menú():
    print("\n-------------------------------------------------")
    print("¡¡¡BIENVENIDO A CLARO!!!")
    print("\nSeleccione la opción que necesita")
    print("1. Usuarios")    
    print("2. Gestión de Servicios")    
    print("3. Reportes")
    print("4. Ventas")
    print("5. Salir")
    print("\n-------------------------------------------------")
    
def usuarios():
    print("\n-------------------------------------------------")
    print("\nUsuarios    ")
    print("1. Actualizar Perfil")
    print("2. Crear un nuevo perfil")
    print("3. Eliminar Perfil")
    print("4. Servicios y promociones personalizadas")
    print("6. Menú")
    print("\n-------------------------------------------------")
   
def Gestion_de_servicios():
    print("\n-------------------------------------------------")
    print("\nGestion de servicios")
    print("1. Agregar servicio")
    print("2. Modificar servicio")
    print("3. Eliminar servicio")
    print("4. Lista de servicios")
    print("6. Menú")
    print("\n-------------------------------------------------")
    
def Reportes():
    print("\n-------------------------------------------------")
    print("\nReporte")
    print("1. Informes")
    print("2. Servicios populares") # esto puede ir en informes
    print("3. Usuarios que han adquirido los servicios") # esto puede ir en informes 
    print("6. Menú")
    print("\n-------------------------------------------------")
    
def ventas():
    print("\n-------------------------------------------------")
    print("\nVentas")
    print("1. Registro de productos y servicios")
    print("2. Registro de ventas")
    print("6. Menú")
    print("5. salir")
    print("\n-------------------------------------------------")
    
def pedir_opcion():
    while True:
        try:
            opc = int(input("Ingrese su opción: "))
            print("\n-------------------------------------------------")
            return opc
        except:
            print("Valor inválido")
            print("\n-------------------------------------------------")
            return -1
    

    
    
    
    