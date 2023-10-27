import numpy as np
import random

class GrafoSecuencial:
    __CantidadV = 0
    __matriz = None

    def __init__(self, n):
        self.__CantidadV = n
        self.__matriz = np.zeros((n, n), dtype=int)
        #self.__matriz = np.empty((n, n) , dtype=int)

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

    def es_aciclicoRecursivo(self):
        visitados = [False] * self.__CantidadV
        for i in range(self.__CantidadV):
            if not visitados[i]:
                if self.es_aciclicoRecursivoAux(i, visitados, -1):
                    return False
        return True
    
    def es_aciclicoRecursivoAux(self, v, visitados, padre):
        visitados[v] = True
        for i in self.obtener_adyacentes(v):
            if not visitados[i]:
                if self.es_aciclicoRecursivoAux(i, visitados, v):
                    return True
            elif i != padre:
                return True
        return False
        
    

    def mostrarGrafo(self):
        for i in range(self.__CantidadV):
            print("[{}]".format(i),end=' ')
            for j in range(self.__CantidadV):
                print(self.__matriz[i][j], end=' ')
            print()
    
    def getMatriz(self):
        return self.__matriz

if __name__ == '__main__':
    grafo = GrafoSecuencial(2)
    grafo.crear_arista(0, 1)
    grafo.crear_arista(0, 0)
    grafo.crear_arista(1, 1)
    grafo.mostrarGrafo()
    print("Adyacentes de 1: ", grafo.obtener_adyacentes(1))
    grafo.es_conexo()
    print("Es aciclico?: ", grafo.es_aciclicoRecursivo())