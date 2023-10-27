import numpy as np
import random

class GrafoSecuencial:
    __CantidadV = 0
    __matriz = None

    def __init__(self, n):
        self.__CantidadV = n
        self.__matriz = np.zeros((n, n), dtype=int)

    def crear_arista(self, i, j):
        if (i <= self.__CantidadV and j <= self.__CantidadV) and (i >= 0 and j >= 0):
            self.__matriz[i][j] = 1
            self.__matriz[j][i] = 1
        else:
            print("Error: vertices no validos")

    def obtener_adyacentes(self, i):
        adyacentes = []
        for j in range(0,self.__CantidadV):
            if self.__matriz[i][j] == 1:
                adyacentes.append(j)
        return adyacentes

    def es_conexo(self):
        band = True
        i = 0
        while band and i < self.__CantidadV:
            if len(self.obtener_adyacentes(i)) == 0:
                band = False
            else:
                i+=1
        if band:
            print("El grafo es conexo")
        else:
            print("El grafo no es conexo")

    #Funciones para saber si es aciclico
    def es_aciclicoRecursivo(self):
        visitados = [False] * self.__CantidadV
        for i in range(self.__CantidadV):
            if not visitados[i]:
                if self.es_aciclicoRecursivoAux(i, visitados, -1):
                    return False
        return True
    
    #Funcion auxiliar para saber si es aciclico
    def es_aciclicoRecursivoAux(self, v, visitados, padre):
        visitados[v] = True
        for i in self.obtener_adyacentes(v):
            if not visitados[i]:
                if self.es_aciclicoRecursivoAux(i, visitados, v):
                    return True
            elif i != padre:
                return True
        return False

    def recorrido_en_anchura(self, verticeInicial):
        visitados = [False] * self.__CantidadV
        cola = []
        visitados[verticeInicial] = True
        cola.append(verticeInicial)
        while len(cola) > 0:
            vertice = cola.pop(0)
            print(vertice, end=' ')
            for i in self.obtener_adyacentes(vertice):
                if not visitados[i]:
                    visitados[i] = True
                    cola.append(i)
        print()

    def recorrido_en_profundidad(self, verticeInicial):
        visitados = [False] * self.__CantidadV
        self.recorrido_en_profundidad_aux(verticeInicial, visitados)
        print()

    def recorrido_en_profundidad_aux(self, vertice, visitados):
        visitados[vertice] = True
        print(vertice, end=' ')
        for i in self.obtener_adyacentes(vertice):
            if not visitados[i]:
                self.recorrido_en_profundidad_aux(i, visitados)
    
    def mostrarGrafo(self):
        print("Grafo: ")

        print("   ",end='')
        for k in range(self.__CantidadV):
            print("[{}]".format(k),end='')

        print()        
        for i in range(self.__CantidadV):
            print("[{}]".format(i),end='')
            for j in range(self.__CantidadV):
                print(" {} ".format(self.__matriz[i][j]),end='') #type: ignore 
            print()
    
    def camino(self, origen, destino):
        visitados = [False] * self.__CantidadV #Lista de visitados: False = no visitado, True = visitado
        return self.caminoAux2(origen, destino, visitados, camino=[]) #Se llama a la funcion auxiliar y se devuelve el camino
    
    #En este primer camino se devuelve un booleano
    def caminoAux(self, origen, destino, visitados):
        visitados[origen] = True
        if origen == destino:
            return True
        for i in self.obtener_adyacentes(origen):
            if not visitados[i]:
                if self.caminoAux(i, destino, visitados):
                    return True
        return False

    #En este segundo camino se inserta en una lista el camino que se va recorriendo
    def caminoAux2(self, origen, destino, visitados, camino):
        visitados[origen] = True #Se marca como visitado
        camino.append(origen) #Se agrega a la lista camino
        
        if origen == destino: #Si el origen es igual al destino, se devuelve el camino
            return camino #Se devuelve el camino
        
        for i in self.obtener_adyacentes(origen): #Se recorren los adyacentes del origen
            if not visitados[i]: #Si no esta visitado
                if self.caminoAux2(i, destino, visitados, camino): #Se llama recursivamente
                    return camino #Se devuelve el camino
        camino.pop() #Si no se encuentra el camino, se elimina el ultimo elemento de la lista
    
if __name__ == '__main__':
    grafo = GrafoSecuencial(5)
    grafo.crear_arista(1, 4)
    grafo.crear_arista(1, 2)
    grafo.crear_arista(2, 3)
    grafo.crear_arista(3, 4)
    grafo.crear_arista(4, 0)
    grafo.mostrarGrafo()
    #print("Adyacentes de 1: ", grafo.obtener_adyacentes(1))
    #grafo.es_conexo()
    #print("Es aciclico?: ", grafo.es_aciclicoRecursivo())
    #print("\n\n")
    #print("Recorrido en Anchura: ")
    #grafo.recorrido_en_anchura(1)
    #print("Recorrido en Profundidad: ")
    #grafo.recorrido_en_profundidad(1)
    print("Camino entre 1 y 3: ", grafo.camino(1, 3))