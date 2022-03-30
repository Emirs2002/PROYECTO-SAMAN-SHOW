from tools import *
from Taquilla import Taquilla
from Feria import Feria 
from Funciones_estadísticas import *


def main():
    
    # LISTAS 
    lista_eventos = []
    lista_articulos = []
    clients_db = []
    carrito_productos = []
    carrito_eventos = []

    #CONTADORES MUSICALES
    cont_saman = 0
    cont_guako = 0

    #CONTADORES TEATRO
    cont_romeo = 0
    cont_fantasma = 0

    #CONTADORES ALIMENTOS
    cont_pizza = 0
    cont_hamburguesa = 0
    cont_dorito = 0
    cont_platanito = 0

    #CONTADORES BEBIDAS
    cont_coca_cola = 0
    cont_jugo = 0
    cont_cerveza = 0


    lista_eventos = Taquilla(assign_event(lista_eventos))  #se asigna la información del API a sus respectivos objetos y se añaden a una lista vacía
                                                            #La lista con la info de los eventos/productos se transforma en objeto Taquilla y Feria
    
    lista_articulos = Feria(assign_producto(lista_articulos))

    
    while True:

        #lista_asientos_ocupados = read_db("asientos_ocupados.txt", lista_asientos_ocupados)

        print("")
        print("***BIENVENIDO A SAMAN SHOW***")
        print("")
                              #Menú principal
        op = check_op(1, 7, '''Ingrese la opción que desea realizar:
            \n1.- Gestión eventos
            \n2.- Comprar tickets
            \n3.- Gestión Feria
            \n4.- Comprar productos
            \n5.- Estadísticas
            \n6.- Reestablecer base de datos
            \n7.- Salir
            \n==>''') 

        if op == 1:   #MÓDULO 1: Opción "ver eventos" abre un submenú
            while True:   
                op1 = check_op(1, 4, '''Ingrese la opción que desea realizar:     
                            \n1.-Ver todos los eventos
                            \n2.-Buscar eventos por filtro
                            \n3.-Apertura o cierre de evento
                            \n4.-Volver al menú 
                            \n-->''')                            
                    
                    #SUBMENÚ DE VER EVENTOS

                if op1 == 1:
                    lista_eventos.show_events()          #Muestra todos los eventos con su respectiva información
                    
                if op1 == 2:
                    filtro = check_op(1, 5, '''Ingrese la opción que desea realizar:
                                    \n1.-Tipo
                                    \n2.-Fecha   
                                    \n3.-Actor o cantante
                                    \n4.-Nombre \n-->''')     
                                            
                    lista = Taquilla(lista_eventos.search_event(filtro))  #busca los eventos por tipo y devuelve una lista con los objetos que tengan el atributo especificado
                    if lista.get_db() == []:                              #esta lista se convierte en objeto Taquilla y se le aplica el método show_events para enseñar la información en pantalla
                        print("")
                        print("***  Error: la información que ha ingresado no se encuentra en la base de datos, intente nuevamente  ***")
                        print("")                                                                           
                    else:
                        lista.show_events()     

                if op1 == 3:     #abrir o cerrar venta de tickets
                    lista_eventos.show_events()  
                    lista_eventos.change_availability()

                if op1 == 4:
                    break


        if op == 2:       #MÓDULO 2: Venta de tickets

            clients_db = Taquilla(read_db("clientes.txt", clients_db))
            client_event, evento, evento_escogido= clients_db.comprar_tickets(lista_events = lista_eventos)
            
            
            if client_event == -1:    #Cliente declina el pago
                continue

            else:                     #Cliente acepta realizar el pago
                print("Su compra ha sido completada exitosamente.")
                clients_db.get_db().append(client_event)
                load_db("clientes.txt", clients_db.get_db())
                
                if len(carrito_eventos) == 0:
                    carrito_eventos.append(evento)
                else:
                    for eve in range(len(carrito_eventos)):
                        event = carrito_eventos[eve]
                        if event.get_nombre_evento().lower().capitalize() == evento_escogido:
                            carrito_eventos.pop(eve)
                            break
                
                    carrito_eventos.append(evento)
                

        if op == 3:      #MÓDULO 3: Gestión de artículos de la feria
            while True:   
                op3 = check_op(1, 4, '''Ingrese la opción que desea realizar:     
                            \n1.-Ver todos los productos
                            \n2.-Buscar productos por filtro
                            \n3.-Eliminar producto                             
                            \n4.-Volver al menú
                            \n-->''')          
                if op3 == 1:
                    lista_articulos.show_products()
                
                if op3 == 2:                    
                    filtro = check_op(1, 3, '''Ingrese por cuál filtro desea buscar:
                                    \n1.-Nombre
                                    \n2.-Tipo   
                                    \n3.-Precios
                                    \n-->''')

                    lista = Feria(lista_articulos.search_product(filtro))

                    if lista.get_food_db() == []:
                        print("")
                        print("***  Error: la información que ha ingresado no se encuentra en la base de datos, intente nuevamente  ***")
                        print("")  
                    else: 
                        lista.show_products()


                if op3 == 3:
                    lista_articulos.show_products()
                    lista_articulos = Feria(lista_articulos.delete_product())

                if op3 == 4:                  
                    break


        if op == 4:      # MÓDULO 4: Compra de comida

            clients_db = Feria(read_db("clientes.txt", clients_db))
            id_confirmation = clients_db.check_cedula()

            if id_confirmation == -1:
                print("")
                print("Para comprar en la feria necesita haber comprado en la taquilla.")
                print("")

            else:
                clients_list = clients_db.get_food_db()
                lista_articulos.show_products()
                lista_articulos, cliente, pagado= lista_articulos.comprar_comida(id_confirmation, clients_list)
                
                if pagado == True:
                    lista_articulos = Feria(lista_articulos)

                    for client in range(len(clients_db.get_food_db())):
                        c = clients_db.get_food_db()[client]
                        if c.get_cedula() == id_confirmation:
                            clients_db.get_food_db().pop(client)

                    clients_db.get_food_db().append(cliente)           #retorna clientre para añadir el coste de la compra al atributo "dinero_pagado" 
                    load_db("clientes.txt", clients_db.get_food_db())

                elif pagado == False:
                    lista_articulos = Feria(lista_articulos)

        if op == 5:  # MÓDULO 5: Estadísticas
            
            while True:
                op5 = check_op(1,6, '''Ingrese el número de la opción que desea ejecutar:
                            \n1.-Mostrar promedio de gasto de cliente
                            \n2.-Mostrar porcentaje de clientes que no compran en la feria
                            \n3.-Mostrar top 3 clientes Saman Show
                            \n4.-Mostrar top 3 eventos 
                            \n5.-Mostrar top 5 productos más vendidos
                            \n6.-Volver al menú
                            \n==>''')
                if op5 == 1:
                    clients_db = read_db("clientes.txt", clients_db)
                    promedio_gasto(clients_db)

                if op5 == 2:
                    clients_db = read_db("clientes.txt", clients_db)
                    clientes_no_feria(clients_db)
                
                if op5 == 3:
                    clients_db = read_db("clientes.txt", clients_db)
                    top_clientes(clients_db)

                if op5 == 4:
                    top_eventos(carrito_eventos)
                    
                if op5 == 5:
                    pass
                    
                
                if op5 == 6:
                    break
        
        if op == 6:    # Reestablecer la información de la base de datos
            lista_articulos = []
            lista_eventos = []
            clients_db = []

            lista_eventos = Taquilla(assign_event(lista_eventos))                                            
    
            lista_articulos = Feria(assign_producto(lista_articulos))

            load_db("clientes.txt", clients_db)

            print("")
            print("¡Datos reestablecidos!")
            print("")

        if op == 7:   #Salir de la aplicación 
            print("¡Hasta pronto!")
            break
        
main()