from xml.dom import minidom
import os
import time

#from pathlib import Path
#mypath = Path().absolute()
#print('Absolute path : {}'.format(mypath))

def leerxml(): 
    ruta = os.path.dirname(os.path.abspath(__file__)) #Obtiene la ruta del script en ejecución
    print(" ---- Obteniendo archivo de ", ruta, "------")
    time.sleep(2)
    archivo = minidom.parse(ruta + "/archivo.xml")
    print(" --- Lectura de archivo.xml --- \n")
    for empleado in archivo.getElementsByTagName("articulo"):
        time.sleep(2)
        codigo = empleado.getAttribute("codigo")
        attr1 = empleado.getElementsByTagName("nombre")[0]
        attr2 = empleado.getElementsByTagName("precio")[0]
        attr3 = empleado.getElementsByTagName("existencias")[0]
        print("codigo: ", codigo)
        print("Nombre: ", attr1.firstChild.data)
        print("Precio: ", attr2.firstChild.data)
        print("Existencias: ", attr3.firstChild.data)
        print()

    print(" -- FIN -- \n")

    time.sleep(2)