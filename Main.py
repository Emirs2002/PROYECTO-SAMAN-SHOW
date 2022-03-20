from tools import *
from Taquilla import *

def main():
    
    lista_eventos = []
    clients_db = []

    lista_eventos = Taquilla(assign_event(lista_eventos))
 
    while True:

       

        print("")
        print("***BIENVENIDO A SAMAN SHOW***")
        print("")
                              #Menú principal
        op = check_op(1, 6, '''Ingrese la opción que desea realizar:
            \n1.- Ver eventos
            \n2.- Venta de Tickets
            \n3.- Ver alimentos
            \n4.- Venta Feria
            \n5.- Estadísticas
            \n6.- Salir
            \n==>''') 

        if op == 1:   #MÓDULO 1: Opción "ver eventos" abre un submenú
            while True:   
                op1 = check_op(1, 3, '''Ingrese la opción que desea realizar:      
                            \n1.-Ver todos los eventos
                            \n2.-Buscar eventos por filtro
                            \n3.-Volver al menú \n-->''')
                if op1 == 1:
                    lista_eventos.show_events()          #Muestra todos los eventos con su respectiva información
                    
                if op1 == 2:
                    filtro = check_op(1, 4, '''Ingrese la opción que desea realizar:
                                    \n1.-Tipo
                                    \n2.-Fecha   
                                    \n3.-Actor o cantante
                                    \n4.-Nombre \n-->''')     #NOTE cómo es eso de buscar por fecha
                    if filtro == 1:                        
                        lista = Taquilla(lista_eventos.search_event(filtro))  #busca los eventos por tipo y devuelve una lista con los objetos que tengan el atributo especificado
                        lista.show_events()                                   # esta lista se convierte en objeto Taquilla y se le aplica el método show_events para enseñar la información en pantalla

                    if filtro == 2:
                        lista_eventos.search_event(filtro)

                    if filtro == 3:
                        lista_eventos.search_event(filtro)

                    if filtro == 4:
                        lista_eventos.search_event(filtro)

                if op1 == 3:
                    break


        if op == 2:
            pass

        if op == 6:
            print("¡Adiós!")
            break
        

main()