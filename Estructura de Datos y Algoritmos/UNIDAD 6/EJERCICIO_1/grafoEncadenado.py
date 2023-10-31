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
    
    def insertarArista(self, origen, destino):
        self.__arreglo[origen].insertar(destino) # Insertar en la lista de origen
        self.__arreglo[destino].insertar(origen) # Insertar en la lista de destino
            
    def getAdyacentes(self, vertice):
        lista = None
        
        if vertice >= 0 and vertice < self.__cantidadV:
            lista = self.__arreglo[vertice]
        else:
            print("Error: vertice no valido")
        
        return lista

    def esConexo(self): #Si todos los vertices estan conectados
        return len(self.rea(0)) == self.__cantidadV

    def esAciclico(self): #Si no tiene ciclos
        for i in range(self.__cantidadV):
            if self.esAciclicoRecursivo(i, [False] * self.__cantidadV, -1):
                return False
        return True

    def esAciclicoRecursivo(self, vertice, visitados, padre):
        visitados[vertice] = True

        # Iterar a través de la lista encadenada del vértice
        nodo = self.__arreglo[vertice].getCabeza()
        while nodo is not None:
            vecino = nodo.getDato()

            # Si el vecino no ha sido visitado, intentar encontrar un ciclo desde él
            if not visitados[vecino]:
                if self.esAciclicoRecursivo(vecino, visitados, vertice):
                    return True

            # Si el vecino ya ha sido visitado y no es el padre del vértice actual, se encontró un ciclo
            elif vecino != padre:
                return True

            nodo = nodo.getSiguiente()

        return False
    
    def rea (self, verticeInicial): #Recorrido en anchura 
        lista = []
        visitados = [False] * self.__cantidadV
        cola = [verticeInicial]

        while cola:
            vertice = cola.pop(0)
            lista.append(vertice)
            visitados[vertice] = True
            
            # Iterar a través de la lista encadenada del vértice
            nodo = self.__arreglo[vertice].getCabeza()
            while nodo is not None:
                vecino = nodo.getDato()
                if not visitados[vecino]:
                    cola.append(vecino)
                    visitados[vecino] = True
                nodo = nodo.getSiguiente()
        
        return lista
            
    def rep (self, verticeInicial): #Recorrido en profundidad
        lista = []
        self.repRec(verticeInicial, [False] * self.__cantidadV, lista)
        return lista

    def repRec(self, verticeInicial, visitados, lista):
        visitados[verticeInicial] = True
        lista.append(verticeInicial)
        
        # Iterar a través de la lista encadenada del vértice
        nodo = self.__arreglo[verticeInicial].getCabeza()
        while nodo is not None:
            vecino = nodo.getDato()
            if not visitados[vecino]:
                self.repRec(vecino, visitados, lista)
            nodo = nodo.getSiguiente()
    
    def camino(self, origen, destino):
        return destino in self.rep(origen)

    # Otras metodos:        
    def mostrarGrafo(self):
        for i in range(self.__cantidadV):
            print(f'{i} --> ', end='')

            lista_vecinos = self.__arreglo[i].getCabeza()  # Obtener la cabeza de la lista
            while lista_vecinos is not None:
                print(f'{lista_vecinos.getDato()} --> ', end='')
                lista_vecinos = lista_vecinos.getSiguiente()
            
            print("None")  # Marcar el final de los vecinos

if __name__ == '__main__':
    os.system('cls')
    grafo = GrafoEncadenado(4)

    grafo.insertarArista(0, 1)
    grafo.insertarArista(0, 2)
    grafo.insertarArista(1, 3)
    grafo.insertarArista(2, 3)
    grafo.mostrarGrafo()

    print("Recorrido en anchura: ", grafo.rea(0))
    print("Recorrido en profundidad: ", grafo.rep(0))
    print("Es conexo: ", grafo.esConexo())
    print("Camino entre 0 y 3: ", grafo.camino(0, 3))