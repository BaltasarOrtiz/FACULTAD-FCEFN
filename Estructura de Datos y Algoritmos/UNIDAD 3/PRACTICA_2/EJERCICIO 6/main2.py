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

if __name__ == '__main__':
    cola = colaEncadenada()
    #datos de simulacion
    tiempoSimulacion = 60
    tiempoAtencion = 5
    frecuencia = 2
    #tiempoActualCajero = tiempoAtencion + 1

    #variables aux
    reloj = 0
    atendidos= 0
    tiempoEsperaAcumulado = 0

    while reloj <= tiempoSimulacion:
        numero1 = random.random()

        print("Reloj: [{}]".format(reloj))

        if numero1 <= (1/frecuencia): #se llega a la cola
            cola.insertar(reloj)
            print("Llego cliente numero [{}]".format(reloj))
            
        #if tiempoActualCajero == tiempoAtencion + 1: #cajero desocupado
        if tiempoAtencion == 0:
            if not cola.vacia():
                cliente = cola.suprimir()
                tiempoEspera = reloj - cliente #type:ignore
                atendidos +=1
                tiempoEsperaAcumulado += tiempoEspera 

                print("Se atiende a cliente numero [{}]: tiempo de espera [{}]".format(cliente, tiempoEspera))
                tiempoAtencion = 5

        else: #cajero ocupado
            tiempoAtencion -= 1
        
        reloj+=1
    
    print("\n------------------------------------------------------\n")
    print("Cantidad de clientes atendidos: ", atendidos)
    print("El tiempo promedio de espera de los clientes fue de: ", round(tiempoEsperaAcumulado/atendidos, 2))
    print("\n------------------------------------------------------\n")

