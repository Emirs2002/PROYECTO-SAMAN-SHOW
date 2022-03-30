from tools import *


### CALCULAR PROMEDIO DE GASTO DE UN CLIENTE ###

def promedio_gasto(db):

    for cliente in range(len(db)):
        client = db[cliente]
        if client.get_feria() == True:
            print("")
            print(f"------------Cliente {cliente+1}------------")
            print("")
            client.show_client_data()
    
    while True:
        op = check_num("Ingrese la cédula del cliente:\n==> ")

        inside_db = False
        for cliente in range(len(db)):
            client = db[cliente]
            if client.get_cedula() == op:
                inside_db = True
                promedio = client.get_dinero_pagado()/2
        
        if inside_db == False:
            print("")
            print("Error. Cliente no ha podido ser encontrado, intente nuevamente.")
            print("")

        elif inside_db == True:
            print("")
            print(f"Promedio de gasto de {client.get_nombre()} (C.I.{client.get_cedula()}): ${promedio}")
            print("")

        op_exit = check_op(1,2, "¿Desea ingresar otro cliente?: \n1.-Sí \n2.-No \n==>")

        if op_exit == 1:
            continue

        if op_exit == 2:
            break

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

    clientes_top = quicksort(clientes_top)   #Ordenar lista por dinero gastado entre eventos y feria
    
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


