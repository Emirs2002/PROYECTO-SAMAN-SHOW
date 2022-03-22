class Producto():
    def __init__(self, nombre_producto, clasificacion, precio):
        self.__nombre_producto = nombre_producto
        self.__clasificacion = clasificacion
        self.__precio = precio

    def get_nombre_producto(self):
        return self.__nombre_producto

    def get_precio(self):
        return self.__precio

    def get_clasificacion(self):
        return self.__clasificacion