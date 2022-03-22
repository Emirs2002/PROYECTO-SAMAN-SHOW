from Producto import Producto

class Alimento(Producto):
    def __init__(self, nombre_producto, clasificacion, precio, tipo):
        super().__init__(nombre_producto, clasificacion, precio)

        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo