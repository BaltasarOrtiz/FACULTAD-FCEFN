# Politica de Manejo de Colisiones: Direccionamiento Abierto
# Función de Transformación de Claves: Método de la división
# Procesamiento de Claves Sinónimas: Secuencia de prueba lineal

import numpy as np
import random
import os

class tablaHash_DA: #Direccionamiento Abierto (DA)
    __dimension : int
    __tabla : np.ndarray
    __contador : int

    def __init__(self, dimension):
        self.__dimension = int(dimension//0.7)
        self.__tabla = np.empty(self.__dimension, dtype= int)
        self.__contador = 0
    
        for i in range(0,self.__dimension):
            self.__tabla[i] = 0
    
    def metodoDivision(self, valor):
        return valor % self.__dimension
  
    def insertar(self, valor):
        direccion = self.metodoDivision(valor)
        j = 0
        if self.__tabla[direccion] == 0:
            self.__tabla[direccion] = valor
        else:
            while self.__tabla[direccion] != valor and self.__tabla[direccion] != 0 and j<self.__dimension:
                self.__contador += 1
                direccion = (direccion + 1) % self.__dimension
                j += 1

            if j<self.__dimension and self.__tabla[direccion] == 0:
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
            print("Posicion: ", i, " Valor: ", self.__tabla[i])
    
    def promedioColisiones(self):
        return self.__contador/self.__dimension

class tablaHash_DA_primo: #Direccionamiento Abierto (DA) con num primo para la dimension
    __dimension : int
    __tabla : np.ndarray
    __contador : int

    def __init__(self, dimension):
        self.__dimension = self.getPrimo(int(dimension//0.7)) #Factor de carga = 0.7
        self.__tabla = np.empty(self.__dimension, dtype= int)
        self.__contador = 0

        for i in range(0,self.__dimension):
            self.__tabla[i] = 0
    
    def getPrimo(self, numero):
        for i in range(2, numero):
            if numero % i == 0:
                return self.getPrimo(numero+1)
        return numero
    
    def metodoDivision(self, valor):
        return valor % self.__dimension
  
    def insertar(self, valor):
        direccion = self.metodoDivision(valor)
        j = 0
        if self.__tabla[direccion] == 0:
            self.__tabla[direccion] = valor
        else:
            while self.__tabla[direccion] != valor and self.__tabla[direccion] != 0 and j<self.__dimension:
                self.__contador += 1
                direccion = (direccion + 1) % self.__dimension
                j += 1

            if j<self.__dimension and self.__tabla[direccion] == 0:
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
            print("Posicion: ", i, " Valor: ", self.__tabla[i])
    
    def promedioColisiones(self):
        return self.__contador/self.__dimension
        
if __name__ == "__main__":
    os.system("cls")

    tabla1 = tablaHash_DA(10)
    tabla2 = tablaHash_DA_primo(10)

    for i in range(0, 20):
        num_random = random.randint(0, 100)
        tabla1.insertar(num_random)
        tabla2.insertar(num_random)
    
    print("Tabla 1: Sin numero primo")
    tabla1.mostrar()
    print("\n\nTabla 2: Con numero primo")
    tabla2.mostrar()

    print("\n\nPromedio de colisiones tabla 1 sin primo: ", tabla1.promedioColisiones())
    print("Promedio de colisiones tabla 2 con primo: ", tabla2.promedioColisiones())
    print("\n\n")

    #¿Cuál de los dos métodos es más eficiente? ¿Por qué?
    # El metodo de direccionamiento abierto con numero primo es mas eficiente, ya que 
    #   el factor de carga es menor, por lo que la probabilidad de colisiones es menor.
    #   ademas, el metodo de direccionamiento abierto con numero primo tiene una menor
    #   cantidad de colisiones que el metodo de direccionamiento abierto normal.
    