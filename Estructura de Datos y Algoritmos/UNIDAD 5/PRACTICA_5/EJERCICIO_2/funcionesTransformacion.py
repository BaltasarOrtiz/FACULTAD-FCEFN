import numpy as np
import os

class tablaHash_DA_primo: #Direccionamiento Abierto (DA) con num primo para la dimension
    __dimension : int
    __tabla : np.ndarray
    __contador : int

    def __init__(self, dimension):
        self.__dimension = self.getPrimo(int(dimension//0.7)) #Factor de carga = 0.7 ejemplo 100 // 0.7 = 142 primo mas cercano 149
        self.__tabla = np.empty(self.__dimension, dtype= int)
        self.__contador = 0
    
        for i in range(0,self.__dimension):
            self.__tabla[i] = 0
    
    def getPrimo(self, numero):
        for i in range(2, numero):
            if numero % i == 0:
                return self.getPrimo(numero+1)
        return numero
    
    def insertar(self, valor):
        direccion = self.metodoPlegado(valor)
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
    
    #Funciones de Transformacion
    def metodoDivision(self, valor):
        return valor % self.__dimension

    def metodoExtraccionClaves(self, valor): #Explicacion: extrae el ultimo digito de cada numero como clave para la tabla hash
        valor = valor % 100 #Ejemplo: 123 -> 123 % 100 = 23
        return valor % self.__dimension
    
    def metodoPlegado(self, valor): #El consiste en sumar sub_mitades de un numero y luego sacar el modulo de la dimension 
        acumulador = 0

        while valor != 0:
            acumulador += valor % 10
            valor //= 10

        #ejemplo 123 -> 1+2+3 = 6 -> 6 % 149 = 6
        #ejemplo en caso % o // 100 : 123 -> 1+23 = 24 -> 24 % 149 = 24
        return acumulador % self.__dimension

    def metodoCuadradosMedios(self, valor): #Consiste en que te de los valores centrales del digito como clave 
        #print (int(str(valor**2)[1:-1]))
        return int(str(valor**2)[1:-1]) % self.__dimension #Ejemplo: 123 -> 123^2 = 15129 -> 5129 -> 512 % 149 = 65 

    def metodoClavesAlfanumericas(self, valor):
        acumulador = 0

        for i in range(0, len(str(valor))):
            acumulador += ord(str(valor)[i])

        return acumulador % self.__dimension
        
        #ord() -> devuelve el valor unicode de un caracter

if __name__ == "__main__":
    os.system("cls")
    tabla = tablaHash_DA_primo(100)

    tabla.insertar(123)
    
    #Mostrar tabla
    tabla.mostrar()
