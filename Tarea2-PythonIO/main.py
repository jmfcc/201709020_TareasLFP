import time
import lectorxml, lectorjson, lectorcsv

print("\n\nNota: los archivos se cargarán automaticamente\n\n")

while True:

    print("\n ............. MENU PRINCIPAL .............. \n")

    print("[1] Leer archivo xml \n[2] Leer archivo json \n[3] Leer archivo csv \n[4] Salir")

    try:
        entrada = int(input("Ingrese una opción: "))
        if entrada == 1:
            lectorxml.leerxml()
        elif entrada == 2:
            lectorjson.leerjson()
        elif entrada == 3:
            lectorcsv.leercsv()
        elif entrada == 4:
            print("\n - BYE - \n")
            time.sleep(1)
            break
        else:
            print("\nOpción no disponible\n")
            time.sleep(1)
    except ValueError:
        print("\nDebe seleccionar una opción del 1 - 4\n")