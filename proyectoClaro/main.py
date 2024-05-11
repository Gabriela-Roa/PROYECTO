from datos import *
from menu import *
from usuarios import *

PRIMERA_RUTA_DE_DATOS = "proyectoClaro/modulos.json"
SEGUNDA_RUTA_DE_DATOS = "servicios.json"

datos = cargar_datos(PRIMERA_RUTA_DE_DATOS)

while True:
    Menú()
    opc = pedir_opcion()
    if opc == 1:
        usuarios()
        while True:
            opc = pedir_opcion()
            if opc == 1:
                datos = actualizar_perfil(datos)
            elif opc == 2:
                datos = crear_un_nuevo_perfil(datos)
            elif opc == 3:
                datos = eliminar_perfil(datos)
            elif opc == 4:
                datos = servicios_y_promociones_personalizadas(datos)
            elif opc == 6:
                datos = Menú()
    elif opc == 2:
        Gestion_de_servicios()
        opc = pedir_opcion()
    elif opc == 3:
        Reportes()
        opc = pedir_opcion()
    elif opc == 4:
        ventas()
        opc = pedir_opcion()
    elif opc == 5:
        print("chao no vuelva")
        break   
     
     
    
guardar_datos(datos, PRIMERA_RUTA_DE_DATOS)
