from os import linesep, path, system
import json
import webbrowser

def getsource():
    ruta = path.dirname(path.abspath(__file__)) #Obtiene la ruta del script en ejecución
    #archivo = open(ruta + "/archivo.csv")
    return ruta

def openhtml(archivo):
    try:
        webbrowser.open(archivo)
    except:
        print("Error")


def reporte(db):
    rutahtml = getsource() + "/Reporte.html"
    filehtml = open(rutahtml, "w") #open("Reporte.html", "w")
    filehtml.write("<!DOCTYPE html>\n" 
        + "<Html>\n"
        + "\n"
        + "<Head>\n"
        + "    <meta charset=\"utf-8\">\n"
        + "    <title>REPORTE DE REGISTROS</title>\n"
        + "    <link rel=\"stylesheet\" href=\"stylerep.css\">\n"
        + "</Head>\n"
        + "<body>\n"
        + "    <h1>REGISTROS</h1>\n"
        + "    <table>\n"
        + "        <tbody>\n")
    filehtml.write("            <tr>\n"
        + "                <th>No. REGRISTRO</th>\n"
        + "                <th>NOMBRE</th>\n"
        + "                <th>EDAD</th>\n"
        + "                <th>ACTIVO</th>\n"
        + "                <th>SALDO</th>\n"
        + "            </tr>" + linesep)
    cont = 1
    for dic in db:
        filehtml.write("            <tr>\n"
            + "                <td>" + str(cont) + "</td>\n"
            + "                <td>" + dic["nombre"] + "</td>\n"
            + "                <td>" + str(dic["edad"]) + "</td>\n"
            + "                <td>" + str(dic["activo"]) + "</td>\n"
            + "                <td>" + str(dic["saldo"]) + "</td>\n")
        cont = cont + 1
    filehtml.write(" </table>" + "</body>" + "</html>" + linesep)
    filehtml.close()

    rutacss = getsource() + "/stylerep.css"
    if not path.isfile(rutacss):
        filecss = open(rutacss, "w")
        filecss.write("body{\n"
            + "    background-color: #40475B\n;"
            + "}\n"
            + "h1{\n"
            + "    color: white;\n"
            + "    background-color: #DBA409;\n"
            + "    font-size: 50pt;\n"
            + "    display: block;\n"
            + "    text-align: center;\n"
            + "}\n"
            + "table{\n"
            + "    margin: 0 auto;\n"
            + "}\n"
            + "tbody{\n"
            + "    color: white;\n"
            + "    background-color: #CE052C;\n"
            + "    font-size: 18px;\n"
            + "    border: darkred 2px solid;\n"
            + "    border-collapse: collapse;"
            + "    margin: 0px 0px;\n"
            + "}\n"
            + "td{\n"
            + "    width: 200px;\n"
            + "    padding: 10px;\n"
            + "    text-align: center;\n"
            + "    border: darkred 2px solid;\n"
            + "}\n"
            + "th{\n"
            + "    text-align: center;\n"
            + "    border: darkred 2px solid;\n"
            + "}")
        filecss.close()
    print("\n ----------- Reporte generado ---------- ")
    openhtml(rutahtml)

def inicio():
    ruta = getsource() + "/sample.json"
    file = open(ruta)
    db = json.load(file)
    reporte(db)


inicio()