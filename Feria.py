from tools import *
from Bebida import Bebida
from Alimento import Alimento

class Feria():
    def __init__(self, food_db):
        self.__food_db = food_db

    def get_food_db(self):
        return self.__food_db



    #######    MÓDULO 3   #######



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
                if lista_productos[art].get_nombre_producto() == op_nom:
                    lista_nombre.append(lista_productos[art])
            
            return lista_nombre
                   
        #### T I P O ####

        if num == 2:
            lista_tipo = []
            op_tipo = check_op(1, 2, '''Seleccione el tipo de producto:
                                \n1.-Alimento
                                \n2.-Bebida\n-->''')
            print("Resultados de su búsqueda:")
            for art in range(len(lista_productos)): 
                if lista_productos[art].get_clasificacion() == op_tipo: 
                    lista_tipo.append(lista_productos[art])
                else:
                    continue
            
            return lista_tipo

        #### P R E C I O S ####

        if num == 3:        #ANCHOR PREGUNTAR POR ESTO 
            pass
        


        #######    MÓDULO 4   #######

    #### ELIMINAR UNA CANTIDAD DETERMINADA DE PRODUCTOS DEL INVENTARIO #####

    def delete_product_inventory(self, num_inventario):
        
        lista_productos = self.__food_db

        num_inventario = check_num("¿Cuántos desea eliminar? \n-->")

        producto_eliminar = int(producto_eliminar)
        num_inventario = int(num_inventario)

        cantidad = lista_productos[producto_eliminar-1].delete_inventory(num_inventario)

        lista_productos[producto_eliminar-1].set_cantidad(cantidad)

        return lista_productos


    ### VERIFICAR QUE EL CLIENTE HAYA COMPRADO UN TICKET ### 


    def check_cedula(self):
        clientes_list = self.__food_db

        cedula = check_num("Ingrese su cédula: \n==>")

        cedula_inside = False
        for client in range(len(clientes_list.get_db())):
            if clientes_list.get_db()[client].get_cedula() == cedula:
                cedula_inside = True
                break
            else:
                continue
        
        if cedula_inside == False:
            return -1 
        else:
            return cedula


    #### COMPRAR UN PRODUCTO ####


    def comprar_comida(self, cedula, client_db):    #NOTE COMENTAR TODO
        
        lista_productos = self.__food_db 
        
        carrito = []
        subtotal = []
        costo = 0
        while True:

            producto_comprado = check_num("Introduzca el número del producto que desea comprar: ")
            producto_comprado = int(producto_comprado)

            cantidad_producto = check_num("Introduzca la cantidad que desea comprar: ")
            cantidad_producto = int(cantidad_producto)

            if cantidad_producto > int(lista_productos[producto_comprado-1].get_cantidad()):
                print("Ha excedido el número de artículos disponibles. Intente nuevamente")
                continue

            nueva_cantidad = lista_productos[producto_comprado-1].delete_inventory(cantidad_producto)

            lista_productos[producto_comprado-1].set_cantidad(nueva_cantidad)

            costo += (float(lista_productos[producto_comprado-1].get_precio()))*cantidad_producto

            cont = 0
            while cont < cantidad_producto:
                carrito.append(lista_productos[producto_comprado-1].get_nombre_producto())   # Añadir a la lista de productos a comprar
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
            descuento = costo_total * 0.15
        else:
            descuento = 0

        iva = costo *0.16

        costo_total = (costo + iva) - descuento

        ###### IMPRIMIR FACTURA  #####

        for cliente in range(len(client_db)):
            if client_db[cliente].get_cedula() == cedula:
                client = client_db[cliente]

        print("********* FACTURA ***********")

        print("*Datos de compra:")
        print(f'''Nombre: {client.get_nombre()}
            \nEdad: {client.get_edad()}
            \nCédula: {client.get_cedula()}''')
        print("-------")
        
        for art in range(len(carrito)):
            print(f"1 {carrito[art]}")
            print("")
        print("")
        print(f"*Subtotal: ${sum(subtotal)}")
        print("-------")
        print(f"*Descuento: -{descuento}")
        print("-------")
        print(f"*IVA: +{iva}")
        print("-------")
        print(f"*Monto total: ${costo_total}")

        op_pagar = check_op(1,2, "¿Desea proceder a pagar? \n1.-Sí \n2.-No\n==>")




            

