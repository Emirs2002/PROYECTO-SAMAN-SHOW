
from Cliente import Cliente
from tools import *
from Evento import Evento
from Musical import Musical
from Teatro import Teatro
from Cliente import Cliente
class Taquilla():
    def __init__(self, db):        
        self.__db = db

    def get_db(self):
        return self.__db

        ########### MÓDULO 1 ###########

    def show_events(self):         #Enseña todos los eventos en la base de datos  
        
        lista_events = self.__db

        print("")
        print("    ------------------EVENTOS-------------------     ")   #FIXME AÑADIR A CADA SUBCLASE EL ATRIBUTO SHOW
        print("")
        for eve in range(len(lista_events)):
            if lista_events[eve].get_disponibilidad() == True:
                print("")
                print(f" --------- Evento {eve+1} -----------")
                print("")
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
                        matrix(asiento[0], asiento[1], "G")

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
            elif lista_events[eve].get_disponibilidad() == False:
                print(f"-Nombre: {lista_events[eve].get_nombre_evento()}")
                print("")
                print("***** El evento se encuentra cerrado *****") 
                    
    
    ##### ABRIR O CERRAR EVENTOS ######
    
    def change_availability(self):
        
        lista_events = self.__db  

        evento = check_num("Selecciona el número del evento que desees cerrar:\n==>")
        evento = int(evento)

        op = check_op(1,2,"¿Está seguro de que desea proceder? \n1.-Sí \n2.-No \n==>")
        

        if op == 1:
            lista_events[evento-1].set_disponibilidad(False)
            return lista_events
        if op == 2:
            return lista_events


    ##### BUSCAR POR FILTROS #####

    def search_event(self, num):   #Busca el evento de acuerdo al filtro introducido por el usuario

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

        ###########   MÓDULO 2 - COMPRA DE TICKETS ###########

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
                continue
      
        tipo_asiento = check_op(1, 2,'''Seleccione el tipo de asiento que desea:
                            \n1.-General
                            \n2.-VIP
                            \n==>''')
        if tipo_asiento == 1:    #Asegurar que el número de tickets deseados no exceda el número de asientos del evento
            tickets = check_op(1, len(matriz_general),"Ingrese el número de tickets que desea comprar:\n-->")
        else:
            tickets = check_op(1, len(matriz_vip),"Ingrese el número de tickets que desea comprar:\n-->")
        tickets = int(tickets)

        print("")
        print("Elija los sientos que desee:")   
        print("")

        cont = 0    #esto es para asegurar que la persona escoja el número de asientos según la cantidad de tickets
        
                            ######SELECCIÓN DE ASIENTOS#####  #FIXME SOLO FUNCIONA PARA UN EVENTO
        
        asientos= []       #Lista de asientos del cliente                  
        
        while tickets > cont:      

            if tipo_asiento == 1:      
                asiento = check_num('''Ingrese el número del asiento (Ejemplo: G10. Ingresar '10'):
                                \n==>''')  
                asiento = int(asiento) 
                if len(lista_asiento) == 0:
                    asientos.append(matriz_general[asiento-1])    
                    lista_asiento.append(matriz_general[asiento-1])   #Lista de asientos ocupados en general
                    cont += 1 
                else:
                    for spot in range(len(lista_asiento)):
                        if lista_asiento[spot] == matriz_general[asiento-1]:
                            print("El asiento seleccionado ya se encuentra ocupado")                

                        else:
                            asientos.append(matriz_general[asiento-1])    
                            lista_asiento.append(matriz_general[asiento-1])  
                            cont += 1
                            break

            elif tipo_asiento == 2:   
                asiento = check_num('''Ingrese el número del asiento (Ejemplo: V1-2. Ingresar '1-2'):
                                \n==>''')
                asiento = int(asiento) 
                if len(lista_asiento) == 0:
                    asientos.append(matriz_vip[asiento-1])    
                    lista_asiento.append(matriz_vip[asiento-1])  
                    cont += 1 
                else:
                    for spot in range(len(lista_asiento)):
                        if lista_asiento[spot] == matriz_vip[asiento-1]:
                            print("El asiento seleccionado ya se encuentra ocupado")                

                        else:
                            asientos.append(matriz_vip[asiento-1])    
                            lista_asiento.append(matriz_vip[asiento-1])  
                            cont += 1
                            break

        client = Cliente(cedula = cedula, nombre = name, edad = age, entradas = tickets, evento = evento, asientos = asientos)


        ###### CALCULAR COSTOS ######
        

        for eve in range(len(lista_events.get_db())):
                if lista_events.get_db()[eve].get_nombre_evento() == evento:
                    precios = lista_events.get_db()[eve].get_precio()
                                

                    if tipo_asiento == 1:           #IF VAMPIRE == TRUE 
                        iva = (precios[0]*tickets)*0.16        #Calcular el IVA para el precio general
                        subtotal = precios[0]*tickets
                        costo = (precios[0]*tickets)+iva
                        
                    elif tipo_asiento == 2:
                        iva = (precios[1]*tickets)*0.16             #Calcular el IVA para el precio VIP
                        subtotal = precios[1]*tickets
                        costo = (precios[1]*tickets)+iva
                        
    
            ###### MOSTRAR FACTURA #######        #NOTE agregar descuento luego
       
        print("********* FACTURA ***********")

        print("*Datos de compra:")
        client.show_client_data()
        print("-------")
        for event in range(client.get_entradas()):
            print(f"->1 Entrada {client.get_evento()}      ${subtotal/client.get_entradas()}" )
        print("")
        print(f"*Subtotal: ${subtotal}")
        #print("-------")
        #print(f"*Descuento: -{descuento}")
        print("-------")
        print(f"*IVA: +{iva}")
        print("-------")
        print(f"*Monto total: ${costo}")
                        
        #### Preguntar al usuario si desea pagar ####

        op = check_op(1,2,"¿Desea proceder con el pago? \n1.-Sí \n2.-No \n==>")

        if op == 1:

            #load_db("asientos_ocupados.txt", lista_asiento)  #carga asientos seleccionados a la lista grande
            
            return client    #Si la respuesta es "sí" se devuelve el objeto con la información
            

        if op == 2:
            
            return -1       #Si la respuesta es "no" se devuelve -1 

           