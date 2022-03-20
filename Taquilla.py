from Musical import Musical
from Teatro import Teatro
from tools import *

class Taquilla():
    def __init__(self, db):
        self.__db = db
    
    def get_db(self):
        return self.__db

    #ANCHOR FUNCIONA PERFECTAMENTE

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
            print("-Asientos:")             
            layout = lista_events[eve].get_asientos()
            for tipo, asiento in layout.items():
                if tipo == "general":
                    print("")
                    print("*General:") 
                    matrix(asiento[0], asiento[1], "G")    #Se llama a la función matrix para enseñar los puestos libres en general

                elif tipo == "vip":
                    print("")
                    print("*VIP:") 
                    matrix(asiento[0], asiento[1], "V")     #Se llama a la función matrix para enseñar los puestos libres en VIP
        
            print("")
            print("-Precios:")
            print(f"*General: ${lista_events[eve].get_precio()[0]}")
            print(f"*VIP: ${lista_events[eve].get_precio()[1]}")    

            print("")
            print("-----------------------------------------------------")
            print("") 
        
    def search_event(self, num): #Busca el evento de acuerdo al filtro introducido por el usuario

        lista_events = self.__db

    #########    T I P O   ########
    
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
            pass


    #######  ACTOR O CANTANTE   #######  
        if num == 3: 
            pass


    ########### N O M B R E ##########   #REVIEW ver si se puede utilizar show eventos en vez de copiar todo otra vez
        if num == 4:
            
            op_nom = check_let("Ingrese el nombre del evento que desea buscar:\n==>")  

            inside_lista = False
            for event in range(len(lista_events)): 
                if lista_events[event].get_nombre_evento() == op_nom:
                    inside_lista = True
                    break  
                
            if inside_lista == False:
                print("Ha ingresado un nombre inválido, intente nuevamente.")

            elif inside_lista == True:
                print("")
                print(f'''-Nombre: {lista_events[event].get_nombre_evento()}
                        \n-Fecha: {lista_events[event].get_fecha()}''')
                print("")
                for cart in range(len(lista_events[event].get_cartel())):
                    print(f"--> {lista_events[event].get_cartel()[cart]}")
                print("")
                print("-Precios:")
                print(f"*General: ${lista_events[event].get_precio()[0]}")
                print(f"*VIP: ${lista_events[event].get_precio()[1]}")    
                
            


        

            
            
            