from Cliente import Cliente

class ClienteEvent(Cliente):
    def __init__(self, cedula, nombre, edad, entradas, evento):
        super().__init__(cedula)
    
        self.__nombre = nombre
        self.__edad = edad
        self.__entradas = entradas
        self.__evento = evento
 
    def get_nombre(self):
        return self.__nombre       
    
    def get_edad(self):
        return self.__edad

    def get_entradas(self):
        return self.__entradas

    def get_evento(self):
        return self.__evento