from services.catalogo import catalogo
from services.carrito import carrito
from services.factura import generar_factura
from utils.archivos import cargar_json, cargar_csv

cat = catalogo()
car = carrito()

# cargar datos
try:
    datos = cargar_json("data/catalogo.json")
except:
    datos = cargar_csv("data/catalogo.csv")

cat.cargar(datos)

while True:

    print("\n1. ver catalogo")
    print("2. agregar videojuego")
    print("3. comprar")
    print("4. salir")

    opcion = input("\nseleccione una opcion: ")

    try:

        # 🔹 VER CATALOGO
        if opcion == "1":
            print("\ncatalogo:")
            cat.listar()

        # 🔹 AGREGAR VIDEOJUEGO
        elif opcion == "2":
            print("\ningrese los datos del videojuego:")

            id = input("id: ")
            nombre = input("nombre: ")
            categoria = input("categoria: ")
            precio = float(input("precio: "))
            rating = input("rating: ")
            stock = int(input("stock: "))
            consola = input("consola (ps5/xbox/nintendo): ")

            from models.videojuego import videojuego

            nuevo = videojuego(id, nombre, categoria, precio, rating, stock, consola)
            cat.agregar(nuevo)

            print("\njuego agregado correctamente")

        # 🔹 SUBMENÚ DE COMPRA
        elif opcion == "3":

            while True:

                print("\n--- carrito ---")
                print("1. agregar juego")
                print("2. eliminar juego")
                print("3. ver carrito")
                print("4. finalizar compra")
                print("5. volver al menu")

                op = input("\nseleccione una opcion: ")

                # agregar juego
                if op == "1":
                    print("\nusa el id del juego (ver catalogo con opcion 1)")

                    id = input("id del juego: ")
                    cantidad = int(input("cantidad: "))

                    juego = cat.buscar(id)

                    if juego:
                        car.agregar(juego, cantidad)
                        print("juego agregado al carrito")
                    else:
                        print("juego no encontrado")

                # eliminar juego
                elif op == "2":
                    id = input("id del juego a eliminar: ")
                    car.eliminar(id)
                    print("juego eliminado")

                # ver carrito
                elif op == "3":
                    print("\ncontenido del carrito:")
                    car.mostrar()

                # finalizar compra
                elif op == "4":
                    cliente = input("nombre del cliente: ")
                    archivo = input("nombre del archivo: ")
                    formato = input("formato (json/csv): ")

                    generar_factura(car, cliente, archivo, formato)

                    print("compra finalizada y factura generada")

                # salir del carrito
                elif op == "5":
                    break

        # 🔹 SALIR
        elif opcion == "4":
            break

    except Exception as e:
        print("error:", e)
