import numpy as np

class PilaSecuencial:
    __items = None
    __tope: int
    __cantidad: int

    def __init__(self, dimension):
        self.__items = np.empty(dimension, dtype=int)
        self.__tope = 0
        self.__cantidad = dimension

    def vacia(self):
        return self.__tope == 0
    
    def insertar(self, dato):
        if self.__tope < self.__cantidad:
            self.__items[self.__tope] = dato
            self.__tope += 1
        else:
            print("Pila llena")

    def suprimir(self):
        if not self.vacia():
            self.__tope -= 1
        else:
            print("Pila vacia")

    def recorrer(self):
        i=self.__tope-1
        while i>=0:
            print(self.__items[i])
            i-=1
    
    def calcFactorial(self):
        fact=1
        while not self.vacia():
            self.suprimir()
            fact*=self.__items[self.__tope] #fact = fact * self.__items[self.__top]
        print("El numero factorial es: ", fact)

    def mostrarFactorial(self,numero):
        while numero > 0:
            self.insertar(numero)
            numero -= 1
        self.calcFactorial()



if __name__ == '__main__':
    pila = PilaSecuencial(5)
    pila.mostrarFactorial(5)
 

