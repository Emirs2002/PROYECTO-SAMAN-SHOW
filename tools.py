
import pickle
import os
import requests   
import json
from Musical import Musical
from Teatro import Teatro


#validar palabras
def check_let(msg):
    while True:
        print("")
        word = input(msg)
        if word.replace(" ", "").replace("&", "").isalpha():
             break
        else:
            print("Error, enter a valid data")
            continue
    return word

#validar números (general)
def check_num(msg):
    while True:
        print("")
        num = input(msg)        
        if num.replace(" ", "").isnumeric():
             break
        else:
            print("Error, enter number")
            continue    
    return num

#validar números en un rango de números específico

def check_op(lim1, lim2, msg):
    while True:
        print("")
        num = input(msg)        
        if num.replace(" ", "").isnumeric():
            num = int(num)
            if num < lim1 or num > lim2:
                print("Error, enter a valid number")
                continue
            else:
                break
        else:
            print("Error, enter a number")
            continue    
    return num


########## Lectura de archivos ##########


# recibir datos de la db #

def read_db(txt, datos):

    lectura = open(txt, "rb")   
    if os.stat(txt).st_size != 0:     #comprobar que el archivo esté vacío
        datos = pickle.load(lectura)    
    lectura.close()

    return datos

# cargar datos en la db #

def load_db(txt, datos):

    escritura = open(txt, "wb")

    pickle.dump(datos, escritura)   

    escritura.close()   

######### Adquirir la información del API #########
     
def assign_event(lista_events):
    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api_saman_show/main/api.json"
    response = requests.get(url)

    if response.status_code == 200:
        db = response.json()       
                                       
        for event in range(len(db["events"])):         #Añadir los elementos del JSON a los objetos Musical y Teatro respectivamente 
            if db["events"][event]["type"] == 1:
                musical_obj = Musical(nombre_evento = db["events"][event]["title"], cartel = db["events"][event]["cartel"], asientos = db["events"][event]["layout"], fecha = db["events"][event]["date"], num_bandas = db["events"][event]["bands"], precio = db["events"][event]["prices"], tipo = db["events"][event]["type"])
                lista_events.append(musical_obj)
                
            elif db["events"][event]["type"] == 2:
                teatro_obj = Teatro(nombre_evento = db["events"][event]["title"], cartel =db["events"][event]["cartel"], asientos = db["events"][event]["layout"], fecha = db["events"][event]["date"], precio = db["events"][event]["prices"], sinopsis = db["events"][event]["synopsis"], tipo = db["events"][event]["type"])
                lista_events.append(teatro_obj)
        
        return lista_events

###  Ordenar los objetos por un parámetro introducido ###

def quick_sort(lista):    #FIXME PONERLO A TRABAJAR CON OBJETOS EN GENERAL

    
    if len(lista) <=1:
        return lista    
   
    objeto = lista[0]
    pivote = objeto.get_average()
    menores = []
    mayores = []
    for student in range(1, len(lista)):
        num = lista[student].get_average()
        if num > pivote:
            mayores.append(lista[student])
        else:
            menores.append(lista[student])
    return quick_sort(mayores) + [objeto] + quick_sort(menores)



### Hacer matrices de filas y columnas especificadas por el usuario ### 

def matrix(filas, columnas, let):
    for fila in range(1, filas+1):
        for columna in range(1, columnas+1):
            if columna == 1:
                print(f"{let}{fila}-{columna}", end=" ")
            else:
                print(f" {let}{fila}-{columna}", end=" ")
        print("")
        
def check_vampire(num):
    pass