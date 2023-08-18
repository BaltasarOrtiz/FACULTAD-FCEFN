import random
from pila1 import Pila1
from pila2 import Pila2
from pila3 import Pila3


def cargarPila1(pila1, cant):
    numero_anterior = None
    for x in range(cant):
        if numero_anterior is None:
            numero = random.randint(1, 100)
        else:
            numero = random.randint(numero_anterior - 10, numero_anterior - 1)  # Asegura que el nuevo número sea menor
        numero_anterior = numero
        pila1.insertar(numero)
    print("Discos colocados correctamente")


def validarMovimiento(pila, numPieza):
    



if __name__ == '__main__':
    print("Inicio del programa")
    pila1 = Pila1()
    pila2 = Pila2()
    pila3 = Pila3()

    #cant = int(input("Ingrese la cantidad de Discos con la que jugara: "))
    cant = 5
    cargarPila1(pila1, cant)
    print("\n\n---------------------------------------\n\n")
    
    while (pila1.Vacia() | pila2.Vacia()) == True: #el juego solo termina cuando la pila1 y pila2 esten vacias
        print("Estado actual de las pilas: ")
        print("Pila 1: ")
        pila1.mostrar()
        print("\n")
        print("Pila 2: ")
        pila2.mostrar()
        print("\n")
        print("Pila 3: ")
        pila3.mostrar()
        print("---------------------------------------")
        print("\n\n")

        origen = int(input("Ingrese la pila de origen: "))
        destino = int(input("Ingrese la pila de destino: "))
        numPieza = input("Ingrese la pieza que desea quitar: ")

        if origen == 1:
            validarMovimiento(pila1, numPieza)
        elif origen == 2:
            validarMovimiento(pila2, numPieza)
        elif origen == 3:
            validarMovimiento(pila3, numPieza)
        else:
            print("Pila de origen no valida")
            



