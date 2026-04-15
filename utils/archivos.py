import json
import csv


def cargar_json(ruta):
    with open(ruta, "r") as archivo:
        return json.load(archivo)


def cargar_csv(ruta):
    datos = []
    with open(ruta, newline="") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            datos.append(fila)
    return datos


def guardar_json(ruta, datos):
    with open(ruta, "w") as archivo:
        json.dump(datos, archivo, indent=4)


def guardar_csv(ruta, datos):
    with open(ruta, "w", newline="") as archivo:
        campos = datos[0].keys()
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(datos)
