from tools import *

        #### M Ó D U L O  5 ####

### CALCULAR PROMEDIO DE GASTO DE CLIENTES ###

def promedio_gasto(db):
    print("")
    print("*** Promedio de gasto de los clientes ***")
    print("")
    for cliente in range(len(db)):
        client = db[cliente]
        promedio = client.get_dinero_pagado()/2
        if client.get_feria() == True:
            print("")
            print(f"------------Cliente {cliente+1}------------")
            print("")
            print(f"Promedio de gasto de {client.get_nombre()} (C.I.{client.get_cedula()}): ${promedio}")


### CALCULAR PORCENTAJE DE CLIENTES QUE NO COMPRARON EN LA FERIA ###

def clientes_no_feria(db):

    total_clientes = len(db)

    cont = 0
    for cliente in range(len(db)):
        client = db[cliente]
        if client.get_feria() == False:
            cont += 1
    
    porcentaje = (cont*100)//total_clientes

    print("")
    print(f"{porcentaje}% de los clientes no compró en la feria.")
    print("")


### TOP 3 CLIENTES MÁS FIELES ###

def top_clientes(db):

    clientes_top = []
    for cliente in range(len(db)):       #Añadir en una lista los clientes que hayan comprado en la feria
        client = db[cliente]
        if client.get_feria() == True:
            clientes_top.append(client)

    clientes_top = quicksort_dinero_pagado(clientes_top)   #Ordenar lista por dinero gastado entre eventos y feria
    
    print("")
    print("********** ·TOP 3 CLIENTES SAMAN SHOW· **********")
    print("")
    for cliente in range(3):
        client = clientes_top[cliente]
        if client.get_feria() == True:
            print("")
            print(f"------------{cliente+1}------------")
            print("")
            client.show_client_data()

            print("")
            print(f"------------------------")
            print("")

        ### TOP 3 EVENTOS ###
    
def top_eventos(carrito):

    carrito = quicksort_ingreso(carrito)

    print("")
    print(" ********** TOP 3 EVENTOS **********")
    print("")
    if len(carrito) < 3:
        for event in range(len(carrito)):
            evento = carrito[event]
            print("")
            print(f"------------{event+1}------------")
            print("")
            print("")
            print(f'''Nombre: {evento.get_nombre_evento()}
                    \nIngreso total: ${evento.get_ingreso()}''')
            print("")

    if len(carrito) >= 3:
        for event in range(3):
            evento = carrito[event]
            print("")
            print(f"------------{event+1}------------")
            print("")
            print("")
            print(f'''Nombre: {evento.get_nombre_evento()}
                    \nIngreso total: ${evento.get_ingreso()}''')
            print("")


        ### MOSTRAR TOP 5 PRODUCTOS VENDIDOS ###

def top_productos(carrito, lista):
    
    #CONTADORES ALIMENTOS
    cont_pizza = 0
    cont_hamburguesa = 0
    cont_dorito = 0
    cont_platanito = 0

    #CONTADORES BEBIDAS
    cont_coca_cola = 0
    cont_jugo = 0
    cont_cerveza = 0


    cont_pizza = carrito.count("Pizza")
    cont_hamburguesa = carrito.count("Hamburguesa")
    cont_dorito = carrito.count("Doritos")
    cont_platanito = carrito.count("Platanitos")

    cont_coca_cola = carrito.count("Coca Cola")
    cont_jugo = carrito.count("Jugo")
    cont_cerveza = carrito.count("Cerveza")
    
    new_list = []
    for art in range(len(lista)):
        producto = lista[art]
        if producto.get_nombre_producto() == "Pizza":
            producto.set_vendido(cont_pizza)
            new_list.append(producto)

        if producto.get_nombre_producto() == "Hamburguesa":
            producto.set_vendido(cont_hamburguesa)
            new_list.append(producto)

        if producto.get_nombre_producto() == "Doritos":
            producto.set_vendido(cont_dorito)
            new_list.append(producto)

        if producto.get_nombre_producto() == "Platanitos":
            producto.set_vendido(cont_platanito)
            new_list.append(producto)

        if producto.get_nombre_producto() == "Coca Cola":
            producto.set_vendido(cont_coca_cola)
            new_list.append(producto)

        if producto.get_nombre_producto() == "Cerveza":
            producto.set_vendido(cont_cerveza)
            new_list.append(producto)
        
        if producto.get_nombre_producto() == "Jugo":
            producto.set_vendido(cont_jugo)
            new_list.append(producto)


    new_list = quicksort_vendido(new_list)    #Ordenar nueva lista con cantidades actualizadas por dichas cantidades

        ## IMPRIMIR NEW_LIST DE MAYOR A MENOR ##

    print("")
    print("--------------- TOP 5 PRODUCTOS VENDIDOS ---------------")
    print("")
    for art in range(5):
        producto = new_list[art]
        print("")
        print(f"--------- {art+1} ---------")
        print("")
        print(f"Nombre: {producto.get_nombre_producto()} \nCantidad: {producto.get_vendido()}")




    
    

