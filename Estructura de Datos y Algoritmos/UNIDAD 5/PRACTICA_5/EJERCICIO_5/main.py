"""Dado un conjunto de 100 nombres insertar los mismos en una tabla hash  
usando una función de transformación de clave adecuada para las mismos, 
y use la secuencia de prueba lineal para el manejo de colisiones.   

Muestre el promedio de comparaciones para  buscar de una clave."""

import numpy as np
import os
class tablaHash_DA_primo: #Direccionamiento Abierto (DA) con num primo para la dimension
    __dimension : int
    __tabla : np.ndarray
    __contador : int

    def __init__(self, dimension):
        self.__dimension = self.getPrimo(int(dimension//0.7)) #Factor de carga = 0.7 ejemplo 100 // 0.7 = 142 primo mas cercano 149
        self.__tabla = np.empty(self.__dimension, dtype= object) #dtype=object (para que acepte cualquier tipo de dato en el array)
        self.__contador = 0
    
        for i in range(0,self.__dimension):
            self.__tabla[i] = ""
    
    def getPrimo(self, numero):
        for i in range(2, numero):
            if numero % i == 0:
                return self.getPrimo(numero+1)
        return numero
    
    def metodoDivision(self, valor):
        return valor % self.__dimension
    
    def insertar(self, valor):
        direccion = self.metodoClavesAlfanumericas(valor)
        j = 0
        if self.__tabla[direccion] == "":
            self.__tabla[direccion] = valor
            print(self.__tabla[direccion])
        else:
            while self.__tabla[direccion] != valor and self.__tabla[direccion] != "" and j<self.__dimension:
                self.__contador += 1
                direccion = (direccion + 1) % self.__dimension
                j += 1

            if j<self.__dimension and self.__tabla[direccion] == "":
                self.__tabla[direccion] = valor
            
    def buscar(self, valor):
        direccion = self.metodoDivision(valor)
        j = 0

        while self.__tabla[direccion] != valor and self.__tabla[direccion] != 0 and j<self.__dimension:
            direccion = (direccion + 1) % self.__dimension
            j += 1

        if self.__tabla[direccion] == valor:
            return direccion
        else:
            return -1
    
    def mostrar(self):
        for i in range(0, self.__dimension):
            print("Posicion", i, ":", self.__tabla[i])
    
    def promedioColisiones(self):
        return self.__contador/self.__dimension

    def metodoClavesAlfanumericas(self, valor):
        acumulador = 0

        for i in range(0, len(str(valor))):
            acumulador += ord(str(valor)[i]) * (10**i)

        return acumulador % self.__dimension

if __name__ == "__main__":
    os.system("cls")
    tabla = tablaHash_DA_primo(3)
    nombres = ["Juan", "Poto", "Mauro"]
    print(nombres)

    for i in range(0, len(nombres)):
        tabla.insertar(nombres[i])
    
    print("\n\n")
    tabla.mostrar()
    print("Promedio de colisiones: ", tabla.promedioColisiones())
