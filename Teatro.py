from Evento import Evento


class Teatro(Evento):
    def __init__(self, nombre_evento, cartel,asientos_general, asientos_vip, fecha, precio, tipo, disponibilidad, sinopsis):
        Evento.__init__(self, nombre_evento, cartel, asientos_general, asientos_vip, fecha, precio, tipo, disponibilidad)

        self.__sinopsis = sinopsis

    def get_sinopsis(self):
        return self.__sinopsis

       

        
