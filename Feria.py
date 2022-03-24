from tools import *
from Bebida import Bebida
from Alimento import Alimento

class Feria():
    def __init__(self, food_db):
        self.__food_db = food_db

    def get_food_db(self):
        return self.__food_db

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

    def delete_product(self):
        
        lista_productos = self.__food_db

        producto_eliminar = check_num("Ingrese el número del producto que desea eliminar: \n==>")

        producto_eliminar = int(producto_eliminar)

        lista_productos.pop(producto_eliminar-1)

        return lista_productos

    def search_product():    #nombre, tipo, o rango de precio
        pass

    