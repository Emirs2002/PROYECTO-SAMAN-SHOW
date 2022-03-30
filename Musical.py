from Evento import Evento


class Musical(Evento):
    def __init__(self, nombre_evento, cartel, asientos_general, asientos_vip, fecha, precio, tipo, disponibilidad, ingreso, num_bandas):
        
        Evento.__init__(self, nombre_evento, cartel, asientos_general, asientos_vip, fecha, precio, tipo, disponibilidad, ingreso)

        self.__num_bandas = num_bandas

    def get_num_bandas(self):
        return self.__num_bandas

    def show_musical(self):
        print(f'''-Nombre: {self.get_nombre_evento()}
            \n-Fecha: {self.get_fecha()}
            \n-Tipo: Musical
            \n-Bandas: {self.get_num_bandas()}''')
     
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
    
   