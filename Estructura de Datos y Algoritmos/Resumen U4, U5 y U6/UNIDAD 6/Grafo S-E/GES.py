import os
import numpy as np
from listaEncadenada import listaEncadenada

class GrafoEncadenado:
    __arreglo: np.ndarray
    __cantidadV: int

    def __init__(self, cantidadV: int):
        self.__cantidadV = cantidadV
        self.__arreglo = np.empty(cantidadV, dtype=listaEncadenada)
    
        # Inicializar cada lista
        for i in range(cantidadV):
            self.__arreglo[i] = listaEncadenada()
    
    def crearArista(self, origen, destino):
        self.__arreglo[origen].insertar(destino) # Insertar en la lista de origen
        self.__arreglo[destino].insertar(origen) # Insertar en la lista de destino

    def obtenerAdyacentes(self, vertice):
        lista = []
        aux = self.__arreglo[vertice].getCabeza()
        while aux is not None:
            lista.append(aux.getDato())
            aux = aux.getSiguiente()
        return lista

    def esAciclico(self):
        for i in range(self.__cantidadV):
            if self.esAciclicoRecursivo(i, [False] * self.__cantidadV, -1):
                return False
        return True
    
    def esAciclicoRecursivo(self, vertice, visitados, padre):
        visitados[vertice] = True

        for i in self.obtenerAdyacentes(vertice):
            if not visitados[i]:
                if self.esAciclicoRecursivo(i, visitados, vertice):
                    return True
            elif i != padre:
                return True
        return False

    def rea (self, verticeInicial): #Recorrido en anchura 
        lista = []
        visitados = [False] * self.__cantidadV
        cola = [verticeInicial]
        visitados[verticeInicial] = True

        while cola:
            vertice = cola.pop(0)
            lista.append(vertice)

            for i in self.obtenerAdyacentes(vertice):
                if not visitados[i]:
                    cola.append(i)
                    visitados[i] = True
        return lista
              
    def rep (self, verticeInicial): #Recorrido en profundidad
        lista = []
        self.repRec(verticeInicial, [False] * self.__cantidadV, lista)
        return lista

    def repRec(self, verticeInicial, visitados, lista):
        visitados[verticeInicial] = True
        lista.append(verticeInicial)
        
        for i in self.obtenerAdyacentes(verticeInicial):
            if not visitados[i]:
                self.repRec(i, visitados, lista)
    
    def camino(self, origen, destino):    
        return destino in self.rep(origen)
    
    def esConexo(self): #Si todos los vertices estan conectados
        return len(self.rea(0)) == self.__cantidadV #type: ignore
#-------------------------------------------------------------------------------------------------------------------------------------

class GrafoSecuencial:
    __CantidadV : int
    __matriz : np.ndarray

    def __init__(self, n):
        self.__CantidadV = n
        self.__matriz = np.zeros((n, n), dtype=int)

    def crearArista(self, origen, destino):
        if (origen <= self.__CantidadV and destino <= self.__CantidadV) and (origen >= 0 and destino >= 0):
            self.__matriz[origen][destino] = 1 #type: ignore
            self.__matriz[destino][origen] = 1 #type: ignore
        else:
            print("Error: vertices no validos")

    def obtenerAdyacentes(self, i):
        adyacentes = []
        for j in range(0,self.__CantidadV):
            if self.__matriz[i][j] == 1: #type: ignore
                adyacentes.append(j)
        return adyacentes

    def esAciclico(self):
        for i in range(self.__CantidadV):
            if self.esAciclicoRecursivo(i, [False] * self.__CantidadV, -1):
                return False
        return True
    
    def esAciclicoRecursivo(self, vertice, visitados, padre):
        visitados[vertice] = True

        for i in self.obtenerAdyacentes(vertice):
            if not visitados[i]:
                if self.esAciclicoRecursivo(i, visitados, vertice):
                    return True
            elif i != padre:
                return True
        return False
    
    def rea(self, verticeInicial):
        lista = []
        visitados = [False] * self.__CantidadV
        cola = [verticeInicial]
        visitados[verticeInicial] = True

        while cola:
            vertice = cola.pop(0)
            lista.append(vertice)

            for i in self.obtenerAdyacentes(vertice):
                if not visitados[i]:
                    cola.append(i)
                    visitados[i] = True
        
        return lista
    
    def rep(self, verticeInicial):
        lista = []
        self.repRecursivo(verticeInicial,[False] * self.__CantidadV, lista)
        return lista

    def repRecursivo(self, verticeInicial, visitados, lista):
        visitados[verticeInicial] = True
        lista.append(verticeInicial)

        for i in self.obtenerAdyacentes(verticeInicial):
            if not visitados[i]:
                self.repRecursivo(i, visitados, lista)
    
    def camino(self, origen, destino):
        return destino in self.rep(origen)

    def esConexo(self):
        return len(self.rea(0)) == self.__CantidadV


# Metodos iguales
# esConexo,esAciclico(se diferencia en el recursivo),rep(se diferencia en el rep recursivo),Camino