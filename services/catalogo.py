from models.videojuego import juegops5, juegoxbox, juegonintendo


class catalogo:
    def __init__(self):
        self.juegos = []

    def cargar(self, datos):
        for d in datos:
            juego = self.crear_juego(d)
            self.juegos.append(juego)

    def crear_juego(self, d):

        datos = {
            "id": d["id"],
            "nombre": d["nombre"],
            "categoria": d["categoria"],
            "precio": float(d["precio"]),
            "rating": d.get("esrb") or d.get("rating"),
            "stock": int(d["stock"]),
            "consola": d["consola"]
        }

        consola = datos["consola"].lower()

        if consola == "ps5":
            return juegops5(**datos)
        elif consola == "xbox":
            return juegoxbox(**datos)
        else:
            return juegonintendo(**datos)

    def agregar(self, juego):
        for j in self.juegos:
            if j.id == juego.id:
                raise Exception("id repetido")
        self.juegos.append(juego)

    def buscar(self, id):
        for j in self.juegos:
            if j.id == id:
                return j
        return None

    def listar(self):
        for j in self.juegos:
            print("id:", j.id, "| nombre:", j.nombre, "| precio:", j.precio, "| stock:", j.stock)
