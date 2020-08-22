import time
import lectorxml

print("\n\nNota: los archivos se cargarán automaticamente\n\n")

while True:

    print("\n ............. MENU PRINCIPAL .............. \n")

    print("[1] Leer archivo xml \n[2] Leer archivo json \n[3] Leer archivo csv \n[4] Salir")

    try:
        entrada = int(input("Ingrese una opción: "))
        if entrada == 1:
            lectorxml.leerxml()
        elif entrada == 2:
            pass
        elif entrada == 3:
            pass
        elif entrada == 4:
            print("\n - BYE - \n")
            time.sleep(2)
            break
    except ValueError:
        print("\nDebe seleccionar una opción del 1 - 4\n")