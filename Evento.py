class Evento():
    def __init__(self, nombre_evento, cartel, asientos, fecha, precio, tipo):
        self.__nombre_evento = nombre_evento
        self.__cartel = cartel
        self.__asientos = asientos
        self.__fecha = fecha
        self.__precio = precio
        self.__tipo = tipo
    
    def get_nombre_evento(self):
        return self.__nombre_evento
    
    def get_cartel(self):
        return self.__cartel
    
    def get_asientos(self):
        return self.__asientos

    def set_asientos(self, new_asientos):
        self.__asientos = new_asientos
    
    def get_fecha(self):
        return self.__fecha

    def get_precio(self):
        return self.__precio

    def get_tipo(self):
        return self.__tipo


   