from tools import *
from Taquilla import *

def main():
    
    lista_eventos = []
    clients_db = []

    db = get_json()
    
    while True:

        print("")
        print("***BIENVENIDO A SAMAN SHOW***")
        print("")
        op = check_op(1, 6, '''Ingrese la opción que desea realizar:
            \n1.- Ver eventos
            \n2.- Venta de Tickets
            \n3.- Ver alimentos
            \n4.- Venta Feria
            \n5.- Estadísticas
            \n6.- Salir
            \n==>''') 

        if op == 1: 
            while True:
                op1 = check_op(1, 3, '''Ingrese la opción que desea realizar:
                            \n1.-Ver todos los eventos
                            \n2.-Buscar eventos por filtro
                            \n3.-Volver al menú \n-->''')
                if op1 == 1:
                    show_events(db, lista_eventos)
                    
                if op1 == 2:
                    filtro = check_op(1, 4, '''Ingrese la opción que desea realizar:
                                    \n1.-Tipo
                                    \n2.-Fecha
                                    \n3.-Actor o cantante
                                    \n4.-Nombre \n-->''')
                    if filtro == 1:
                        search_event(db, filtro, lista_eventos)
                    
                    if filtro == 4:
                        search_event(db, filtro, lista_eventos)

                if op1 == 3:
                    break

        if op == 6:
            print("¡Adiós!")
            break
        

main()