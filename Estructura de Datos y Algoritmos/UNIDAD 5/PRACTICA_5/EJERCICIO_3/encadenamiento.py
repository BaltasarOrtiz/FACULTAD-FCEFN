import numpy as np

class Nodo:
    __dato = None
    __siguiente = None

    def __init__(self, dato):
        self.__dato = dato
        self.__siguiente = None
    
    def getDato(self):
        return self.__dato
    
    def getSiguiente(self):
        return self.__siguiente
    
    def setDato(self, dato):
        self.__dato = dato
    
    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente
    
class listaEncadenada:
    __cabeza = None
    __cantidad: int
    
    def __init__ (self):
        self.__cabeza 
        self.__cantidad = 0
    
    def vacio(self):
        return self.__cabeza == None
 
    def buscar(self, dato):
        aux = self.__cabeza
        
        while aux != None and aux.getDato() != dato:
            aux = aux.getSiguiente()
        
        if aux == None:
            return -1
        else:
            return aux

    def insertarLista(self, dato):
        nuevo = Nodo(dato)
        if self.vacio() or dato < self.__cabeza.getDato(): #type: ignore
            nuevo.setSiguiente(self.__cabeza)
            self.__cabeza = nuevo
        else:
            aux = self.__cabeza
            anterior = None
            
            while aux is not None and dato > aux.getDato():
                anterior = aux
                aux = aux.getSiguiente()

            nuevo.setSiguiente(aux)
            anterior.setSiguiente(nuevo) #type: ignore
        self.__cantidad += 1
    
    def eliminar(self, dato):
        aux = self.__cabeza
        anterior = None

        while aux != None and aux.getDato() != dato:
            anterior = aux
            aux = aux.getSiguiente()
        
        if aux == None:
            print("El dato no existe")
        elif anterior == None:
            self.__cabeza = aux.getSiguiente() 
        else:
            anterior.setSiguiente(aux.getSiguiente())

    def mostrarLista(self):
        aux = self.__cabeza
        while aux != None:
            print(aux.getDato())
            aux = aux.getSiguiente()


class EncadenamientoHash:
    __dimension: int
    __tabla = None

    def __init__(self, dimension):
        self.__dimension = self.getPrimo(int(dimension//0.7)) #Factor de carga = 0.7 ejemplo 100 // 0.7 = 142 primo mas cercano 149
        self.__tabla = np.empty(self.__dimension, dtype=listaEncadenada)
    
        for i in range(0,self.__dimension):
            self.__tabla[i] = None
    

    def getPrimo(self, numero):
        for i in range(2, numero):
            if numero % i == 0:
                return self.getPrimo(numero+1)
        return numero
    
    def metodoPlegado(self, valor): #El consiste en sumar sub_mitades de un numero y luego sacar el modulo de la dimension 
        acumulador = 0

        while valor != 0:
            acumulador += valor % 10
            valor //= 10

        #ejemplo 123 -> 1+2+3 = 6 -> 6 % 149 = 6
        #ejemplo en caso % o // 100 : 123 -> 1+23 = 24 -> 24 % 149 = 24
        return acumulador % self.__dimension

    def insertarHash(self, valor):
        direccion = self.metodoPlegado(valor)
        if self.__tabla[direccion] == None:
            self.__tabla[direccion] = listaEncadenada()
        self.__tabla[direccion].insertarLista(valor)


    def mostrarHash(self):
        for i in range(0, self.__dimension):
            print("Posicion: ", i)
            if self.__tabla[i] != None:
                self.__tabla[i].mostrarLista()
            else:
                print("Vacio")



if __name__ == "__main__":
    encadenamiento = EncadenamientoHash(100)
    for i in range(0,100):
        encadenamiento.insertarHash(i)

    encadenamiento.mostrarHash()

