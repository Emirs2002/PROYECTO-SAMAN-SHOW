from Producto import Producto

class Bebida(Producto):
    def __init__(self, nombre_producto, clasificacion, precio, cantidad):
        super().__init__(nombre_producto, clasificacion, precio, cantidad)

    def show_bebida(self):
        print(f'''-Nombre: {self.get_nombre_producto()}
                \n-Tipo: Bebida''')
        print("-Cantidad:") 
        print(f"*Pequeño: {int(self.get_cantidad())//3}")
        print(f"*Mediano: {int(self.get_cantidad())//3}")
        print(f"*Grande: {int(self.get_cantidad())//3}")
        print("")
        print("-Precios:")                
        print(f"*Pequeño: ${self.get_precio()[0]}")
        print(f"*Mediano: ${self.get_precio()[1]}")
        print(f"*Grande: ${self.get_precio()[2]}")
