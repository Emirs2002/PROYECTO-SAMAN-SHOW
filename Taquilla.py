from Cartelera import Cartelera
from Cliente import Cliente
from tools import *
from Evento import *
class Taquilla():
    def __init__(self, clientes):        
        self.__clientes = clientes

    def get_clientes(self):
        return self.__clientes

    def comprar_tickets(self, lista_events):
        
        name = check_let("Ingrese su nombre:\n-->")
        
        cedula = check_num("Ingrese su cédula:\n-->")
        
        age = check_num("Ingrese su edad:\n-->")        

        lista_events.show_events()        

       
        ### Enseñar los asientos del evento que ingrese el cliente ###  
        
         #NOTE FUNCIONA GENIAL ESTE

        inside_db = False
        while inside_db == False:

            evento = check_let("Ingrese el nombre del evento que desea comprar:\n-->")

            for eve in range(len(lista_events.get_db())):
                if lista_events.get_db()[eve].get_nombre_evento() == evento:
                    inside_db = True
                    layout = lista_events.get_db()[eve].get_asientos()
                    for tipo, asiento in layout.items():
                        if tipo == "general":
                            print("")
                            print("*General:") 
                            matrix(asiento[0], asiento[1], "G")   #Se llama a la función matrix para enseñar los puestos libres en general

                        elif tipo == "vip":
                            print("")
                            print("*VIP:") 
                            matrix(asiento[0], asiento[1], "V")    #Se llama a la función matrix para enseñar los puestos libres en VIP

            if inside_db == False: 
                print("Error, el nombre que ha ingresado no se encuentra en la base de datos.Intente nuevamente.")
        
        tickets = check_num("Ingrese el número de tickets que desea comprar:\n-->")

        print("")
        print("Elija los sientos que desee:")   #FIXME ELEGIR PUESTOS
        print("")

    #    cont = 0    #esto es para asegurar que la persona escoja el número de asientos según la cantidad de tickets
    #    asiento = []
    #    while tickets > cont:
    #        tipo_asiento = check_let('''Seleccione el tipo de asiento que desea:
    #                        \n1.-General
    #                        \n2.-VIP''')
    #        
    #        asiento = check_num('''Ingrese el número del asiento:
    #                            \n==>''')
    #        if 
    #        cont += 1
    #        pass