class carrito:
    def __init__(self):
        self.items = []

    def agregar(self, juego, cantidad):
        if juego.stock < cantidad:
            raise Exception("sin stock")

        juego.reducir_stock(cantidad)

        self.items.append({
            "juego": juego,
            "cantidad": cantidad
        })

    def eliminar(self, id):
        self.items = [i for i in self.items if i["juego"].id != id]

    def mostrar(self):
        total = 0
        for i in self.items:
            subtotal = i["cantidad"] * i["juego"].precio
            total += subtotal
            print(i["juego"].nombre, i["cantidad"], subtotal)
        print("total:", total)

    def total(self):
        return sum(i["cantidad"] * i["juego"].precio for i in self.items)
