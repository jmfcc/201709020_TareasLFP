
elementos = {
    "letra" : ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
    "numero" : ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
    "simbolo" : ["_"]
}

transiciones = [
    ["0", "simbolo", "1"],
    ["1", "simbolo", "1"],
    ["1", "letra", "3"],
    ["3", "numero", "4"],
    ["0", "letra", "2"],
    ["2", "letra", "2"],
    ["2", "numero", "4"]
]


def analizadorcadena():
    print("\n -- Analizador de cadeanas AFD -- ")
    print("\nNota: para detener el programa solo presione enter.\n")

    analiza = True
    while analiza:
        cad = input("Ingresa una cadena para analizar: ")
        if cad:
            estadoActual = "0"
            nexterr = False
            for caracter in cad:
                estadoSiguiente = validaTransicion(estadoActual, definecaracter(caracter))

                if estadoSiguiente.__eq__("None"):
                    #print("cadena inválida")
                    nexterr = True
                    break
                else:
                    #print("Estado Actual: " + estadoActual + "  Simbolo: " + caracter + " ES:" + estadoSiguiente)
                    estadoActual = estadoSiguiente
            if estadoActual == "4" and not nexterr:
                print("Cadena válida")
            else:
                print("Cadena inválida")
        else:
            print("Debe ingresar una cadena")
            analiza = False

def validaTransicion(estadoA, simbolo):
    for tr in transiciones:
        if tr[0] == estadoA and tr[1] == simbolo:
            estadoS = tr[2]
            return estadoS
    return "None"

def definecaracter(caracter):
    if elementos["letra"].__contains__(caracter):
        return "letra"
    elif elementos["numero"].__contains__(caracter):
        return "numero"
    elif elementos["simbolo"].__contains__(caracter):
        return "simbolo"
    else:
        return "none"

analizadorcadena()