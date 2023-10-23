# Tabla Hash
# Manejo de Colisiones: Buckets

import numpy as np

class TablaHash:
    __dimension : int
    __tabla : np.ndarray

    def __init__(self, dimension, dimensionBucket):
        self.__dimension = self.getPrimo(int(dimension//0.7)) #Factor de carga = 0.7 ejemplo 100 // 0.7 = 142 primo mas cercano 149
        self.__dimensionBucket = dimensionBucket
        self.__dimensionOverflow = int(self.__dimension *0.2)

        self.__tablaOverflow = np.empty((self.__dimensionOverflow, self.__dimensionBucket) , dtype=int)
        self.__tabla = np.empty((self.__dimension, self.__dimensionBucket), dtype=int)

        self.inicializar()    

    def inicializar(self):
        for i in range(0, self.__dimension):
            for j in range(0, self.__dimensionBucket):
                self.__tabla[i][j] = 0
        
        for i in range(0, self.__dimensionOverflow):
            for j in range(0, self.__dimensionBucket):
                self.__tablaOverflow[i][j] = 0
    
    def getPrimo(self, numero):
        for i in range(2, numero):
            if numero % i == 0:
                return self.getPrimo(numero+1)
        return numero

    def metodoExtraccionClaves(self, valor, dimension): #Explicacion: extrae el ultimo digito de cada numero como clave para la tabla hash
        valor = valor % 10 #Ejemplo: 123 -> 123 % 100 = 23
        return valor % dimension

    def insertar(self, valor):
        direccion = self.metodoExtraccionClaves(valor, self.__dimension)
        j = 0
        while j < self.__dimensionBucket and self.__tabla[direccion][j] != 0:
            j += 1
        if j < self.__dimensionBucket:
            self.__tabla[direccion][j] = valor

        else:
            direccion = self.metodoExtraccionClaves(valor, self.__dimensionOverflow)
            j = 0
            while j < self.__dimensionBucket and self.__tablaOverflow[direccion][j] != 0:
                j += 1
            if j < self.__dimensionBucket:
                self.__tablaOverflow[direccion][j] = valor
            else:
                print("No se pudo insertar")
    
    def buscar(self, valor):
        direccion = self.metodoExtraccionClaves(valor, self.__dimension)
        j = 0
        while j < self.__dimensionBucket and self.__tabla[direccion][j] != valor:
            j += 1
        if j < self.__dimensionBucket:
            return True
        else:
            return False

    def mostrar(self):
        print("#Tabla Hash")
        for i in range(0,self.__dimension):
            print("\nDireccion: ", i)
            for j in range(0,self.__dimensionBucket):
                print("{}:{}".format(j,self.__tabla[i][j]), end="    ")
            print("")
        print("\n\n")
        print("#Tabla Overflow")
        for i in range(0, self.__dimensionOverflow):
            print("\nDireccion: ", i)
            for j in range(0, self.__dimensionBucket):
                print("{}:{}".format(j,self.__tablaOverflow[i][j]), end="   ")
            print("")
    
if __name__ == "__main__":
    th = TablaHash(10, 3)
    th.insertar(123)
    th.insertar(323)
    th.insertar(453)
    th.insertar(553)
    th.insertar(456)
    th.insertar(789)

    th.mostrar()