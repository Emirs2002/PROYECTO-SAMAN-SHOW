from Evento import Evento


class Musical(Evento):
    def __init__(self, nombre_evento, cartel, asientos_general, asientos_vip, fecha, precio, tipo, disponibilidad, num_bandas):
        
        Evento.__init__(self, nombre_evento, cartel, asientos_general, asientos_vip, fecha, precio, tipo, disponibilidad)

        self.__num_bandas = num_bandas

    def get_num_bandas(self):
        return self.__num_bandas

    
   