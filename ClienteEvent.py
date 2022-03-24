from Cliente import Cliente

class ClienteEvent(Cliente):
    def __init__(self, cedula, nombre, edad, entradas, evento, asientos):
        super().__init__(cedula)
    
        self.__nombre = nombre
        self.__edad = edad
        self.__entradas = entradas
        self.__evento = evento
        self.__asientos = asientos
 
    def get_nombre(self):
        return self.__nombre       
    
    def get_edad(self):
        return self.__edad

    def get_entradas(self):
        return self.__entradas

    def get_evento(self):
        return self.__evento

    def get_asientos(self):
        return self.__asientos

    def show_client_data(self):
        print(f'''Nombre: {self.get_nombre()}
            \nEdad: {self.get_edad()}
            \nCédula: {self.get_cedula()}
            \nEvento seleccionado: {self.get_evento()}
            \nNúmero de entradas: {self.get_entradas()}
            \nAsientos: {self.get_asientos()}''')
        




