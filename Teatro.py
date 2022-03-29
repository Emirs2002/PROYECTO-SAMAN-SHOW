from Evento import Evento


class Teatro(Evento):
    def __init__(self, nombre_evento, cartel,asientos_general, asientos_vip, fecha, precio, tipo, disponibilidad, sinopsis):
        Evento.__init__(self, nombre_evento, cartel, asientos_general, asientos_vip, fecha, precio, tipo, disponibilidad)

        self.__sinopsis = sinopsis

    def get_sinopsis(self):
        return self.__sinopsis

    def show_teatro(self):
        print(f'''-Nombre: {self.get_nombre_evento()}
            \n-Fecha: {self.get_fecha()}
            \n-Tipo: Obra de teatro
            \n-Sinopsis: {self.get_sinopsis()}''')
     
        print("")
        print("-Cartel:")
        for cart in range(len(self.get_cartel())):
            print(f"--> {self.get_cartel()[cart]}")

        print("")
        print("Asientos:")
        self.show_asientos()

        print("")
        print("-Precios:")
        print(f"*General: ${self.get_precio()[0]}")
        print(f"*VIP: ${self.get_precio()[1]}")    


        
