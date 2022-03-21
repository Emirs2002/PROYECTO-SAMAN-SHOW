
from ClienteEvent import ClienteEvent
from tools import *
from Evento import *
class Taquilla():
    def __init__(self, db):        
        self.__db = db

    def get_db(self):
        return self.__db

    def show_events(self):         #Enseña todos los eventos en la base de datos  
        
        lista_events = self.__db

        print("")
        print("    ------------------EVENTOS-------------------     ")
        print("")
        for eve in range(len(lista_events)):
            
            print(f'''-Nombre: {lista_events[eve].get_nombre_evento()}
                    \n-Fecha: {lista_events[eve].get_fecha()}''')
                    
            if lista_events[eve].get_tipo() == 1:
                print("-Tipo: Musical")
                print(f"-Bandas: {lista_events[eve].get_num_bandas()}")

            elif lista_events[eve].get_tipo() == 2:
                print("-Tipo: Obra de teatro")
                print(f"-Sinopsis: {lista_events[eve].get_sinopsis()}")

            print("")
            print("-Cartel:")
            for cart in range(len(lista_events[eve].get_cartel())):
                print(f"--> {lista_events[eve].get_cartel()[cart]}")

            print("")
            print("-Asientos:")               #ANCHOR Dejar así por ahora
            layout = lista_events[eve].get_asientos()
            for tipo, asiento in layout.items():
                if tipo == "general":
                    print("")
                    print("*General:") 
                    print(matrix(asiento[0], asiento[1], "G"))  

                elif tipo == "vip":
                    print("")
                    print("*VIP:") 
                    matrix(asiento[0], asiento[1], "V")   
        
            print("")
            print("-Precios:")
            print(f"*General: ${lista_events[eve].get_precio()[0]}")
            print(f"*VIP: ${lista_events[eve].get_precio()[1]}")    

            print("")
            print("-----------------------------------------------------")
            print("") 
        
    def search_event(self, num): #Busca el evento de acuerdo al filtro introducido por el usuario

        lista_events = self.__db                   
                                
                                #NOTE COMENTAR TODA ESTA PARTE DEL CÓDIGO

    #########   T I P O   ########  

        if num == 1: 
            lista_tipo = []
            op = check_op(1, 2, '''Seleccione el tipo de evento:
                                \n1.-Musical
                                \n2.-Obra de teatro\n-->''')
            print("Resultados de su búsqueda:")
            for event in range(len(lista_events)): 
                if lista_events[event].get_tipo() == op: 
                    lista_tipo.append(lista_events[event])
                else:
                    continue
            
            return lista_tipo
                    

    #######   F E C H A   #######     
        if num == 2: 
            lista_fecha = []
            mes = check_num("Ingrese el mes del evento (Intoducir dos dígitos. Ejemplo: abril = '04'):\n==>")
            
            mes = str(mes)

            for event in range(len(lista_events)): 

                lista = lista_events[event].get_fecha().split("-")

                for fecha in range(len(lista)-1):       
                    if lista[fecha] == mes:
                        lista_fecha.append(lista_events[event])
            
            return lista_fecha

    #######  ACTOR O CANTANTE   #######   
        if num == 3: 
            lista_performer = []

            op_performer = check_let('''Ingrese el nombre del actor o cantante:   
                                \n==>''')  
            for event in range(len(lista_events)):               
                for performer in range(len(lista_events[event].get_cartel())):
                    if lista_events[event].get_cartel()[performer] == op_performer:
                        lista_performer.append(lista_events[event])

            return lista_performer

    ########### N O M B R E ##########   

        if num == 4:
            lista_nombre = []             
            
            op_nom = check_let('''Ingrese el nombre del evento que desea buscar:   
                                \n==>''')  
         
            for event in range(len(lista_events)): 
                if lista_events[event].get_nombre_evento() == op_nom:                    
                    lista_nombre.append(lista_events[event])  
            
            return lista_nombre

            ########   MÓDULO 2 - COMPRA DE TICKETS ###########

    def comprar_tickets(self, lista_events, lista_asiento):
        
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
        
                  #NOTE CONFIGURAR LOS ASIENTOS OCUPADOS (comparar elementos de una lista con el asiento escogido por el usuario)
        asientos= []                        #FIXME arreglar código con lista cargada
       
        while tickets > cont:

            if tipo_asiento == 1:      
                asiento = check_num('''Ingrese el número del asiento (Ejemplo: G1-8. Ingresar '1-8'):
                                \n==>''')
                multi_num = asiento.split("-")                
                multi = int(multi_num[0]) * int(multi_num[1]) 
                asientos.append(matriz_general[multi-1])    #atributo cliente
                lista_asiento.append(matriz_general[multi-1])  #lista general de asientos ocupados
                cont += 1

            elif tipo_asiento == 2:
                asiento = check_num('''Ingrese el número del asiento (Ejemplo: V1-2. Ingresar '1-2'):
                                \n==>''')
                multi_num = asiento.split("-")                
                multi = int(multi_num[0]) * int(multi_num[1])
                asientos.append(matriz_vip[multi-1])  
                lista_asiento.append(matriz_vip[multi-1])

                cont += 1

        load_db("asientos_ocupados.txt", lista_asiento)

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
        
            
