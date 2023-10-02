import numpy as np
import os

class Monticulo:
    __arreglo : np.ndarray
    __dimension : int

    def __init__(self, dimension):
        self.__arreglo = np.empty(dimension, dtype = int)
        self.__arreglo[0] = 0
        self.__dimension = dimension+1

    def insertar(self, dato):
        if self.__arreglo[0] < self.__dimension:
            self.__arreglo[0] += 1
            self.__arreglo[self.__arreglo[0]] = dato
            i = self.__arreglo[0]
            while i > 1 and self.__arreglo[i] < self.__arreglo[i//2]:
                aux = self.__arreglo[i]
                self.__arreglo[i] = self.__arreglo[i//2]
                self.__arreglo[i//2] = aux
                i = i//2
        else:
            print("Monticulo lleno")

    def eliminarMinimo(self):
        if self.__arreglo[0] > 0:
            x = self.__arreglo[1]
            self.__arreglo[0] -= 1
            self.__arreglo[1] = self.__arreglo[self.__arreglo[0]]
            
            i = 1

            while (i * 2 + 1 <= self.__arreglo[0]) and ((self.__arreglo[i] > self.__arreglo[i*2]) or (self.__arreglo[i] > self.__arreglo[i*2+1])):
                if self.__arreglo[i*2] < self.__arreglo[i*2+1]:
                    aux = self.__arreglo[i*2]
                    self.__arreglo[i*2] = self.__arreglo[i]
                    self.__arreglo[i] = aux
                    i = i*2
                else:
                    aux = self.__arreglo[i*2+1]
                    self.__arreglo[i*2+1] = self.__arreglo[i]
                    self.__arreglo[i] = aux
                    i = i*2+1
            return x
        else:
            print("Monticulo vacio")

    def mostrarMonticulo(self, sangria=4):
        if self.__arreglo[0] == 0:
            print("El montículo está vacío")
            return

        def mostrarMonticuloRec(posicion, cadena):
            print(str(self.__arreglo[posicion]))
            #Para el hijo derecho
            hijoDer = 2 * posicion + 1
            if hijoDer <= self.__arreglo[0]:
                if 2 * posicion <= self.__arreglo[0]:
                    print(cadena+ "├" + "─" * sangria, end="") 
                else:
                    print(cadena+ "└" + "─" * sangria, end="")
                mostrarMonticuloRec(hijoDer, cadena + "│" + " " *sangria)
            #Para el hijo izquierdo
            hijoIzq = 2 * posicion
            if hijoIzq <= self.__arreglo[0]:
                print(cadena+ "└" + "─" * sangria, end="")
                mostrarMonticuloRec(hijoIzq, cadena + " " *sangria)
        mostrarMonticuloRec(1, "")
    
    def mostrar(self):
        i=1
        while i<=self.__arreglo[0]:
            print("Nodo ",self.__arreglo[i])
            if i*2  <= self.__arreglo[0]:
                print("Hijo izquierdo",self.__arreglo[i*2])
            if i*2+1 <= self.__arreglo[0]:
                print("Hijo derecho",self.__arreglo[i*2+1])
            i+=1

            

    def mostrarSecuencial(self):
        if self.__arreglo[0] == 0:
            print("El montículo está vacío")
            return
        for i in range(1, self.__arreglo[0]+1):
            print(self.__arreglo[i], end=" ")
        print()

if __name__ == '__main__':
    os.system("cls")
    m = Monticulo(10)
    m.insertar(1)
    m.insertar(2)
    m.insertar(3)
    m.insertar(4)
    m.insertar(5)
    m.insertar(6)
    
    print("Mostrando monticulo")
    m.mostrarMonticulo()
    print("\nMostrando secuencial")
    m.mostrarSecuencial()
    print("\nMostrando Normal")
    m.mostrar()
    
    
    print("\n\nEliminando el minimo")
    m.eliminarMinimo()
    print("\nMostrando monticulo")
    m.mostrarMonticulo()
    print("\nMostrando secuencial")
    m.mostrarSecuencial()
    print("\nMostrando Normal")
    m.mostrar()

    