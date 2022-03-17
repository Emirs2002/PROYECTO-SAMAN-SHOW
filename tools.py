
import pickle
import os
import requests   
import json


#validar palabras
def check_let(msg):
    while True:
        print("")
        word = input(msg)
        if word.replace(" ", "").isalpha():
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

# JSON
     
def get_json():
    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api_saman_show/main/api.json"
    response = requests.get(url)

    if response.status_code == 200:
        db = response.json()
        return db
    