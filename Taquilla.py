
from Cliente import Cliente
from tools import *
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
        print("    ------------------EVENTOS-------------------     ")   
        print("")
        for eve in range(len(lista_events)):
            evento = lista_events[eve]
            print("")
            print(f" --------- Evento {eve+1} -----------")
            print("")
            if evento.get_disponibilidad() == True:     #de estar abiertos, se muestran
                if evento.get_tipo() == 1:
                    evento.show_musical()
                elif evento.get_tipo() == 2:
                    evento.show_teatro()
                print("")
                print("-----------------------------------------------------")
                print("") 

            elif evento.get_disponibilidad() == False:

                print(f"-Nombre: {lista_events[eve].get_nombre_evento()}")
                print("")
                print("***** El evento se encuentra cerrado *****")

                print("")
                print("-----------------------------------------------------")
                print("")  
           
                        
    
    ##### ABRIR O CERRAR EVENTOS ######
    
    def change_availability(self):
        
        lista_events = self.__db  

        op = check_op(1,3, "Seleccione la opción que desea ejecutar: \n1.-Aperturar \n2.-Cerrar \n3.-Volver\n==>")
        
        if op == 1:

            evento = check_num("Ingrese el número del evento que desee abrir:\n==>")
            evento = int(evento)

            op = check_op(1,2,"¿Está seguro de que desea proceder? \n1.-Sí \n2.-No \n==>")
        
            if op == 1:
                lista_events[evento-1].set_disponibilidad(True)
                return lista_events
            if op == 2:
                return lista_events
        
        if op == 2:
            
            evento = check_num("Ingrese el número del evento que desees cerrar:\n==>")
            evento = int(evento)

            op = check_op(1,2,"¿Está seguro de que desea proceder? \n1.-Sí \n2.-No \n==>")
        
            if op == 1:
                lista_events[evento-1].set_disponibilidad(False)
                return lista_events
            if op == 2:
                return lista_events
        
        if op == 3:
            pass


    ##### BUSCAR POR FILTROS #####

    def search_event(self, num):   #Busca el evento de acuerdo al filtro introducido por el usuario

        lista_events = self.__db                   
                                

    #########   T I P O   ########  

        if num == 1: 
            lista_tipo = []
            op = check_op(1, 2, '''Seleccione el tipo de evento:
                                \n1.-Musical
                                \n2.-Obra de teatro\n-->''')
            print("Resultados de su búsqueda:")
            for event in range(len(lista_events)):
                evento = lista_events[event]
                if evento.get_tipo() == op: 
                    lista_tipo.append(evento)   #se busca el objeto por el nombre, si se encuentra se añade a la lista vacía
                else:
                    continue
            
            return lista_tipo       #de encontrarse, devuelve la lista con el objeto, sino devuelve la lista vacía
                    

    #######   F E C H A   #######     
        if num == 2: 
            lista_fecha = []       

            year = check_num("Ingrese el año del evento:\n==>")
            year = str(year)

            mes = check_num("Ingrese el mes del evento (Intoducir dos dígitos. Ejemplo: abril = '04'):\n==>")
            
            mes = str(mes)
            
            for event in range(len(lista_events)): 
                evento = lista_events[event]
                lista = evento.get_fecha().split("-")       #se crea una lista donde en el índice 0 está el añor y en el índice 1 está el mes
                
                if lista[0] == year and lista[1] == mes:        
                    lista_fecha.append(evento)
            
            return lista_fecha

    #######  ACTOR O CANTANTE   #######   
        if num == 3: 
            lista_performer = []

            op_performer = check_let('''Ingrese el nombre del actor o cantante:   
                                \n==>''').lower().capitalize()  
            for event in range(len(lista_events)):
                evento = lista_events[event]

                for performer in range(len(evento.get_cartel())):
                    if evento.get_cartel()[performer].lower().capitalize() == op_performer:
                        lista_performer.append(evento)

            return lista_performer

    ########### N O M B R E ##########   

        if num == 4:
            lista_nombre = []             
            
            op_nom = check_let('''Ingrese el nombre del evento que desea buscar:   
                                \n==>''').lower().capitalize()  
         
            for event in range(len(lista_events)): 
                evento = lista_events[event]
                if evento.get_nombre_evento().lower().capitalize() == op_nom:                    
                    lista_nombre.append(evento)  
            
            return lista_nombre


        ###########   MÓDULO 2  ###########


    def comprar_tickets(self, lista_events):            

        # Se pide datos personales del cliente # 
        
        name = check_let("Ingrese su nombre:\n-->").lower().capitalize()
        
        cedula = check_num("Ingrese su cédula:\n-->")
        
        age = check_num("Ingrese su edad:\n-->")        

        lista_events.show_events()      

        ### Enseñar los asientos del evento que ingrese el cliente ###  
        
        inside_db = False
        while inside_db == False:

            evento_escogido = check_let("Ingrese el nombre del evento que desea comprar:\n-->").lower().capitalize()
            
            lista = lista_events.get_db()
            for eve in range(len(lista)):
                evento = lista[eve]
                if evento.get_nombre_evento().lower().capitalize() == evento_escogido and evento.get_disponibilidad() == True:  #si se encuentra en la lista y está abierto, se muestran los asientos
                    inside_db = True
                    print(f'''-Asientos:''') 
                    evento.show_asientos()

                    matriz_general = evento.get_asientos_general()      #se guardan las matrices en sus respectivas variables para poder modificarlas
                    matriz_vip = evento.get_asientos_vip()
                                        
            if inside_db == False: 
                print("Error, el nombre que ha ingresado no se encuentra en la base de datos.Intente nuevamente.")
                continue
      
        tipo_asiento = check_op(1, 2,'''Seleccione el tipo de asiento que desea:
                            \n1.-General
                            \n2.-VIP
                            \n==>''')
        
        
        tickets = check_num("Ingrese el número de tickets que desea comprar:\n-->")
        tickets = int(tickets)

        print("")
        print("Elija los sientos que desee:")   
        print("")

        cont = 0    #esto es para asegurar que la persona escoja el número de asientos según la cantidad de tickets
        
                            ######      SELECCIÓN DE ASIENTOS       #####  
        
        asientos= []       #Lista de asientos del cliente                  
        while tickets > cont:   

                # ASIENTOS GENERAL

            if tipo_asiento == 1:      
                asiento = input('''Ingrese el asiento que desea (Ejemplo: A6. Ingresar 'A6'):
                                \n==>''')  
                inside_asiento = False
                for fila in range(len(matriz_general)):
                    for spot in range(len(matriz_general[fila])):
                        if matriz_general[fila][spot] == asiento:
                            inside_asiento = True
                            asientos.append(matriz_general[fila][spot])    #Al elegir los asientos, estos se cambian por una X
                            matriz_general[fila][spot] = "X"
                            cont += 1

                if inside_asiento == False:   #De no encontrarse el asiento ingresado pro el usuario
                    print("El asiento está ocupado. Ingrese otro.")
                    
            # ASIENTOS VIP
        
            elif tipo_asiento == 2:   
                asiento = input('''Ingrese el asiento que desea (Ejemplo: A1. Ingresar 'A1'):
                                \n==>''')

                inside_asiento = False
                for fila in range(len(matriz_vip)):
                    for spot in range(len(matriz_vip[fila])):
                        if matriz_vip[fila][spot] == asiento:
                            inside_asiento = True
                            asientos.append(matriz_vip[fila][spot])
                            matriz_vip[fila][spot] = "X"
                            cont += 1

                if inside_asiento == False:   
                    print("El asiento está ocupado. Ingrese otro.")

        

        ###### CALCULAR COSTOS ######
        
        for eve in range(len(lista)):
                if lista[eve].get_nombre_evento().lower().capitalize() == evento_escogido:
                    precios = lista[eve].get_precio()
                                

                    if tipo_asiento == 1:          
                        iva = (precios[0]*tickets)*0.16        #Calcular el IVA para el precio general
                        subtotal = precios[0]*tickets
                        costo = (precios[0]*tickets)+iva
                        
                    elif tipo_asiento == 2:
                        iva = (precios[1]*tickets)*0.16             #Calcular el IVA para el precio VIP
                        subtotal = precios[1]*tickets
                        costo = (precios[1]*tickets)+iva
                        
        client = Cliente(cedula = cedula, nombre = name, edad = age, dinero_pagado = costo, feria = False)   #Asignar atributos al cliente


            ###### MOSTRAR FACTURA #######        
       
        print("********* FACTURA ***********")

        print("*Datos de compra:")
        client.show_client_data()
        print("")
        print(f'''-Número de entradas: {tickets}
                \n-Asientos: {asientos}''')
        print("-------")
        for event in range(tickets):
            print(f"->1 Entrada {evento_escogido}     ${subtotal/tickets}" )
        print("")
        print(f"*Subtotal: ${subtotal}")
        print("-------")
        print(f"*IVA: +{iva}")
        print("-------")
        print(f"*Monto total: ${costo}")
                        
        #### Preguntar al usuario si desea pagar ####

        op = check_op(1,2,"¿Desea proceder con el pago? \n1.-Sí \n2.-No \n==>")

        if op == 1:

            ## SE APLICAN CAMBIOS A LAS LISTAS DE ASIENTOS DEL EVENTO ## 

            for eve in range(len(lista)):
                evento = lista[eve]
                if evento.get_nombre_evento().lower().capitalize() == evento_escogido:
                    if tipo_asiento == 1:
                        evento.set_asientos_general(matriz_general)
                    else:
                        evento.set_asientos_vip(matriz_vip)

            ## ADICIONAR EL COSTE TOTAL AL ATRIBUTO INGRESO DEL EVENTO ##

            for eve in range(len(lista)):
                evento_obj = lista[eve]
                if evento_obj.get_nombre_evento().lower().capitalize() == evento_escogido:
                    evento_obj.set_ingreso(costo)
                    break
            
            #  RETORNAR VALORES  #

            return client, evento_obj, evento_escogido, lista    #Si la respuesta es "sí" se devuelve el objeto con la información y los contadores
            

        if op == 2:
            
            return -1       #Si la respuesta es "no" se devuelve -1 

           