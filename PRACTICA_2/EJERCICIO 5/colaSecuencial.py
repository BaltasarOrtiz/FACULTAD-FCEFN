import numpy as np

class ColaSecuencial:
    __items = None
    __pr = None
    __ul = None
    __cantidad = int
    __dim = int

    def __init__(self, dimension):
        self.__items = np.empty(dimension, dtype=int)
        self.__pr = 0
        self.__ul = 0
        self.__cantidad = 0
        self.__dim = dimension

    def vacia(self):
        return self.__cantidad == 0
    
    def lleno(self):
        return self.__cantidad == self.__dim
    
    def insertar(self, dato):
        if self.lleno():
            print("La cola esta llena")
        else:
            self.__items[self.__ul]=dato
            self.__ul=(self.__ul+1)%self.__dim
            self.__cantidad+=1
            print("Elemento insertado correctamente")
            
    
    def suprimir(self):
            
    
    def recorrer(self):
        i=self.__pr
        j=0
        while j<self.__cantidad:
            print("Elemento: ", self.__items[i])
            i=(i+1)%self.__dim
            j+=1


if __name__ == '__main__':
    cola = ColaSecuencial(5)
    cola.insertar(1)
    cola.insertar(2)
    cola.insertar(3)
    print("\n\nMostrando Elementos")
    cola.recorrer()
    

