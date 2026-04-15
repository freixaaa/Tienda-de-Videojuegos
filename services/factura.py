from datetime import datetime
from utils.archivos import guardar_json, guardar_csv


def generar_factura(carrito, cliente, nombre_archivo, formato):
    datos = {
        "cliente": cliente,
        "fecha": str(datetime.now()),
        "items": [],
        "total": carrito.total()
    }

    for i in carrito.items:
        datos["items"].append({
            "nombre": i["juego"].nombre,
            "cantidad": i["cantidad"],
            "precio": i["juego"].precio
        })

    if formato == "json":
        guardar_json(nombre_archivo + ".json", datos)
    else:
        guardar_csv(nombre_archivo + ".csv", datos["items"])
