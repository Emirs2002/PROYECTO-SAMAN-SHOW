from Producto import Producto

class Alimento(Producto):
    def __init__(self, nombre_producto, clasificacion, precio, cantidad, vendido, presentacion):
        super().__init__(nombre_producto, clasificacion, precio, cantidad, vendido)

        self.__presentacion = presentacion

    def get_presentacion(self):
        return self.__presentacion

    def show_alimento(self):
        print(f'''-Nombre: {self.get_nombre_producto()}
                \n-Tipo: Alimento
                \n-Cantidad: {self.get_cantidad()}
                \n-Precio: ${self.get_precio()}''')
        print("")
        print("-Presentación: ", end="")        
        if self.get_presentacion() == 1:
            print("Preparación")
        elif self.get_presentacion() == 2:
            print("Empaque")