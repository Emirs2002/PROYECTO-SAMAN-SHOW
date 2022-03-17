
from calendar import c
from Musical import Musical
from Teatro import Teatro
from tools import *

######### Mostrar todos los eventos######### 

def assign_events(db, lista_events):
    
    #Añadir los elementos del JSON a los objetos Musical y Teatro respectivamente

    for event in range(len(db["events"])):        
        if db["events"][event]["type"] == 1:
            musical_obj = Musical(nombre_evento = db["events"][event]["title"], cartel = db["events"][event]["cartel"], asientos = db["events"][event]["layout"], fecha = db["events"][event]["date"], num_bandas = db["events"][event]["bands"], precio = db["events"][event]["prices"], tipo = db["events"][event]["type"])
            lista_events.append(musical_obj)
            

        elif db["events"][event]["type"] == 2:
            teatro_obj = Teatro(nombre_evento = db["events"][event]["title"], cartel =db["events"][event]["cartel"], asientos = db["events"][event]["layout"], fecha = db["events"][event]["date"], precio = db["events"][event]["prices"], sinopsis = db["events"][event]["synopsis"], tipo = db["events"][event]["type"])
            lista_events.append(teatro_obj)

    return lista_events

def show_events(db, lista):

    lista_events = assign_events(db, lista)

    #Se muestra la información ordenadamente.
    print("")
    print("    -----------EVENTOS-------------     ")
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
        print("-Precios:")
        print(f"*General: ${lista_events[eve].get_precio()[0]}")
        print(f"*VIP: ${lista_events[eve].get_precio()[1]}")    

        print("")
        print("-----------------------------------------------------")
        print("")            
   
def search_event(db, num, lista): #preguntar por cuál filtro desea buscar

    lista_events = assign_events(db, lista)

#########    T I P O   ########
    if num == 1: 
        op = check_op(1, 2, '''Seleccione el tipo de evento:
                            \n1.-Musical
                            \n2.-Obra de teatro\n-->''')
        print("Resultados de su búsqueda:")
        for event in range(len(lista_events)): 
            if lista_events[event].get_tipo() == op:
                print("")
                print(f'''-Nombre: {lista_events[event].get_nombre_evento()}''')
                print("---------------------------------------------------------")

            
    
########### N O M B R E ##########
    if num == 4:
        
        op_nom = check_let("Ingrese el nombre del evento que desea buscar:\n==>")

        inside_lista = False
        for event in range(len(lista_events)): 
            if lista_events[event].get_nombre_evento() == op_nom:
                inside_lista = True
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
                break
            
        if inside_lista == False:
            print("Ha ingresado un nombre inválido, intente nuevamente.")

        


    

        
        
        