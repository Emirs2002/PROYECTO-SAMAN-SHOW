from Producto import Producto

class Bebida(Producto):
    def __init__(self, nombre_producto, clasificacion, precio, cantidad):
        super().__init__(nombre_producto, clasificacion, precio, cantidad)

        