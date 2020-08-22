import os, time, json

def leerjson():
    
    ruta = os.path.dirname(os.path.abspath(__file__)) #Obtiene la ruta del script en ejecución
    print(" ---- Obteniendo archivo de ", ruta, "------")
    time.sleep(1)
    archivo = open(ruta + "/archivo.json")
    print(" --- Lectura de archivo.json --- \n")

    datosjson = json.load(archivo)
    for articulo in datosjson['articulos']:
        time.sleep(1)
        print('Nombre: ', articulo['nombre'])
        print('Precio: ', articulo['precio'])
        print('Codigo: ', articulo['codigo'])
        print('Existencia: ', articulo['existencias'])
        print('')

    print(" -- FIN -- \n")
    time.sleep(2)