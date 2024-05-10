from menu import *


RUTA_DE_DATOS = "datos.json"

datos = cargar_datos(RUTA_DE_DATOS)

while True:
    Menú()
    opc = pedir_opcion
    if opc == 1:
        