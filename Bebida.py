from Producto import Producto

class Bebida(Producto):
    def __init__(self, nombre_producto, clasificacion, precio, tamanho):
        super().__init__(nombre_producto, clasificacion, precio)

        self.__tamanho = tamanho
    
    def get_tamanho(self):
        return self.__tamanho