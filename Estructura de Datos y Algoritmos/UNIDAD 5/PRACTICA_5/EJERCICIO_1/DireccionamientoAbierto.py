# Politica de Manejo de Colisiones: Direccionamiento Abierto
# Función de Transformación de Claves: Método de la división
# Procesamiento de Claves Sinónimas: Secuencia de prueba lineal


import numpy as np
import random

class DireccionamientoAbierto:
    __dimension: int
    __tabla = None


    def __init__(self, cantClaves, usarPrimo=False):

        self.__dimension = int(cantClaves//0.7)

        self.__tabla = np.empty(self.__dimension, dtype=int)
        for i in range(self.__dimension):
            self.__tabla[i]=0
        

    def getPrimo(self,numero):
        for i in range(2,numero):
            if numero % i == 0:
                return self.getPrimo(numero+1)
        print("Primo: ",numero)
        return numero

    #FUNCIÓN DE TRANSFORMACIÓN H(K)
    #Método de la división (módulo) h(k) = k % m
    def metododeDivison(self,valor): 
        return valor % self.__dimension
    

    def insertar(self,valor):
        print("Valor: ",valor)
        print("Direccion: ",self.metododeDivison(valor))
        direccion = self.metododeDivison(valor)
        j = 0
        if self.__tabla[direccion] == 0:
            self.__tabla[direccion] = valor
        else:
            while self.__tabla[direccion] != valor and self.__tabla[direccion] != 0 and j<self.__dimension:
                #direccion = (direccion + 1) % self.__dimension
                direccion = self.metododeDivison(direccion+1)
                j += 1

            if j<self.__dimension and self.__tabla[direccion] == 0:
                self.__tabla[direccion] = valor
        #print(j)


    def buscar(self,valor):
        direccion = self.metododeDivison(valor)
        j=0
        while self.__tabla[direccion] != valor and self.__tabla[direccion] != 0 and j<self.__dimension:
                #direccion = (direccion + 1) % self.__dimension
                direccion = self.metododeDivison(direccion+1)
                j += 1
        
        
    

    def mostrarTablaHashing(self):
        print(self.__tabla)

if __name__ == '__main__':
    tabla = DireccionamientoAbierto(10)

    for i in range(10):
        tabla.insertar(random.randint(20,30))


    tabla.mostrarTablaHashing()
    