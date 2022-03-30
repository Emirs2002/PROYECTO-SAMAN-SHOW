from tools import *


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
        
def top_productos(carrito):
    pass