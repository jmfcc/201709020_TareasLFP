import csv, os, time

def leercsv():
    
    ruta = os.path.dirname(os.path.abspath(__file__)) #Obtiene la ruta del script en ejecución
    print(" ---- Obteniendo archivo de ", ruta, "------")
    time.sleep(1)
    archivo = open(ruta + "/archivo.csv")
    print(" --- Lectura de archivo.csv --- \n")

    atributos = []
    datos = []
    init = True
    for line in archivo:
        if init:
            atributos = line.strip().split(",")
            init = False
        else:
            datos.append(line.strip().split(","))
    
    for dato in datos:
        time.sleep(1)
        print(atributos[0], ": ", dato[0])
        print(atributos[1], ": ", dato[1])
        print(atributos[2], ": ", dato[2])
        print(atributos[3], ": ", dato[3])
        print()
    
    print(" -- FIN -- \n")
    time.sleep(2)
#leercsv()