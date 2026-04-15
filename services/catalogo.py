from models.videojuego import juegops5, juegoxbox, juegonintendo


class catalogo:
    def __init__(self):
        self.juegos = []

    def cargar(self, datos):
        for d in datos:
            juego = self.crear_juego(d)
            self.juegos.append(juego)

    def crear_juego(self, d):
        consola = d["consola"].lower()

        if consola == "ps5":
            return juegops5(**d)
        elif consola == "xbox":
            return juegoxbox(**d)
        else:
            return juegonintendo(**d)

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
            print(j.nombre, "-", j.precio)
