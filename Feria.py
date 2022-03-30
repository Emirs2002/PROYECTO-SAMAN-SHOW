from tools import *
from Bebida import Bebida
from Alimento import Alimento

class Feria():
    def __init__(self, food_db):
        self.__food_db = food_db

    def get_food_db(self):
        return self.__food_db



    #######    MÓDULO 3   #######               #NOTE COMENTAR TODO EL CÓDIGO



    def show_products(self):

        lista_products = self.__food_db

        print("")
        print("    ------------------ ARTÍCULOS -------------------     ")
        print("")       
           
        for art in range(len(lista_products)):
            print("")
            print(f"---------- Producto {art+1} ----------")
            print("")
            if type(lista_products[art]) == Alimento:
                lista_products[art].show_alimento()
            else:
                lista_products[art].show_bebida()          
            print("")
            print("-----------------------------------------------------")
            print("") 

    #### ELIMINAR UN PRODUCTO DE LA LISTA ####

    def delete_product(self):

        lista_productos = self.__food_db
        
        producto_eliminar = check_num("Ingrese el número del producto que desea eliminar: \n==>")
        producto_eliminar = int(producto_eliminar)

        lista_productos.pop(producto_eliminar-1)

        return lista_productos
   

    ######### BUSCAR PRODUCTOS POR FILTRO ###########


    def search_product(self, num):    #nombre, tipo, o rango de precio
        
        lista_productos = self.__food_db

        #### N O M B R E ####

        if num == 1:
            lista_nombre = [] 
            op_nom = check_let("Ingrese el nombre del producto: \n==>")            
            
            for art in range(len(lista_productos)):
                articulo = lista_productos[art]
                if articulo.get_nombre_producto() == op_nom:
                    lista_nombre.append(articulo)
            
            return lista_nombre
                   
        #### T I P O ####

        if num == 2:
            lista_tipo = []
            op_tipo = check_op(1, 2, '''Seleccione el tipo de producto:
                                \n1.-Alimento
                                \n2.-Bebida\n-->''')
            print("Resultados de su búsqueda:")
            for art in range(len(lista_productos)): 
                articulo = lista_productos[art]
                if articulo.get_clasificacion() == op_tipo: 
                    lista_tipo.append(articulo)
                else:
                    continue
            
            return lista_tipo

        #### P R E C I O S ####
        lista_precios = []                #NOTE COMENTAR TODO
        if num == 3:       
            op_precio = check_op(1,3,'''Seleccione el rango de precios que desea consultar: 
                    \n1.-Menor a $5 
                    \n2.-De $5 a $10 
                    \n3.-Mayor a $10 
                    \n==>''')

            for art in range(len(lista_productos)): 
                articulo = lista_productos[art] 
                if op_precio == 1:
                    if articulo.get_clasificacion() == 1:
                        if float(articulo.get_precio()) < 5:
                            lista_precios.append(articulo)
                    else:
                        for precio in range(len(articulo.get_precio())):
                            if float(articulo.get_precio()[precio]) < 5:
                                lista_precios.append(articulo)
                                break

                if op_precio == 2:
                    if articulo.get_clasificacion() == 1:
                        if float(articulo.get_precio()) > 5 and float(articulo.get_precio()) < 10:
                            lista_precios.append(articulo)
                    else:
                        for precio in range(len(articulo.get_precio())):
                            if float(articulo.get_precio()[precio]) > 5 and float(articulo.get_precio()[precio]) < 10:
                                lista_precios.append(articulo)
                                break

                if op_precio == 3:
                    if articulo.get_clasificacion() == 1:
                        if float(articulo.get_precio()) > 10:
                            lista_precios.append(articulo)
                    else:
                        for precio in range(len(articulo.get_precio())):
                            if float(articulo.get_precio()[precio]) > 10:
                                lista_precios.append(articulo)
                                break

            return lista_precios

        #######    MÓDULO 4   #######


    ### VERIFICAR QUE EL CLIENTE HAYA COMPRADO UN TICKET ### 

    def check_cedula(self):
        clientes_list = self.__food_db

        cedula = check_num("Ingrese su cédula: \n==>")

        cedula_inside = False
        for client in range(len(clientes_list)):
            if clientes_list[client].get_cedula() == cedula:
                cedula_inside = True
                break
            else:
                continue
        
        if cedula_inside == False:
            return -1 
        else:
            return cedula


    #### COMPRAR PRODUCTOS ####


    def comprar_comida(self, cedula, client_db):    #NOTE COMENTAR TODO
        
        lista_productos = self.__food_db 
        
        carrito = []
        subtotal = []
        indices = []
        indices_bebidas = []
        cantidad_alimento = []
        cantidad_bebida = []
        tamanho_list = []
        costo = 0
        while True:

            producto_comprado = check_num("Introduzca el número del producto que desea comprar: ")
            producto_comprado = int(producto_comprado)

            

            if type(lista_productos[producto_comprado-1]) == Alimento:

                indices.append(producto_comprado)

                cantidad_producto = check_num("Introduzca la cantidad que desea comprar: ")
                cantidad_producto = int(cantidad_producto)

                cantidad_alimento.append(cantidad_producto)

                alimento = lista_productos[producto_comprado-1]
                
                nueva_cantidad = alimento.delete_inventory(cantidad_producto)

                alimento.set_cantidad(nueva_cantidad)

                costo += (float(alimento.get_precio()))*cantidad_producto

            if type(lista_productos[producto_comprado-1]) == Bebida:
                
                indices_bebidas.append(producto_comprado)

                tamanho = check_op(1,3, "Seleccione el tamaño de la bebida: \n1.-Pequeña\n2.-Mediana\n3.-Grande\n==>")
                tamanho = int(tamanho)

                tamanho_list.append(tamanho)

                cantidad_producto = check_num("Introduzca la cantidad que desea comprar: ")
                cantidad_producto = int(cantidad_producto)

                cantidad_bebida.append(cantidad_producto)

                bebida = lista_productos[producto_comprado-1]

                nueva_cantidad = bebida.delete_inventory_bebida(tamanho, cantidad_producto)

                bebida.set_cantidad_bebida(tamanho, nueva_cantidad)

                costo += (float(bebida.get_precio()[tamanho-1]))*cantidad_producto


            cont = 0
            while cont < cantidad_producto:
                if type(lista_productos[producto_comprado-1]) == Bebida:
                    carrito.append(lista_productos[producto_comprado-1])   # Añadir a la lista de productos a comprar
                    subtotal.append(float(lista_productos[producto_comprado-1].get_precio()[tamanho-1]))        # Añadir a la lista de subtotales de las bebidas
                    cont += 1
                else:
                    carrito.append(lista_productos[producto_comprado-1])   # Añadir a la lista de productos a comprar
                    subtotal.append(float(lista_productos[producto_comprado-1].get_precio()))        # Añadir a la lista de subtotales
                    cont += 1

            op = check_op(1,2,"¿Desea comprar otro producto? \n1.-Sí \n2.-No \n==>")

            if op == 1:
                continue
            if op == 2:
                break

        #### CALCULAR IVA, DESCUENTO Y COSTO TOTAL####

        cedula = int(cedula)
        narcisista = check_narcissistic(cedula)
        if narcisista == True:
            print("")
            print("~ ¡Felicidades, se le ha otorgado un descuento del 15%! ~")
            print("")
            descuento = costo * 0.15
        else:
            descuento = 0

        iva = costo *0.16

        costo_total = (costo + iva) - descuento

        print("")
        print("Costo total de la compra:")
        print("")
        print(f"${costo_total}")
        print("")

        ### PREGUNTAR AL USUARIO SI VA A PAGAR ### 
        
        op_pagar = check_op(1,2, "¿Desea proceder a pagar? \n1.-Sí \n2.-No\n==>")   

        if op_pagar == 1:    #Si desea proceder con el pago
            

                ###### IMPRIMIR FACTURA  #####

            for cliente in range(len(client_db)):
                if client_db[cliente].get_cedula() == str(cedula):     
                    client = client_db[cliente]         
            
            print("")        
            print("********* FACTURA ***********")
            print("")

            print("*Datos de compra:")
            client.show_client_data()
            print("-------")
            print("Artículos:")
            for art in range(len(carrito)):
                print(f"-> {carrito[art].get_nombre_producto()}")
                print("")
            print("")
            print(f"*Subtotal: ${sum(subtotal)}")
            print("-------")
            if descuento != 0:
                print(f"*Descuento: -{descuento}")
                print("-------")
            print(f"*IVA: + ${iva}")
            print("-------")
            print(f"*Monto total: ${costo_total}")

            client.set_dinero_pagado(float(client.get_dinero_pagado())+costo_total)
            client.set_feria(True)

            return lista_productos, client, True    


        elif op_pagar == 2:

            if len(indices) != 0:
                for i in range(len(indices)):
                    indice = indices[i]-1                
                    cantidad = cantidad_alimento[i]
                    articulo = lista_productos[indice]
                    articulo.set_cantidad(articulo.get_cantidad() + cantidad)
            
            if len(indices_bebidas) != 0:
                for i in range(len(indices_bebidas)):
                    indice = indices_bebidas[i]-1                
                    cantidad = cantidad_bebida[i]
                    tamanho = tamanho_list[i]
                    articulo = lista_productos[indice]
                    articulo.set_cantidad_bebida(index = tamanho, nueva_cantidad = articulo.get_cantidad()[tamanho-1] + cantidad)

            return lista_productos, client, False
         
         



                    



        






            

