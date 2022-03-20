from Cartelera import Cartelera
from ClienteEvent import ClienteEvent
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
        
        matriz_general = []
        matriz_vip = []
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
                            matrix(asiento[0], asiento[1], "G")   #Se llama a la función matrix para enseñar los puestos en general
                            
                            for x in range(1, (asiento[0]*asiento[1])+1):   #Guarda los asientos generales en una lista
                                matriz_general.append(f"G{x}")

                        elif tipo == "vip":
                            print("")
                            print("*VIP:") 
                            matrix(asiento[0], asiento[1], "V")    #Se llama a la función matrix para enseñar los puestos libres en VIP
                            
                            for x in range(1, (asiento[0]*asiento[1])+1):    #Guarda los asientos vip en una lista
                                 matriz_vip.append(f"V{x}")
                           

            if inside_db == False: 
                print("Error, el nombre que ha ingresado no se encuentra en la base de datos.Intente nuevamente.")
      
        tipo_asiento = check_op(1, 2,'''Seleccione el tipo de asiento que desea:
                            \n1.-General
                            \n2.-VIP
                            \n==>''')
        if tipo_asiento == 1:    #Asegurar que el número de tickets deseados no exceda el número de asientos del evento
            tickets = check_op(1, len(matriz_general),"Ingrese el número de tickets que desea comprar:\n-->")
        else:
            tickets = check_op(1, len(matriz_vip),"Ingrese el número de tickets que desea comprar:\n-->")

        print("")
        print("Elija los sientos que desee:")   
        print("")

        cont = 0    #esto es para asegurar que la persona escoja el número de asientos según la cantidad de tickets
        
        lista_asiento = []          #NOTE CONFIGURAR LOS ASIENTOS OCUPADOS (comparar elementos de una lista con el asiento escogido por el usuario)
                                    #FIXME lista_asiento siempre será vacía si se deja aquí adentro
        while tickets > cont:

            if tipo_asiento == 1:      
                asiento = check_num('''Ingrese el número del asiento (Ejemplo: G1-8. Ingresar '1-8'):
                                \n==>''')
                multi_num = asiento.split("-")                
                multi = int(multi_num[0]) * int(multi_num[1])  
                lista_asiento.append(matriz_general[multi-1])
                cont += 1

            elif tipo_asiento == 2:
                asiento = check_num('''Ingrese el número del asiento (Ejemplo: V1-2. Ingresar '1-2'):
                                \n==>''')
                multi_num = asiento.split("-")                
                multi = int(multi_num[0]) * int(multi_num[1])  
                lista_asiento.append(matriz_vip[multi-1])

                cont += 1

        ###### MOSTRAR COSTOS #######

        for eve in range(len(lista_events.get_db())):
                if lista_events.get_db()[eve].get_nombre_evento() == evento:
                    precios = lista_events.get_db()[eve].get_precio()
                                

                    if tipo_asiento == 1:           #IF VAMPIRE == TRUE 
                        iva = (precios[0]*tickets)*0.16        #Calcular el IVA para el precio general
                        print(f"*Costo: ${(precios[0]*tickets)+iva}")

                    elif tipo_asiento == 2:
                        iva = (precios[1]*tickets)*0.16             #Calcular el IVA para el precio VIP
                        print(f"*Costo: ${(precios[1]*tickets)+iva}")

            
