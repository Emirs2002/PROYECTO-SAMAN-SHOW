class Cliente():
    def __init__(self, nombre, cedula, edad):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre
        
    def get_cedula(self):
        return self.__cedula

    def get_edad(self):
        return self.__edad