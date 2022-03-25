class Evento():
    def __init__(self, nombre_evento, cartel, asientos_general, asientos_vip, fecha, precio, tipo, disponibilidad):
        self.__nombre_evento = nombre_evento
        self.__cartel = cartel
        self.__asientos_general = asientos_general
        self.__asientos_vip = asientos_vip
        self.__fecha = fecha                        
        self.__precio = precio
        self.__tipo = tipo
        self.__disponibilidad = disponibilidad
    
    def get_nombre_evento(self):
        return self.__nombre_evento
    
    def get_cartel(self):
        return self.__cartel
    
    def get_asientos_general(self):
        return self.__asientos_general

    def set_asientos_general(self, new_asientos):
        self.__asientos_general = new_asientos
    
    def get_asientos_vip(self):
        return self.__asientos_vip

    def set_asientos_vip(self, new_asientos):
        self.__asientos_vip = new_asientos
    
    def get_fecha(self):
        return self.__fecha

    def get_precio(self):
        return self.__precio

    def get_tipo(self):
        return self.__tipo

    def get_disponibilidad(self):
        return self.__disponibilidad
    
    def set_disponibilidad(self, new_disponibilidad):
        self.__disponibilidad = new_disponibilidad

    



   