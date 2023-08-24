import os
import random

class Nodo:
    __dato : int
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
    
class colaEncadenada:
    __primero : None|Nodo
    __ultimo : None|Nodo
    __cantidad : int

    def __init__(self):
        self.__primero = None
        self.__ultimo = None
        self.__cantidad = 0

    def vacia(self):
        return self.__cantidad == 0
    
    def insertar(self, dato):
        nuevoNodo = Nodo(dato)
        if self.__ultimo == None:
            self.__primero = nuevoNodo
        else:
            self.__ultimo.setSiguiente(nuevoNodo)
        
        self.__ultimo = nuevoNodo
        self.__cantidad += 1
    
    def suprimir(self):
        if self.vacia():
            print("La cola esta vacia")
        else:
            x = self.__primero.getDato() #type: ignore
            self.__primero = self.__primero.getSiguiente() #type: ignore
            self.__cantidad -= 1

            if self.__primero is None: #esto lo utilizamos en el caso hipotetico de que nos quedemos sin elementos en el caso hipotetico
                self.__ultimo = None

            return x
    
    def recorrer(self):
        aux = self.__primero
        while aux != None:
            print("Elemento: ", aux.getDato())
            aux = aux.getSiguiente()
    
    def getCantidad(self):
        return self.__cantidad

class manejador_Simulador: 
    __cola: colaEncadenada
    __ts : int
    __tac : int
    __fr : int 
    __max : int
    __reloj : int

    def __init__ (self, tiempo_simulacion, tiempo_atencion, tiempo_frecuencia):
        self.__cola = colaEncadenada()
        self.__ts = tiempo_simulacion
        self.__tac = tiempo_atencion
        self.__fr = tiempo_frecuencia
        self.__tadc = tiempo_atencion + 1 #tiempo actual del cajero
        self.__max = -1
        self.__reloj = 0

    #Ingresar el tiempo de atención de cajero y la frecuencia de llegada de los clientes
    
    def simular(self):
        while self.__reloj <= self.__ts:
            self.__cola.insertar(self.__reloj)
            self.cajero()
            self.__reloj += 1
        print("El tiempo maximo de espera aprox de cada cliente fue de: {} minutos".format(self.__max))

    def ingresarCliente(self):
        numero = random.random()
        if numero <= (1/self.__fr): #si(llega cliente)
            self.__cola.insertar(self.__reloj)
            print("Llega cliente")
    
    def cajero(self):
        #si viene el primero se atiende, cuando venga el segundo espera, y cuando venga el tercero se atiende el segundo
        if self.__tadc == self.__tac + 1: #cajero desocupado
            if not self.__cola.vacia():
                tiempo = self.__reloj - self.__cola.suprimir() #type:ignore
                self.__tadc = self.__tac
                if tiempo > self.__max:
                    self.__max = tiempo

        else: #cajero ocupado
            self.__tadc -= 1
            if self.__tadc == 0:
                self.__tadc = self.__tac +1


if __name__ == "__main__":
    os.system("cls")
    ms = manejador_Simulador(60,5,2)
    ms.simular()