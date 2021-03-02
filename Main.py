import pickle

from models.Escapada import *


# Listado de las propuestas


def listado_propuesta(fichero):
    
    with open (fichero,'rb') as pickle_file:
        propuestas = pickle.load(pickle_file)
    
    for indice in range(len(propuestas)):
        propuestas[indice].get_datos()

# Calcular el tamaño ddel fichero


def get_tamanio(fichero):
    try:
        with open(fichero, errors="ignore") as fich:
            total_fichero = fich.readlines()
        return int(len(total_fichero))
    except IOError:
        return 0

# Alta a una nueva propuesta


def alta_propuesta(fichero):
    tamanio = get_tamanio(fichero)
    propuestas=[]
    if input("Escapada o viaje: ") == "Escapada":
        escapada = Escapada(tamanio+1,
                            input("Destino: "), input("Fecha: "), input("Descripcion: "), input("Autobus: "))
        f = open(fichero, "wb")
        propuestas.append(escapada)
        pickle.dump(propuestas, f)
        f.close
        del(f)


# Menu


def menu():
    opc = int(input("1.-Alta de propuestas.\n" +
                    "2.-Listado de las propuestas de la agencia.\n" +
                    "3.-Eliminar TurOperadora.\n" +
                    "4.-Listado de las propuestas para un destino.\n" +
                    "5.-Salir.\n"))
    return opc


# Main
fichero = "fichero11.txt"
while True:
    opc = menu()
    if opc == 1:
        alta_propuesta(fichero)
    elif opc == 2:
        listado_propuesta(fichero)
    elif opc == 5:
        break
