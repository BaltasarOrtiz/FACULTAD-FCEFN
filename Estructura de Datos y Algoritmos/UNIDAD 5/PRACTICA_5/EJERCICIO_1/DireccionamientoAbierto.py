# Politica de Manejo de Colisiones: Direccionamiento Abierto
# Función de Transformación de Claves: Método de la división
# Procesamiento de Claves Sinónimas: Secuencia de prueba lineal


import numpy as np

class DireccionamientoAbierto:
    __dimension: int
    __tabla = None
    __longPrueba: int|


    def __init__(self, cantClaves, usarPrimo=False):
        self.__diemension = cantClaves

        if usarPrimo:
            self.__dimension = self.__getPrimo(int(self.__dimension/0.7)+1)

        self.__tabla = np.empty(self.__dimension, dtype=None)
        self.__longPrueba = 0
        

    def __getPrimo(self,numero):
        for i in range(2,numero):
            if numero % i == 0:
                return self.__getPrimo(numero+1)
        return numero

#-----------------------------------------------------------------------------------------------

    def insertar(self,valor):
        index = self.__PruebaLineal(valor)
        
        if index != -1:
            self.__tabla[index] = valor
        else:
            #Peor caso: recorrer todo el arreglo y no encontrar posición disponible
            print("Tabla llena, no es posible almacenar la clave")
    
    def buscar(self,valor):
        index = self.__PruebaLineal(valor)
        if index != -1:
            return self.__tabla[index]
        else:
            return None
    
    def calcularFactorCarga(self):
        total = np.count_nonzero(self.__tabla != None) #Cuenta el número de elementos no nulos
        print(self.__dimension)
        return (total / self.__dimension)
    
    def getLongPrueba(self):
        return self.__longPrueba
    
    #Metodos Auxiliares---------------------------------------------------------
    # FUNCIÓN DE TRANSFORMACIÓN H(K)
    def __metododeDivison(self,valor): #Método de la división (módulo) h(k) = k % m
        return valor % self.__dimension
    
    
    # POLÍTICA DE MANEJO DE COLISIONES
    def __PruebaLineal(self,valor): #Secuencia de prueba lineal - Retorna la posición donde se debe almacenar la clave
        IndexOrigen = index = self.__metododeDivison(valor)
        self.__longPrueba = 0
        
        while self.__tabla[index] != None and self.__tabla[index] != valor:
            self.__longPrueba += 1
            index = (index + 1) % self.__dimension
            
            if index == IndexOrigen:
                return -1 #Tabla llena
        
        return index