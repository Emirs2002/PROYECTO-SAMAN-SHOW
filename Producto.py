class Producto():
    def __init__(self, nombre_producto, clasificacion, precio, cantidad, vendido):
        self.__nombre_producto = nombre_producto
        self.__clasificacion = clasificacion
        self.__precio = precio
        self.__cantidad = cantidad
        self.__vendido = vendido

    def get_nombre_producto(self):
        return self.__nombre_producto

    def get_precio(self):
        return self.__precio

    def get_clasificacion(self):
        return self.__clasificacion

    def get_cantidad(self):
        return self.__cantidad
    
    def set_cantidad(self, new_cantidad):
        self.__cantidad = new_cantidad
    
    def get_vendido(self):
        return self.__vendido

    def set_vendido(self, new_vendido):
        self.__vendido = new_vendido

    def delete_inventory(self, num):

        cantidad = int(self.get_cantidad()) - num

        return cantidad