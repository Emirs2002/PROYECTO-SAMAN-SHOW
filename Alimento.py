from Producto import Producto

class Alimento(Producto):
    def __init__(self, nombre_producto, clasificacion, precio, cantidad, presentacion):
        super().__init__(nombre_producto, clasificacion, precio, cantidad)

        self.__presentacion = presentacion

    def get_presentacion(self):
        return self.__presentacion