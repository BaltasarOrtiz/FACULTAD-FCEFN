import numpy as np

class tablaHash_DA_primo: 
    __dimension : int
    __tabla : np.ndarray
    __contador : int

    def __init__(self, dimension):
        self.__dimension = self.getPrimo(int(dimension//0.7)) 
        self.__tabla = np.empty(self.__dimension, dtype= int)
        self.__contador = 0

        for i in range(0,self.__dimension):
            self.__tabla[i] = 0
    
    def getPrimo(self, numero):
        for i in range(2, numero):
            if numero % i == 0:
                return self.getPrimo(numero+1)
        return numero

    def promedioColisiones(self):
        return self.__contador/self.__dimension

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
    
#---------------------Funciones de Transformacion---------------------#

    def metodoDivision(self, valor):
        return valor % self.__dimension

    def metodoExtraccionClaves(self, valor): 
        valor = valor % 100 
        return valor % self.__dimension
    
    def metodoPlegado(self, valor):
        acumulador = 0

        while valor != 0:
            acumulador += valor % 10
            valor //= 10

        return acumulador % self.__dimension

    def metodoCuadradosMedios(self, valor): 
        return int(str(valor**2)[1:-1]) % self.__dimension

    def metodoClavesAlfanumericas(self, valor):
        acumulador = 0

        for i in range(0, len(str(valor))):
            acumulador += ord(str(valor)[i])

        return acumulador % self.__dimension

#---------------------------------------------------------------------------------------------------------------------------------

class EncadenamientoHash:
    __dimension: int
    __tabla = None

    def __init__(self, dimension):
        self.__dimension = self.getPrimo(int(dimension//0.7)) 
        self.__tabla = np.empty(self.__dimension, dtype=listaEncadenada) #type: ignore
    
        for i in range(0,self.__dimension):
            self.__tabla[i] = None
    
    def getPrimo(self, numero):
        for i in range(2, numero):
            if numero % i == 0:
                return self.getPrimo(numero+1)
        return numero
    
    def insertarHash(self, valor):
        direccion = self.metodoPlegado(valor)
        if self.__tabla[direccion] == None: #type: ignore
            self.__tabla[direccion] = listaEncadenada() #type: ignore
        self.__tabla[direccion].insertarLista(valor) #type: ignore

    def buscar(self, valor):
        direccion = self.metodoPlegado(valor)
        if self.__tabla[direccion] == None: #type: ignore
            return "No se encontro el valor"
        else:
            return direccion