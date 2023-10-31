import numpy as np
import os 

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

    def esConexo(self):
        return len(self.rea(0)) == self.__CantidadV

    def esAciclico(self):
        for i in range(self.__CantidadV):
            if self.esAciclicoRecursivo(i, [False] * self.__CantidadV, -1):
                return False
        return True
    
    def esAciclicoRecursivo(self, vertice, visitados, padre):
        visitados[vertice] = True

        # Iterar a través de la lista del vértice
        for i in self.obtenerAdyacentes(vertice):
            # Si el vecino no ha sido visitado, intentar encontrar un ciclo desde él
            if not visitados[i]:
                if self.esAciclicoRecursivo(i, visitados, vertice):
                    return True
            # Si el vecino ha sido visitado y no es el padre del vértice actual, entonces hay un ciclo
            elif i != padre:
                return True
        return False
    
    def rea(self, verticeInicial):
        visitados = [False] * self.__CantidadV
        lista = []

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
        visitados = [False] * self.__CantidadV
        lista = []
        self.repRecursivo(verticeInicial, visitados, lista)
        return lista

    def repRecursivo(self, vertice, visitados, lista):
        visitados[vertice] = True
        lista.append(vertice)

        for i in self.obtenerAdyacentes(vertice):
            if not visitados[i]:
                self.repRecursivo(i, visitados, lista)
    
    def camino(self, origen, destino):
        return destino in self.rep(origen)

    #Otros métodos: 
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

if __name__ == '__main__':
    os.system('cls')
    grafo = GrafoSecuencial(4)

    grafo.crearArista(0, 1)
    grafo.crearArista(0, 2)
    grafo.crearArista(1, 3)
    grafo.crearArista(2, 3)
    grafo.mostrarGrafo()

    print("Recorrido en anchura: ", grafo.rea(0))
    print("Recorrido en profundidad: ", grafo.rep(0))
    print("Es conexo: ", grafo.esConexo())
    print("Camino entre 0 y 3: ", grafo.camino(0, 3))
