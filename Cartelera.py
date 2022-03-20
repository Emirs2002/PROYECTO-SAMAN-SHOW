from Musical import Musical
from Teatro import Teatro
from tools import *

class Cartelera():
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
            print("-Asientos:")               #Modificar esta parte. Que muestre mejor cantidad de asientos
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
                    

    #######   F E C H A   #######     #FIXME NO ES SOLAMENTE POR MES, TAMBIÉN TOMA EL DÍA
        if num == 2: 
            lista_fecha = []
            mes = check_num("Ingrese el mes del evento (Intoducir dos dígitos. Ejemplo: abril = '04'):\n==>")
            
            mes = str(mes)

            for event in range(len(lista_events)): 

                lista = lista_events[event].get_fecha().split("-")

                for fecha in range(len(lista)):
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


        

            
            
            