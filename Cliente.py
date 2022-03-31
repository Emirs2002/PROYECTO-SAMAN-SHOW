class Cliente():
    def __init__(self, cedula, nombre, edad, dinero_pagado, feria):
        
        self.__cedula = cedula       
        self.__nombre = nombre
        self.__edad = edad
        self.__dinero_pagado = dinero_pagado      #Acumula el dinero que gasta el cliente entre la feria y la taquilla
        self.__feria = feria         #Booleano: indica si el cliente compró en la feria
        
 
    def get_nombre(self):
        return self.__nombre  

    def get_cedula(self):
        return self.__cedula     
    
    def get_edad(self):
        return self.__edad
    
    def get_dinero_pagado(self):
        return self.__dinero_pagado

    def set_dinero_pagado(self, new_dinero_pagado):
        self.__dinero_pagado = new_dinero_pagado
    
    def get_feria(self):           
        return self.__feria
    
    def set_feria(self, new_feria):
        self.__feria = new_feria

    def show_client_data(self):
        print(f'''-Nombre: {self.get_nombre()}
            \n-Edad: {self.get_edad()}
            \n-Cédula: {self.get_cedula()}''')


    

    