from tools import *
from Cartelera import *

def main():
    
    lista_eventos = []
    clients_db = []

    lista_eventos = Cartelera(assign_event(lista_eventos))
 
    while True:

        print("")
        print("***BIENVENIDO A SAMAN SHOW***")
        print("")
                              #Menú principal
        op = check_op(1, 6, '''Ingrese la opción que desea realizar:
            \n1.- Ver eventos
            \n2.- Comprar Tickets
            \n3.- Ver artículos de la feria
            \n4.- Venta de la Feria
            \n5.- Estadísticas
            \n6.- Salir
            \n==>''') 

        if op == 1:   #MÓDULO 1: Opción "ver eventos" abre un submenú
            while True:   
                op1 = check_op(1, 3, '''Ingrese la opción que desea realizar:      
                            \n1.-Ver todos los eventos
                            \n2.-Buscar eventos por filtro
                            \n3.-Volver al menú 
                            \n-->''')
                if op1 == 1:
                    lista_eventos.show_events()          #Muestra todos los eventos con su respectiva información
                    
                if op1 == 2:
                    filtro = check_op(1, 4, '''Ingrese la opción que desea realizar:
                                    \n1.-Tipo
                                    \n2.-Fecha   
                                    \n3.-Actor o cantante
                                    \n4.-Nombre 
                                    \n-->''')     
                                            
                    lista = Cartelera(lista_eventos.search_event(filtro))  #busca los eventos por tipo y devuelve una lista con los objetos que tengan el atributo especificado
                    if lista.get_db() == []:                              #esta lista se convierte en objeto Taquilla y se le aplica el método show_events para enseñar la información en pantalla
                        print("")
                        print("***  Error: la información que ha ingresado no se encuentra en la base de datos. Intente nuevamente  ***")
                        print("")                                                                           
                    else:
                        lista.show_events()     
                        
                if op1 == 3:
                    break


        if op == 2:       #Venta de tickets
            pass

        if op == 6:
            print("¡Hasta pronto!")
            break
        

main()