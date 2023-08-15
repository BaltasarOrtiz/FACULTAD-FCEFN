import numpy as np
class PilaSecuencial:
    __items: np.array
    __top: int
    __cantidad: int
    
    def __init__(self,dimension):
        self.__items = np.empty(dimension,dtype=int)
        self.__top = 0
        self.__cantidad = dimension
    
    def Vacia(self):
        return self.__top == 0
    
    def insertar(self,item):
        if self.__top < self.__cantidad:
            self.__items[self.__top] = item
            self.__top += 1
        else:
            print("Pila llena")
    
    def suprimir(self):
        if not self.Vacia():
            self.__top -= 1
            np.delete(self.__items,self.__top)
        else:
            print("Pila vacia")
    
    def recorrer(self):
        while not self.Vacia():
            self.suprimir()
            print(self.__items[self.__top])

if __name__ == "__main__":
    print("------Pila secuencial-------")
    tamanio = int(input("Ingrese el tamaño de la pila: "))
    Pila=PilaSecuencial(tamanio)
    Pila.insertar(1)
    Pila.insertar(2)
    Pila.insertar(3)
    Pila.insertar(4) #Pila llena al intentar insertar 4
    print("Elimina el elemento del tope")
    Pila.suprimir()
    print("--Muestra el contenido de la pila--")
    Pila.recorrer()