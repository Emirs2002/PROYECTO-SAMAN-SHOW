from Producto import Producto

class Bebida(Producto):
    def __init__(self, nombre_producto, clasificacion, precio, cantidad):
        super().__init__(nombre_producto, clasificacion, precio, cantidad)

    def show_bebida(self):
        print(f'''-Nombre: {self.get_nombre_producto()}
                \n-Tipo: Bebida''')
        print("-Cantidad:")         
        print(f"*Pequeño: {self.get_cantidad()[0]}")
        print(f"*Mediano: {self.get_cantidad()[1]}")
        print(f"*Grande: {self.get_cantidad()[2]}")
        print("")
        print("-Precios:")                
        print(f"*Pequeño: ${self.get_precio()[0]}")
        print(f"*Mediano: ${self.get_precio()[1]}")
        print(f"*Grande: ${self.get_precio()[2]}")
    
    def delete_inventory_bebida(self, index, num):
        
        if index == 1:
            cantidad = int(self.get_cantidad()[0]) - num
            return cantidad

        if index == 2:
            cantidad = int(self.get_cantidad()[1]) - num
            return cantidad

        if index == 3:
            cantidad = int(self.get_cantidad()[2]) - num
            return cantidad
    
    def set_cantidad_bebida(self, index, nueva_cantidad):

        if index == 1:
            self.get_cantidad()[0] = nueva_cantidad
            
        if index == 2:
            self.get_cantidad()[1] = nueva_cantidad
            
        if index == 3:
            self.get_cantidad()[2] = nueva_cantidad
            

