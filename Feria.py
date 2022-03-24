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

    #### ELIMINAR UNA CANTIDAD DETERMINADA DE PRODUCTOS DEL INVENTARIO #####

    def delete_product(self):
        
        lista_productos = self.__food_db

        producto_eliminar = check_num("Ingrese el número del producto que desea eliminar: \n==>")
        num_inventario = check_num("¿Cuántos desea eliminar? \n-->")

        producto_eliminar = int(producto_eliminar)
        num_inventario = int(num_inventario)

        cantidad = lista_productos[producto_eliminar-1].delete_inventory(num_inventario)

        lista_productos[producto_eliminar-1].set_cantidad(cantidad)

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

    def comprar_comida(self, cedula, clientes):
        
        lista_productos = self.__food_db 
        

        print("Wiuuuuu")
