from services.catalogo import catalogo
from services.carrito import carrito
from services.factura import generar_factura
from utils.archivos import cargar_json

cat = catalogo()
car = carrito()

datos = cargar_json("data/juegos.json")
cat.cargar(datos)

while True:

    print("\n1. ver catalogo")
    print("2. agregar juego")
    print("3. agregar al carrito")
    print("4. ver carrito")
    print("5. finalizar compra")
    print("6. salir")

    opcion = input("\n")

    try:

        if opcion == "1":
            cat.listar()

        elif opcion == "2":
            id = input()
            nombre = input()
            categoria = input()
            precio = float(input())
            rating = input()
            stock = int(input())
            consola = input()

            from models.videojuego import videojuego

            nuevo = videojuego(id, nombre, categoria, precio, rating, stock, consola)
            cat.agregar(nuevo)

        elif opcion == "3":
            id = input()
            cantidad = int(input())

            juego = cat.buscar(id)
            if juego:
                car.agregar(juego, cantidad)

        elif opcion == "4":
            car.mostrar()

        elif opcion == "5":
            cliente = input()
            archivo = input()
            formato = input()

            generar_factura(car, cliente, archivo, formato)

        elif opcion == "6":
            break

    except Exception:
        pass
