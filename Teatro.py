from Evento import Evento

class Teatro(Evento):
    def __init__(self, nombre_evento, cartel, asientos, fecha, precio, tipo, sinopsis):
        Evento.__init__(self, nombre_evento, cartel, asientos, fecha, precio, tipo)

        self.__sinopsis = sinopsis

    def get_sinopsis(self):
        return self.__sinopsis
