class videojuego:
    def __init__(self, id, nombre, categoria, precio, rating, stock, consola):
        self._id = id
        self._nombre = nombre
        self._categoria = categoria
        self._precio = float(precio)
        self._rating = rating
        self._stock = int(stock)
        self._consola = consola

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @property
    def stock(self):
        return self._stock

    def reducir_stock(self, cantidad):
        if cantidad <= self._stock:
            self._stock -= cantidad
        else:
            raise Exception("stock insuficiente")

    def to_dict(self):
        return {
            "id": self._id,
            "nombre": self._nombre,
            "categoria": self._categoria,
            "precio": self._precio,
            "rating": self._rating,
            "stock": self._stock,
            "consola": self._consola
        }


class juegops5(videojuego):
    pass


class juegoxbox(videojuego):
    pass


class juegonintendo(videojuego):
    pass
